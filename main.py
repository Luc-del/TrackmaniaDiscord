import utils.utils as utils
from bot.bot import *


config_dir = "cfg/"
config_file = "config.yml"

if __name__ == "__main__":
    discordToken, databaseToken = utils.ReadConfig(config_dir+config_file)
    bot.run(discordToken)

