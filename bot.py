from discord.ext import commands
import records

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
async def serverInfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"""
    Le serveur **{serverName}** contient *{numberOfPerson}* personnes !
    La description du serveur est {serverDescription}.
    Ce serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux.
    """
    await ctx.send(message)


@bot.command()
async def pb(ctx, map_idx, time):
    map_idx = int(map_idx)
    time = float(time)

    is_pb, time = r.add_pb(ctx.author.name, map_idx, time)

    s = f"You didn't beat your PB on map {map_idx}. Old PB: {time}"
    if is_pb:
        s = f"NEW PB on map {map_idx}: {time}"
    await ctx.send(s)


