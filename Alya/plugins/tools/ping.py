from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from Alya import app
from Alya.core.call import alya
from Alya.utils import bot_sys_stats
from Alya.utils.decorators.language import language
from Alya.utils.inline import supp_markup
from config import BANNED_USERS

LORD_ID = 5645075587

@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    user = message.from_user
    user_firstname = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
    bot_private_link = f"<a href='tg://user?id={app.me.id}'>Ꮢɪᴏ ᴛsᴜᴋᴀᴛsᴜᴋɪ</a>"
    lord_firstname = f"<a href='tg://user?id={5860411988}'>𝐒ᴀᴍ 𝐄ᴍᴘɪʀᴇ</a>"

    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )

    pytgping = await alya.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    if user.id == LORD_ID:
        ping_2_message = (
            f"🔱 I'ᴍ ᴀʟɪᴠᴇ ᴍʏ Qᴜᴇᴇɴ\n\n"
            f" ➣ ɪ'ᴍ {bot_private_link}\n"
            f" ➣ ᴄʀᴇᴀᴛᴏʀ ⌯ {lord_firstname}\n"
            f"┏━━━━━━━━━━━━━⧫\n"
            f"┠ ➥ Uᴘᴛɪᴍᴇ : {UP}\n"
            f"┠ ➥ Rᴀᴍ : {RAM}%\n"
            f"┠ ➥ ᴄᴘᴜ : {CPU}%\n"
            f"┠ ➥ ᴅɪsᴋ : {DISK}%\n"
            f"┠ ➥ ᴘʏ - ᴛɢᴄᴀʟʟs : <code>{resp}ᴍs</code>\n"
            f"┗━━━━━━━━━━━━━━⧫"
        )
    else:
        ping_2_message = (
            f"ʏᴏᴏ ! {user_firstname}\n\n"
            f"➣ ɪ'ᴍ {bot_private_link}\n"
            f"➣ ᴄʀᴇᴀᴛᴏʀ ⌯ {lord_firstname}\n"
            f"┏━━━━━━━━━━━━━⧫\n"
            f"┠ ➥ Uᴘᴛɪᴍᴇ : {UP}\n"
            f"┠ ➥ Rᴀᴍ : {RAM}%\n"
            f"┠ ➥ ᴄᴘᴜ : {CPU}%\n"
            f"┠ ➥ ᴅɪsᴋ : {DISK}%\n"
            f"┠ ➥ ᴘʏ - ᴛɢᴄᴀʟʟs : <code>{resp}ᴍs</code>\n"
            f"┗━━━━━━━━━━━━━━⧫"
        )

    await response.edit_text(
        ping_2_message.format(UP, RAM, CPU, DISK, resp, pytgping),
       
        reply_markup=supp_markup(_),
    )
