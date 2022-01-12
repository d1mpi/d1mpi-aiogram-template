from aiogram import Router
from aiogram.dispatcher.filters import Command

from bot.handlers.commands.help import cmd_help
from bot.handlers.commands.start import cmd_start


def register_commands_handler(router: Router):
    router.message.register(cmd_start, Command(commands="start"), chat_type="private")
    router.message.register(cmd_help, Command(commands="help"), chat_type="private")
