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
            return update.effective_user.id == settings.BOT_OWNER_ID
    
    class IsCatalog(BaseFilter):
        def __call__(self, update: Update):
            msg = update.effective_message
            if not msg or not msg.text:
                return False
            return msg.text == "📦 Katalog"
    

    class IsSmartPhone(BaseFilter):
        def __call__(self, update: Update):
            msg = update.effective_message
            if not msg or not msg.text:
                return False
            return msg.text == "Smartfonlar"
    
    class IsBack(BaseFilter):
        def __call__(self, update: Update):
            msg = update.effective_message
            if not msg or not msg.text:
                return False
            return msg.text == "Orqaga"

    is_private = IsPrivate()
    is_admin = IsAdmin()
    is_catalog = IsCatalog()
    smartphone = IsSmartPhone()
    back = IsBack()

