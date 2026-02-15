from telegram.ext import(
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)

from bot.config.settings import settings
from bot.handlers.command_handlers import command_handler
from bot.handlers.admin import admin_handler
from bot.filters.filter import CustomFilters

def main() -> None:
    updater = Updater(settings.TG_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', command_handler.start_command)
    )
    dispatcher.add_handler(
        CommandHandler('add_product', callback=admin_handler.add_product_command, filters=Filters.command)
    )
    dispatcher.add_handler(
        MessageHandler(filters=Filters.photo, callback=admin_handler.handle_product_message)
    )

    updater.start_polling()
    updater.idle()
