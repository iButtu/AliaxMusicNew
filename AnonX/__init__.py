from AnonX.core.bot import AnonXBot
from AnonX.core.dir import dirr
from AnonX.core.git import git
from AnonX.core.userbot import Userbot
from AnonX.misc import dbb, heroku, sudo
from telethon import TelegramClient

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AnonXBot()
userbot = Userbot()
telethn = TelegramClient("AnonX", API_ID, API_HASH)

from AnonX.config import Development as Config
API_ID = Config.API_ID
API_HASH = Config.API_HASH

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
