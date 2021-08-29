import os
from discord.ext import commands
from pkg.models import records
import pkg.models.time as vtime
import pkg.models.map as vmap
from tabulate import tabulate

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
async def pb(ctx, map_idx, time):
    map_idx, ok = vmap.validate(map_idx)
    if not ok:
        return
    time, ok = vtime.parse(time)
    if not ok:
        return

    player_name = ctx.author.name
    is_pb, is_server_record = r.add_pb(player_name, map_idx, time)
    player_pb = r.get_player_pb(map_idx, player_name)
    player_server_record, server_record, _ = r.get_server_record(map_idx)

    await ctx.send(pb_string(player_server_record, map_idx, is_pb, player_pb, is_server_record, server_record))


def pb_string(player_server_record, map_idx, is_pb, time, is_server_record, server_time):
    if is_server_record:
        return newServerRecordString.format(map_idx, server_time)
    if is_pb:
        return newPBString.format(map_idx, time) + os.linesep + noServerRecordString.format(player_server_record, server_time)
    return noPBString.format(map_idx, time)


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
        name, time, ok = r.get_server_record(idx)
        if not ok:
            name, time = "-", "-"
        rec.append((idx, name, str(time)))

    return rec


def get_player_records(player_name, map_idx):
    rec = []
    for idx in map_idx:
        time = r.get_player_pb(idx, player_name)
        if not time:
            time = "-"
        rec.append((idx, str(time)))

    return rec
