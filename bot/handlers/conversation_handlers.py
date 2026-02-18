from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
)
from telegram.ext import CallbackContext, ConversationHandler
from bot.config.constants import AddProductStates
from bot.database.db import product


class AddProduct:
    def add_product_start(self, update: Update, context: CallbackContext):
        context.user_data.clear()
        update.message.reply_text(
            "📦 Mahsulot nomini kiriting (bekor qilish uchun /cancel bosing):"
        )
        return AddProductStates.SET_NAME

    def set_name(self, update: Update, context: CallbackContext):
        name = update.message.text.strip()

        if len(name) < 2:
            update.message.reply_text(
                "❗ Nom juda qisqa. Qayta kiriting (bekor qilish uchun /cancel bosing):"
            )
            return AddProductStates.SET_NAME

        context.user_data["name"] = name
        update.message.reply_text("💰 Narxni kiriting (faqat son):")
        return AddProductStates.SET_PRICE

    def set_price(self, update: Update, context: CallbackContext):
        text = update.message.text.strip()

        if not text.isdigit():
            update.message.reply_text("❗ Narx son bo'lishi kerak:")
            return AddProductStates.SET_PRICE

        context.user_data["price"] = int(text)
        update.message.reply_text(
            "📝 Tavsif kiriting (bekor qilish uchun /cancel bosing):"
        )
        return AddProductStates.SET_DESCRIPTION

    def set_description(self, update: Update, context: CallbackContext):
        context.user_data["description"] = update.message.text.strip()
        update.message.reply_text(
            "🏷 Brand nomini kiriting (bekor qilish uchun /cancel bosing):"
        )
        return AddProductStates.SET_BRAND

    def set_brand(self, update: Update, context: CallbackContext):
        context.user_data["brand"] = update.message.text.strip()

        memory_keyboard = ReplyKeyboardMarkup(
            [
                [KeyboardButton("64GB"), KeyboardButton("128GB")],
                [KeyboardButton("256GB"), KeyboardButton("512GB")],
            ],
            resize_keyboard=True,
        )

        update.message.reply_text(
            "💾 Xotira tanlang (bekor qilish uchun /cancel bosing):",
            reply_markup=memory_keyboard,
        )

        return AddProductStates.SET_MEMORY

    def set_memory(self, update: Update, context: CallbackContext):
        context.user_data["memory"] = update.message.text.strip()
        update.message.reply_text(
            "🎨 Rangini kiriting (bekor qilish uchun /cancel bosing):",
            reply_markup=ReplyKeyboardRemove(),
        )
        return AddProductStates.SET_COLOR

    def set_color(self, update: Update, context: CallbackContext):
        context.user_data["color"] = update.message.text.strip()
        update.message.reply_text("📉 Chegirma foizini kiriting (faqat son):")
        return AddProductStates.SET_DISCOUNT

    def set_discount(self, update: Update, context: CallbackContext):
        text = update.message.text.strip()

        if not text.isdigit():
            update.message.reply_text("❗ Chegirma son bo'lishi kerak:")
            return AddProductStates.SET_DISCOUNT

        context.user_data["discount"] = int(text)

        update.message.reply_text(
            "Product rasmini yuboring (bekor qilish uchun /cancel bosing):"
        )

        return AddProductStates.SET_PHOTO

    def set_photo(self, update: Update, context: CallbackContext):
        if not update.message.photo:
            update.message.reply_text("❗ Iltimos, rasm yuboring:")
            return AddProductStates.SET_PHOTO

        photo = update.message.photo[-1].file_id

        context.user_data["photo"] = photo
        data = context.user_data

        keyboard = [
            [
                InlineKeyboardButton("✅ Xa", callback_data="confirm"),
                InlineKeyboardButton("❌ Yuq", callback_data="cancel"),
            ]
        ]

        update.message.reply_photo(
            photo=photo,
            caption=(
                f"📦 Mahsulot ma'lumotlari:\n\n"
                f"Nom: {data['name']}\n"
                f"Narx: {data['price']}\n"
                f"Tavsif: {data['description']}\n"
                f"Brand: {data['brand']}\n"
                f"Xotira: {data['memory']}\n"
                f"Rang: {data['color']}\n"
                f"Chegirma: {data['discount']}%"
            ),
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

        return AddProductStates.CONFIRM

    def confirm_product(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()

        if query.data == "cancel":
            query.edit_message_caption("❌ Mahsulot qo'shish bekor qilindi.")
            context.user_data.clear()
            return ConversationHandler.END

        product_data = context.user_data
        product.save_product(product_data)
        print("SAVE PRODUCT:", product_data)

        query.edit_message_caption("✅ Mahsulot muvaffaqiyatli saqlandi.")

        context.user_data.clear()
        return ConversationHandler.END

    def cancel(self, update: Update, context: CallbackContext):
        update.message.reply_text(
            "❌ Jarayon bekor qilindi.", reply_markup=ReplyKeyboardRemove()
        )
        context.user_data.clear()
        return ConversationHandler.END


add_product = AddProduct()
