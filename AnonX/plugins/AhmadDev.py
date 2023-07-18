# telegram: @bbnnQ ~ My channel: @ccooR حقوق.
import os
import random
import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import (Message,
InlineKeyboardMarkup,InlineKeyboardButton)
from typing import Union
from AnonX import app




def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "contact",
            "dice",
            "poll",
            "location",
            "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj



@app.on_message(
    command(["المطور","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message, OWNER: Union[bool, int] = None):
    usr = await client.get_users(6201061981)
    name = usr.first_name
    bio = (await client.get_chat(6201061981)).bio
    async for photo in client.iter_profile_photos(6201061981, limit=1):
                    await message.reply_photo(photo.file_id,   caption=f"- 𝙳𝚎𝚟: @bbnnQ\n- 𝙱𝚒𝚘: {bio}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, user_id=6201061981)
                ],
            ]
        ),
    )
@app.on_message(command("ايما"))
async def bottttt(client, message):
    selections = ["عمرها لأيما", 
"يا قلب ايما",
"صرعت راسها لأيما",
"لك نعم يا عيوني",
"تؤبرني معك",
"تفضل عن أسمع واللهي نصرعت",]
    bar = random.choice(selections)
    await message.reply_text(bar)
    
@app.on_message(command("بحبك"))
async def bottttt(client, message):
    selections = ["يخليلي قلبك", 
"بحبك اكتر على فكرة!",
"بتنفسك",
"ياعمري انااااا",
"تفضل واطلب ايدي من @bbnnQ",
"لا اله الا الله وانا بحبك",]
    bar = random.choice(selections)
    await message.reply_text(bar)

@app.on_message(command("الاوامر"))
async def ahmad(client: Client, message: Message):
    await message.reply_text(f"""**اليك أوامر بوت ايما**:

‹: تشغيل - لتشغيل أغنية 🎵
‹: تخطي - لتخطي الأغنية 🎵
‹: انهاء - لانهاء تشغيل الاغنية 🎵
‹: كت - لبدأ لعبة الكت تويت ❤️
‹: صراحة - لبدأ لعبة الصراحه ❤️
‹: لو خيروك - لبدأ لعبة لو خيروك ❤️
‹: حروف - لبدأ لعبة الحروف ❤️
‹: ميديا - بالرد على صورة ❤️""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("‹ اضافة الى مجموعة ›", url=f"https://t.me/EmCaMusicBot?startgroup=true"),
            ],
            ]
        ),
    )
