from aiogram import Router, types

from bot.utils.logger import logger


async def error_message_handler(message: types.Message):
    try:
        await message.delete()
    except Exception as err:
        logger.error(err)

    await message.answer("⚠Пожалуйста, выберите пункт из меню.")


def register_error_message(router: Router):
    router.message.register(error_message_handler, chat_type="private")
