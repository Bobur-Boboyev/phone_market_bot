from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from bot.config.constants import start_msg

class CommandHandlers:

    def start_command(self, update: Update, context: CallbackContext):
        keyboard = [
            [KeyboardButton("📦 Katalog"), KeyboardButton("🔥 Chegirmalar")],
            [KeyboardButton("📞 Bog'lanish ")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_html(start_msg, reply_markup=reply_markup)

command_handler = CommandHandlers()