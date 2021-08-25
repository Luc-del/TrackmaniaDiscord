from discord.ext import commands
import records
import validators.time as vtime
import validators.map as vmap

botPrefix = "tm "
botDescription = "VROUM VROUM"

bot = commands.Bot(command_prefix=botPrefix, description=botDescription)
r = records.Records()


@bot.event
async def on_ready():
    print("bot launched")


@bot.command()
async def coucou(ctx, *txt):
    await ctx.send("Coucou !" + "-".join(txt))


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
    map_idx, ok = vmap.parse(map_idx)
    if not ok:
        return
    time, ok = vtime.parse(time)
    if not ok:
        return

    is_pb, time = r.add_pb(ctx.author.name, map_idx, time)

    s = f"You didn't beat your PB on map {map_idx}. Current PB: {str(time)}"
    if is_pb:
        s = f"NEW PB on map {map_idx}: {str(time)}"
    await ctx.send(s)


