from telegram.ext import BaseFilter, Updater
from telegram import Update, Chat
from bot.config.settings import settings


class CustomFilters:
    class IsPrivate(BaseFilter):
        def __call__(self, update: Update):
            msg = update.effective_message
            if not msg:
                return False
            return msg.chat.type == Chat.PRIVATE

    class IsAdmin(BaseFilter):
        def __call__(self, update: Update):
            return update.effective_user.id == int(settings.OWNER_ID)

    is_private = IsPrivate()
    is_admin = IsAdmin()
