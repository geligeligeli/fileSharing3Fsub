#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    user = query.from_user  # Get the user who initiated the interaction
    
    if data == "about":
        await query.message.edit_text(
            text = (
                f"<b>○ Creator : </b>Bot Father\n"
                f"<b>○ My best Friend : </b><a href='tg://user?id={user.id}'>{user.first_name}</a>\n\n"
                f"○ I may be a bot, but I can still be your best digital friend!\n\n"
                f"<b>○ Fun Fact : </b>If you click 'Close', I will disappear like a magician's trick! 🎩✨\n"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Close", callback_data="close")
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