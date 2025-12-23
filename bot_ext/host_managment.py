#imports
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup

#router
router = Router()

#add host
class Add(StatesGroup):
    name = State()
    ip = State()
    port = State()

@router.message_handler(commands=["addhost"])
async def add_host(message: types.Message, state: FSMContext):
    await message.answer("Entering host name")