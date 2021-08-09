from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="VROUM VROUM")


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


token = open("config.txt", "r").read()

bot.run(token)
