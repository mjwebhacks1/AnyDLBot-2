# (c) @PredatorHackerzZ

import asyncio
from sample_config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, cmd: Message):
    return 200
