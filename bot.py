import os
from discord.ext import commands
from pkg.models import records
import pkg.models.time as vtime
import pkg.models.map as vmap
from tabulate import tabulate
import pkg.store.file as file

botPrefix = "tm "
botDescription = "VROUM VROUM"

noPBString = "You didn't beat your PB on map {}. Current PB: {}"
newPBString = "NEW PB on map {}: {}"
noServerRecordString = "Server record is currently held by {} in {}"
newServerRecordString = "NEW SERVER RECORD on map {}: {}"

bot = commands.Bot(command_prefix=botPrefix, description=botDescription)
r = records.Records()


@bot.event
async def on_ready():
    print("bot launched")

@bot.command()
async def server_info(ctx):
    server = ctx.guild
    text_channel_count = len(server.text_channels)
    voice_channel_count = len(server.voice_channels)
    server_description = server.description
    number_of_person = server.member_count
    server_name = server.name
    message = f"""
    Le serveur **{server_name}** contient *{number_of_person}* personnes !
    La description du serveur est {server_description}.
    Ce serveur possède {text_channel_count} salons textuels et {voice_channel_count} salon vocaux.
    """
    await ctx.send(message)


@bot.command()
async def github(ctx):
    await ctx.send("Feel free to contribute !\nhttps://github.com/Luc-del/TrackmaniaDiscord")


@bot.command()
async def pb(ctx, map_idx, time):
    map_idx = vmap.validate(map_idx)
    if map_idx is None:
        return
    time = vtime.parse(time)
    if time is None:
        return

    player_name = ctx.author.name
    str_time = vtime.to_string(time)
    _, old_server_record = r.get_server_record(map_idx)

    # beat his pb, check for server record
    if r.register_player_time(player_name, map_idx, time):
        best_player_name, server_record = r.get_server_record(map_idx)
        if old_server_record is None or server_record < old_server_record:
            bot_answer = newServerRecordString.format(map_idx, str_time)
        else:
            bot_answer = newPBString.format(map_idx, str_time) + \
                         os.linesep + \
                         noServerRecordString.format(best_player_name, server_record)
        await ctx.send(bot_answer)
        return

    await ctx.send(noPBString.format(map_idx, str_time))

@bot.command()
async def records(ctx, player_name, *map_idx):
    if map_idx:
        map_idx = vmap.validate_list(map_idx)
    else:
        map_idx = vmap.get_list()

    if player_name.lower() == "server":
        header = ["map", "player", "time"]
        rec = get_server_records(map_idx)
    else:
        if not r.player_exists(player_name):
            await ctx.send("unknown player " + player_name)
            return

        header = ["map", "time"]
        rec = get_player_records(player_name, map_idx)

    tab = tabulate(rec, headers=header, tablefmt="fancy_grid", stralign='center')
    await ctx.send("```" + tab + "```")


def get_server_records(map_idx):
    rec = []
    for idx in map_idx:
        name, time = r.get_server_record(idx)
        if name is None:
            name, time = "-", "-"
        rec.append((idx, name, vtime.to_string(time)))

    return rec


def get_player_records(player_name, map_idx):
    rec = []
    for idx in map_idx:
        time = r.get_player_pb(player_name, idx)
        if time is None:
            time = "-"
        rec.append((idx, vtime.to_string(time)))

    return rec


@bot.command()
async def delete(ctx, map_idx):
    map_idx = vmap.validate(map_idx)
    if map_idx is None:
        return

    player_name = ctx.author.name
    r.delete_player_pb(player_name, map_idx)