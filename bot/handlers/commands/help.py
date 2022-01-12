from aiogram import types


async def cmd_help(message: types.Message):
    await message.answer("Чем тебе помочь?")
