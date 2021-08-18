#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os

from pyrogram import Client, filters
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

    )
    await bot.send_message(
        chat_id=Config.ADMIN,
        text=Presets.USER_DETAILS.format(
            info.first_name,
            info.last_name,
            info.id, info.username,
            info.is_scam,
            info.is_restricted,
            info.status,
            info.dc_id
        )
    )
