from telegram.ext import(
    Updater,
    MessageHandler,
    CommandHandler,
    Filters,
    CallbackQueryHandler
)

from bot.config.settings import settings
from bot.handlers.command_handlers import command_handler
from bot.handlers.admin import admin_handler
from bot.filters.filter import CustomFilters
from bot.handlers.message_handlers import message_handler

def main() -> None:
    updater = Updater(settings.TG_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', command_handler.start_command)
    )
    dispatcher.add_handler(
        CommandHandler('add_product', callback=admin_handler.add_product_command)
    )
    dispatcher.add_handler(
        MessageHandler(filters=Filters.photo, callback=admin_handler.handle_product_message)
    )
    dispatcher.add_handler(
        MessageHandler(filters=CustomFilters.is_catalog, callback=message_handler.catalog)
    )
    dispatcher.add_handler(
        MessageHandler(filters=CustomFilters.smartphone, callback=message_handler.show_phone)
    )
    dispatcher.add_handler(
        MessageHandler(filters=CustomFilters.back, callback=message_handler.back)
    )
    dispatcher.add_handler(
        CallbackQueryHandler(message_handler.phone_callback)
    )


    updater.start_polling()
    updater.idle()
