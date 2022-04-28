from pyrogram import Client as Aliciabot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from AliciaMusic.config import BOT_NAME, BOT_USERNAME, BOT_PIC, SUPPORT_CHANNEL, ASSISTANT_USERNAME, OWNER_USERNAME


@Aliciabot.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}![🤓]({BOT_PIC})
        
I am {BOT_NAME}

I can play music in your groups without any lags.
I can add your playlist and many helpful commands you can use
which can be helpful for you.
Add me to your group and don't forget to make me admin 

Use the buttons below to know more about me..
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton("Creator", url=f"https://t.me/AkHiL_SI"),                
                    InlineKeyboardButton("Commands", url=f"https://telegra.ph/MUSIC-BOT-COMMANDS-09-28")
                     ],[
                    InlineKeyboardButton("Update", url=f"https://t.me/AkiraUpdates"),
                    InlineKeyboardButton("Support ", url=f"https://t.me/TheBlue_Support"),
                    InlineKeyboardButton("➕ ADD TO YOUR GROUP ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
            ]
        ),
    )


@Aliciabot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Aliciabot, message: Message):
      await message.reply_text(f"""**{BOT_NAME} is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Creator", url=f"https://t.me/AkHiL_SI"),
                    InlineKeyboardButton("More Projects", url=f"https://t.me/TheBlueCode")
                ]
            ]
        )
   )
