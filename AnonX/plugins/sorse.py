
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/f0e558c18bc3188fb7030.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ ՏøuƦcε ʍαπĝα ⌝](https://t.me/SOURCEMANGA)⧽⌯⊶★═╮\n★‹ [⌞ ՏøuƦcε ʍαπĝα ](https://t.me/SOURCEMANGA)\n★‹ [𝙱𝙰𝚁](https://t.me/C_A_G1)\n★‹ [𝙼𝙰𝙽𝙶𝙰](https://t.me/zmngaz)\n★‹ [ρ᥆kᥱꪔ᥆ꪀ](https://t.me/devpokemon)\n╰═★⊷⌯⧼[⌞ ՏøuƦcε ʍαπĝα ⌝](https://t.me/SOURCEMANGA)⧽⌯⊶★═╯\n ⍟ Welcome to source Avatar""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙼𝙰𝙽𝙶𝙰►", url=f"https://t.me/zmngaz"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ ՏøuƦcε ʍαπĝα ⌝⚡️", url=f"https://t.me/SOURCEMANGA"),
                ],[
                    InlineKeyboardButton(
                        "MANGA", url=f"https://t.me/DEVTOM_bot?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تم اختيار اغنيه لك من سورس مانجا",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



