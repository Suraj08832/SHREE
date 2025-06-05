from shree.core.bot import SHREE
from shree.core.dir import dirr
from shree.core.git import git
from shree.core.userbot import Userbot
from shree.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SHREE()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
