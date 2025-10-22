import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 23321960
API_HASH = "a334659dd1e01f78c189fc93fc6db455"
BOT_TOKEN = "8380480804:AAFCjO70YKP-2NnamUjbsgCYbTQk49dLT48"
OWNER_USERNAME = "@Suicidemoments"
BOT_USERNAME = "@SafetronixMusicBot"
BOT_NAME = "𝖲𝖺𝖿𝖾𝗍𝗋𝗈𝗇𝗂𝗑 𝖬𝗎𝗌𝗂𝖼"
ASSUSERNAME = "@SafetronixAssistant"
EVALOP = list(map(int, getenv("EVALOP", "8076443359").split()))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ahad0181888:ahad0181888@cluster0.f9casz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGGER_ID = -1003138759746
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

GPT_API = getenv("GPT_API", None)
DEEP_API = getenv("DEEP_API", None)
OWNER_ID = 7857598507

HEROKU_APP_NAME = None
HEROKU_API_KEY = None
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/sexyxcoders/LUNA")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SafetronixNetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TNCmeetup")

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

STRING1 = getenv("STRING_SESSION" ,"BACOaU4AOrGAJ4ZSA0yWG9gRkyyYCKZlOerdlYeruqGK2LHwG8e35cmxpEfaZ4ArGoZ23w2LU3dZZZFoUUOl1ifBLuK91xqHBo4gWwtZdRDFUiKEDt1SYfwx7-AnlzgcaYiwDWRY7Raep-K-ARHS-HWUGLqGkDwCQ5KatrlIzrbZAAJQFL9kfxSi-I4ZnXTkPzEqSzOp8HaQDduh5LPzd7B_SLyS9MBbo9534zsLG_3vo-5LbKddmZ49RXIAAAvdLA4u0PFVBu3VMckRFTE26tds6wq8MQQP52TnNW0tkVcVmoHT1mNK9MBdqS8TDR65tWb-6JXFOVmeuFlZGn-zseAP2bFvuQAAAAHk8qpoAA") 
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