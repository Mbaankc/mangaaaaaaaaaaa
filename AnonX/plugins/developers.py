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

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطور مانجا","المطورين","مطورين","مطورين مانجا"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/f0e558c18bc3188fb7030.jpg",
        caption=f"""**⩹━★⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين مانجا ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙼𝙰𝙽𝙶𝙰⌯►", url=f"https://t.me/zmngaz"), 
                 ],[
                    InlineKeyboardButton(
                        "𝙱𝙰𝚁", url=f"https://t.me/C_A_G1"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ ՏøuƦcε ʍαπĝα ⌝⚡", url=f"https://t.me/SOURCEMANGA"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مانجا انجم","مانجا","منقا","مبرمج","MANGA","manga" ,"المطور مانجا"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("zmngaz")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["منقا"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("zmngaz")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["بوت حذف"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("zaggaz4_bot")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**يلا غور احذف يعم دانت بارد😂**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["مساعدة"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/f0e558c18bc3188fb7030.jpg",
        caption=f"""**⩹⊷━⌞ ՏøuƦcε ʍαπĝα ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس مانجا\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ ՏøuƦcε ʍαπĝα ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙼𝙰𝙽𝙶𝙰ِ⌯‹", url=f"https://t.me/zmngaz"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ ՏøuƦcε ʍαπĝα ⌝⚡", url=f"https://t.me/SOURCEMANGA"),
                ],

            ]

        ),

    )



    