from telegram import (Update, InputMediaPhoto,
                      ReplyKeyboardMarkup, KeyboardButton,
                      InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import CallbackContext
from bot.utils.formatters import get_smartphone_caption
from bot.models.smartphones import smartphones

class MessageHandler:

    def catalog(self, update: Update, context: CallbackContext):
        keyboard = [
            [KeyboardButton("Smartfonlar")],
            [KeyboardButton("Aksesuarlar")],
            [KeyboardButton("Orqaga")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
        update.message.reply_text(text='📦 Katalog', reply_markup=reply_markup)
    
    def back(self, update: Update, context: CallbackContext):
        keyboard = [
            [KeyboardButton("📦 Katalog"), KeyboardButton("🔥 Chegirmalar")],
            [KeyboardButton("📞 Bog'lanish ")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("Bosh Menu", reply_markup=reply_markup)
    
    def show_phone(self, update: Update, context: CallbackContext, index=0):
        phone = smartphones[index]
        caption = get_smartphone_caption(phone)

        keyboard = [
            [
                InlineKeyboardButton("⬅ Orqaga", callback_data=f"prev_{index}"),
                InlineKeyboardButton("Sotib olish 🛒", callback_data=f"buy_{index}"),
                InlineKeyboardButton("Keyingisi ➡", callback_data=f"next_{index}")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_photo(
            photo=phone.photo,
            caption=caption,
            reply_markup=reply_markup
        )
    
    def phone_callback(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        data = query.data
        action, index_str = data.split("_")
        index = int(index_str)

        new_index = index
        if action == "prev" and index > 0:
            new_index = index - 1
        elif action == "next" and index < len(smartphones) - 1:
            new_index = index + 1
        elif action == "buy":
            query.edit_message_caption(f"Siz {smartphones[index].name} ni xarid qildingiz 🛒")
            return
        
        if new_index == index:
            query.answer("O'tkazib bo'lmaydi", show_alert=True)
            return

        phone = smartphones[new_index]
        caption = get_smartphone_caption(phone)

        keyboard = [
            [
                InlineKeyboardButton("⬅ Orqaga", callback_data=f"prev_{new_index}"),
                InlineKeyboardButton("Sotib olish 🛒", callback_data=f"buy_{new_index}"),
                InlineKeyboardButton("Keyingisi ➡", callback_data=f"next_{new_index}")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        media = InputMediaPhoto(media=phone.photo, caption=caption)
        query.edit_message_media(media=media, reply_markup=reply_markup)


message_handler = MessageHandler()
