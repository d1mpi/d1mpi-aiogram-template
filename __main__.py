import asyncio

from aiogram import Router, Bot, Dispatcher
from aiogram.types import BotCommand

from bot.filters.chat_type import ChatTypeFilter
from bot.handlers.commands import register_commands_handler
from bot.handlers.error_message import register_error_message
from bot.utils.config_reader import config
from bot.utils.database.postgres import DataBase
from bot.utils.localization import Lang
from bot.utils.logger import logger


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start this bot"),
        BotCommand(command="help", description="Help me please"),
    ]
    await bot.set_my_commands(commands)


async def main():
    default_router = Router()

    bot = Bot(token=config.token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(default_router)

    try:
        lang = Lang(config.lang)
    except ValueError:
        print(f"Error no localization found for language code: {config.lang}")
        return

    logger.info("Starting bot")

    # Фильтр chat_type
    default_router.message.bind_filter(ChatTypeFilter)

    # Регистрируем команды
    register_commands_handler(default_router)

    # Ловим неизвестные сообщения, всегда в конец.
    register_error_message(default_router)

    await set_bot_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(),
                           config=config, lang=lang)


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()

        loop.run_until_complete(DataBase.create_pool())
        loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
