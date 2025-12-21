#imports
import bot_ext.keyboards as kb
import tools

#aiogram imports
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, message
from aiogram import F



#router
router = Router()

#/start
@router.message(CommandStart())
async def main_menu(message: Message):
    await message.answer(text="main menu", reply_markup=kb.main_menu_keyboard)

#/status
@router.message(F.text == "📊 Status")  # Точно как текст кнопки!
async def status_handler(message: Message):
    ping_results = tools.ping_hosts()
    status_text = ""
    for host, is_online in ping_results.items():
        status_emoji = "🟢 ONLINE" if is_online else "🔴 OFFLINE"
        status_text += f"• `{host}`: {status_emoji}\n"
    await message.answer(status_text, reply_markup=kb.main_menu_keyboard, parse_mode="Markdown")