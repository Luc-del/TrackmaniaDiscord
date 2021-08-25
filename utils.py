import yaml

discordConfigKey = "discord"
databaseConfigKey = "sheet"


def ReadConfig(file):
    file = yaml.load(open(file, "r"), Loader=yaml.FullLoader)
    return file[discordConfigKey], file[databaseConfigKey]
