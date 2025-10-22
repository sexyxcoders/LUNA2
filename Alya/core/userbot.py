from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot:
    def __init__(self):
        self.one = (
            Client(
                name="Devine1",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING1),
                no_updates=True,
            )
            if config.STRING1
            else None
        )
        self.two = (
            Client(
                name="Devine2",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING2),
                no_updates=True,
            )
            if config.STRING2
            else None
        )
        self.three = (
            Client(
                name="Devine3",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING3),
                no_updates=True,
            )
            if config.STRING3
            else None
        )
        self.four = (
            Client(
                name="Devine4",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING4),
                no_updates=True,
            )
            if config.STRING4
            else None
        )
        self.five = (
            Client(
                name="Devine5",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=str(config.STRING5),
                no_updates=True,
            )
            if config.STRING5
            else None
        )

    async def start(self):
        LOGGER(__name__).info("Alya's Assistant starting...")

        # List of new chats to join
        new_chats = [
            "Kyrix_AnimeChat",
            "devine_support",
            "devine_updates",
            "Ongoing_kyrix",
            "Kyrix_hentai",
        ]

        # List of assistants with their respective index
        assistants_data = [
            (self.one, 1),
            (self.two, 2),
            (self.three, 3),
            (self.four, 4),
            (self.five, 5),
        ]

        for assistant, index in assistants_data:
            if assistant:
                await assistant.start()
                try:
                    for chat in new_chats:
                        await assistant.join_chat(chat)
                except Exception as e:
                    LOGGER(__name__).warning(f"Assistant {index} failed to join chats: {e}")
                assistants.append(index)
                try:
                    await assistant.send_message(
                        config.LOGGER_ID, f"Alya's Assistant {index} Started"
                    )
                except Exception as e:
                    LOGGER(__name__).error(
                        f"Assistant Account {index} failed to access the log group: {e}"
                    )
                    exit()
                me = await assistant.get_me()
                assistant.id = me.id
                assistant.name = me.mention
                assistant.username = me.username
                assistantids.append(assistant.id)
                LOGGER(__name__).info(f"Assistant {index} started as {assistant.name}")

    async def stop(self):
        LOGGER(__name__).info("Devine's assistants stopping...")
        assistants_data = [
            (self.one, 1),
            (self.two, 2),
            (self.three, 3),
            (self.four, 4),
            (self.five, 5),
        ]

        for assistant, index in assistants_data:
            if assistant:
                try:
                    await assistant.stop()
                except Exception as e:
                    LOGGER(__name__).warning(f"Assistant {index} failed to stop: {e}")
