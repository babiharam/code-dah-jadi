#(Β©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>π Owner cakep : <a href='tg://user?id={OWNER_ID}'>klik sayang</a>\n</code>\nπ Libary : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\nπ Tutor buat bot : <a href='https://t.me/tutorfiletolink'>klik sayang</a>\nπ Channel asupan : <a href='https://t.me/joinchat/Ac_aQdyZAZdlOGRh'>asupan disini syg</a>\nπ Info channel : <a href='https://t.me/joinchat/XzdlJ6oU6iNjZWYx'>klik sayang</a>\nπJoin VIP: https://t.me/joinvipmurah</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("β Keluar", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
