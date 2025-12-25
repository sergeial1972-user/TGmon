#imports
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.filters import Command, CommandObject
import hostmanager


#router
router = Router()

#add host
class AddHost(StatesGroup):
    name = State()
    ip = State()
    port = State()

#hostmanager
manager = hostmanager.Manager()

#add host
@router.message(Command("addhost"))
async def add_host(message: types.Message, state: FSMContext):
    await message.answer("Enter host name")
    await state.set_state(AddHost.name)

@router.message(AddHost.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()

    await state.update_data(name=name)
    await message.answer("Enter ip")
    await state.set_state(AddHost.ip)

@router.message(AddHost.ip)
async def process_ip(message: types.Message, state: FSMContext):
    ip = message.text.strip()
    await state.update_data(ip=ip)
    await message.answer("Enter port:")
    await state.set_state(AddHost.port)

@router.message(AddHost.port)
async def process_port(message: types.Message, state: FSMContext):
    port = message.text.strip()
    await state.update_data(port=port)

    #result
    data = await state.get_data()
    name = data['name']
    ip = data['ip']
    port = data['port']

    """adding host via hostmanager"""
    manager.add_host(name=name, ip=ip, port=port)

    await state.clear()


"""removing host via hostmanager (args)"""


@router.message(Command("rmhost"))
async def remove_host(message: types.Message, command: CommandObject, state: FSMContext):
    args = command.args

    if not args or not args.strip():
        await message.answer("enter host name as argument")
        return

    hostname = args.strip()

    try:
        manager.remove_host(hostname)
        await message.answer(f"✅ `{hostname}` Deleted", parse_mode="Markdown")
    except Exception as e:
        await message.answer(f"❌ {e}", parse_mode="Markdown")
