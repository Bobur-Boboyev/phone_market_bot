from telegram import Update
from telegram.ext import CallbackContext
from bot.config.constants import example_text
from bot.utils.product_parser import utils
from bot.services.product_service import ProductService


class AdminHandler:
    def add_product_command(self, update: Update, context: CallbackContext):
        update.message.reply_html(example_text)

    def handle_product_message(self, update: Update, context: CallbackContext):
        if not update.message.photo:
            return 
        
        caption = update.message.caption

        if not caption:
            update.message.reply_text("Caption bo‘sh.")
            return
        
        data = utils.parse_product_caption(caption)
        is_valid, error = utils.validate_product_data(data)

        if not is_valid:
            update.message.reply_text(f"❌ {error}")
            return
        
        data["photo"] = update.message.photo[-1].file_id

        ProductService.create_product(data)

        update.message.reply_text("✅ Mahsulot saqlandi.")

admin_handler = AdminHandler()