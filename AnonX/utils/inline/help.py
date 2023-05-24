from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌹Aᴅᴅ ᴍᴇ🌹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌹Hᴇʟᴘ🌹",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🌹Sᴇᴛᴛɪɴɢs🌹", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Gʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🪄 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs 🪄", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💬 Assᴏᴄɪᴀᴛɪᴏɴ", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🪛 Uᴘᴅᴀᴛᴇs", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url=config.SUPPORT_GROUP                
            )
        ],
     ]
    return buttons
