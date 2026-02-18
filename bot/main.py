from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters,
    CallbackQueryHandler,
    ConversationHandler,
)

from bot.config.settings import settings
from bot.handlers.command_handlers import command_handler
from bot.filters.filter import CustomFilters
from bot.handlers.message_handlers import message_handler
from bot.config.constants import AddProductStates
from bot.handlers.conversation_handlers import add_product


def main() -> None:
    updater = Updater(settings.TG_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", command_handler.start_command))
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler(
                "add_product",
                add_product.add_product_start,
                filters=CustomFilters.is_admin,
            )
        ],
        states={
            AddProductStates.SET_NAME: [
                MessageHandler(Filters.text & ~Filters.command, add_product.set_name)
            ],
            AddProductStates.SET_PRICE: [
                MessageHandler(Filters.text & ~Filters.command, add_product.set_price)
            ],
            AddProductStates.SET_DESCRIPTION: [
                MessageHandler(
                    Filters.text & ~Filters.command, add_product.set_description
                )
            ],
            AddProductStates.SET_BRAND: [
                MessageHandler(Filters.text & ~Filters.command, add_product.set_brand)
            ],
            AddProductStates.SET_MEMORY: [
                MessageHandler(Filters.text & ~Filters.command, add_product.set_memory)
            ],
            AddProductStates.SET_COLOR: [
                MessageHandler(Filters.text & ~Filters.command, add_product.set_color)
            ],
            AddProductStates.SET_DISCOUNT: [
                MessageHandler(
                    Filters.text & ~Filters.command, add_product.set_discount
                )
            ],
            AddProductStates.SET_PHOTO: [
                MessageHandler(Filters.photo, add_product.set_photo)
            ],
            AddProductStates.CONFIRM: [
                CallbackQueryHandler(add_product.confirm_product)
            ],
        },
        fallbacks=[CommandHandler("cancel", add_product.cancel)],
    )

    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(
        MessageHandler(
            filters=Filters.text("📦 Katalog"), callback=message_handler.catalog
        )
    )
    dispatcher.add_handler(
        MessageHandler(
            filters=Filters.text("Smartfonlar"), callback=message_handler.show_phone
        )
    )
    dispatcher.add_handler(
        MessageHandler(filters=Filters.text("Orqaga"), callback=message_handler.back)
    )
    dispatcher.add_handler(CallbackQueryHandler(message_handler.phone_callback))

    updater.start_polling()
    updater.idle()
