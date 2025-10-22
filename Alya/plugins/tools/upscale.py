from lexica import Client as LexicaClient
from pyrogram import filters
from pyrogram.types import Message
import os
from Alya import app

async def getFile(message: Message):
    if not message.reply_to_message:
        return None

    if message.reply_to_message.photo:
        return await message.reply_to_message.download()

    if message.reply_to_message.document and message.reply_to_message.document.mime_type in ['image/png', 'image/jpg', 'image/jpeg']:
        return await message.reply_to_message.download()

    return None

async def UpscaleImages(image_path: str) -> str:
    try:
        client = LexicaClient()
        
        if not hasattr(client, "upscale"):
            raise NotImplementedError("LexicaClient does not support upscaling.")
        
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        content = client.upscale(image_bytes)
        
        upscaled_file_path = "upscaled.png"
        with open(upscaled_file_path, "wb") as output_file:
            output_file.write(content)

        return upscaled_file_path

    except Exception as e:
        raise Exception(f"Failed to upscale the image: {e}")

@app.on_message(filters.command("upscale"))
async def upscaleImages(_, message):
    file_path = await getFile(message)
    if file_path is None:
        return await message.reply_text("Reply to an image.")

    msg = await message.reply("Upscaling...")

    try:
        upscaled_image = await UpscaleImages(file_path)
        
        await message.reply_document(upscaled_image)

        os.remove(file_path)
        os.remove(upscaled_image)

        await msg.delete()
    except Exception as e:
        await msg.edit(f"Failed to upscale the image: {e}")
