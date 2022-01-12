from aiogram import types


async def cmd_start(message: types.Message):
    await message.answer(
        f"💫Доброго времени суток, {message.from_user.first_name}!"
    )
