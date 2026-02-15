from telegram.ext import BaseFilter
from telegram import Update, Chat

class CustomFilters:
    class IsPrivate(BaseFilter):
        def __call__(self, update: Update):
            msg = update.effective_message
            if not msg:
                return False
            return msg.chat.type == Chat.PRIVATE

    class IsAdmin(BaseFilter):
        def __call__(self, update: Update):
            user = update.effective_user
            chat = update.effective_chat
            
            if not user or not chat or chat.type == Chat.PRIVATE:
                return False
            
            admins = update.message.bot.get_chat_administrators(chat.id)
            return user.id in [admin.user.id for admin in admins]

    is_private = IsPrivate()
    is_admin = IsAdmin()

