from telegram.ext import(
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from config.settings import settings
from handlers.command_handlers import start_command

def main() -> None:
    updater = Updater(settings.TG_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start_command)
    )
    updater.start_polling()
    updater.idle()

