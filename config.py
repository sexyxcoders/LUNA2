import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 23321960
API_HASH = "a334659dd1e01f78c189fc93fc6db455"
BOT_TOKEN = "7922289237:AAEjHTUvg4hEbo1AgI_Edp2EOBWIw2i5R9k"
OWNER_USERNAME = "@Og_Goku_God_7"
BOT_USERNAME = "@Nefermusicbot"
BOT_NAME = "Nefer music"
ASSUSERNAME = "@Neferxassistant"
EVALOP = list(map(int, getenv("EVALOP", "5268691896").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Sasuke_680:Sasuke_680@cluster0.xds2ykw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGGER_ID = -1002918784392
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

GPT_API = getenv("GPT_API", None)
DEEP_API = getenv("DEEP_API", None)
OWNER_ID = 7793156995

HEROKU_APP_NAME = None
HEROKU_API_KEY = None
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/DeadliestOne/Alya.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/eternal_bot_update")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Eternal_Anime_chat")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

STRING1 = getenv("STRING_SESSION" ,"BQFj3WgACAydO4RJ_jPjCgKS2WVN_Ly423URDOQOum0rStKdqIv-W--4-XfpzFkVNQcZoEhxXct9C4SDzWYBLz-zpt9QmKRVePHlaNrFst_c5LyDVwtxoWTiDbI75UpbGzdhKZbj_a_KjTVnV4BUGmW8OTuRgqi7OR1BEdpDa8NaGdQtnqvmYYr14SEl_HZP-t4EGUGj4upJEhMJpLft7rQ4mXY2i-88RP316uTsxQia7YJtAtg1G6krZjyJcCsznnvEePkbrlnUYmOkV0fprTW7XIP1WXdB-FfvGxwrM4UqJU5EstsW4We2pIhQonS-rK4sDDtPGr60BZ8aXawQqsKA6xNzyAAAAAFrDRd3AA") 
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦋", "🦋", "🕊️", "🦋", "🕊️", "🦋", "🦋", "🦋", "🪄", "💌", "🦋", "🦋", "🧨"
]

AYUV = [ "<b>нєу</b> {0}, 💗\n\n๏ ᴛʜɪs ɪs {1} !\n\n➻ {1} ɪs ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴍᴜsɪᴄ ᴄᴏᴍᴘᴀɴɪᴏɴ, ʜᴇʀᴇ ᴛᴏ ʙʀɪɴɢ ʜᴀʀᴍᴏɴʏ ᴛᴏ ʏᴏᴜʀ ᴅᴀʏ. EɴJᴏʏ sᴇᴀᴍʟᴇss ᴍᴜsɪᴄ ᴘʟᴀʏʙᴀᴄᴋ, ᴄᴜʀᴀᴛᴇᴅ ᴘʟᴀʏʟɪsᴛs, ᴀɴᴅ ᴇғғᴏʀᴛʟᴇss ᴄᴏɴᴛʀᴏʟ, ᴀʟʟ ᴀᴛ ʏᴏᴜʀ ғɪɴɢᴇʀᴛɪᴘs. Lᴇᴛ {1} ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟɪsᴛᴇɴɪɴɢ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴇᴀsᴇ ᴀɴᴅ sᴛʏʟᴇ.\n\n<b><u>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs :</b></u> ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n──────────────────\n<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs🦋.</b> "  ,
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/ggrsa1.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/830pjr.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/tkq9uh.jpg"
STATS_IMG_URL = "https://files.catbox.moe/0rmax6.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/tkq9uh.jpg"
TELEGRAM_VID_URL = "https://files.catbox.moe/tkq9uh.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/tkq9uh.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/s5Vfz84/photo-2025-01-05-21-49-51-7456552074738663428.jpg"
STATS_VID_URL = "https://files.catbox.moe/z1k13z.mp4"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
