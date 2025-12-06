import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NexaMusic import LOGGER, app, userbot
from NexaMusic.core.call import nexa
from NexaMusic.misc import sudo
from NexaMusic.plugins import ALL_MODULES
from NexaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    # Validate assistant sessions
    if not any([
        config.STRING1, config.STRING2, config.STRING3,
        config.STRING4, config.STRING5
    ]):
        LOGGER.error("Assistant session(s) missing! Please add Pyrogram SESSION strings.")
        return

    # Initialize sudo users
    await sudo()

    # Load banned & globally banned users
    try:
        gbanned = await get_gbanned()
        local_banned = await get_banned_users()

        for user_id in gbanned + local_banned:
            BANNED_USERS.add(user_id)

    except Exception:
        LOGGER.warning("Could not load banned user lists.")

    # Start main bot
    await app.start()

    # Import all plugin modules
    for module in ALL_MODULES:
        importlib.import_module(f"NexaMusic.plugins{module}")
    LOGGER.info("All NexaMusic modules loaded successfully.")

    # Start assistant userbots
    await userbot.start()

    # Start PyTgCalls
    await nexa.start()

    # Optional intro stream (music/video)
    try:
        await nexa.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER.error(
            "Voice chat is OFF in your log group/channel.\n\n"
            "NexaMusic cannot start until the VC is opened!"
        )
        return
    except Exception:
        pass

    # Load call decorators (handlers)
    await nexa.decorators()

    LOGGER.info("NexaMusic Started Successfully!")

    # Idle mode (keeps bot alive)
    await idle()

    # Shutdown sequence
    await app.stop()
    await userbot.stop()

    LOGGER.info("NexaMusic stopped. Goodbye!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())