class AddProductStates:
    SET_NAME = 0
    SET_PRICE = 1
    SET_PHOTO = 2
    SET_DESCRIPTION = 3
    SET_BRAND = 4
    SET_MEMORY = 5
    SET_COLOR = 6
    SET_DISCOUNT = 7
    SET_PHOTO = 8
    CONFIRM = 9


start_msg = """
<b>📱 Phone Market Bot'ga xush kelibsiz!</b>

Siz bu yerda eng so‘nggi smartfonlar, aksessuarlar va maxsus chegirmalarni topishingiz mumkin 🚀

<b>🔎 Bizda mavjud:</b>
• 📲 Eng yangi smartfon modellari  
• 🎧 Aksessuarlar (naushnik, powerbank va boshqalar)  
• 💰 Maxsus chegirmalar  

<b>Quyidagilardan birini tanlang:</b>

📦 <b>Katalog</b> – Mahsulotlarni ko‘rish  
🔥 <b>Chegirmalar</b> – Aksiyalar  
📞 <b>Bog‘lanish</b> – Operator bilan aloqa  
"""

smartphone_message = """
📱 {name}
💰 Narxi: ${price}
📝 Tavsifi: {description}
🏷️ Brand: {brand}
💾 Memory: {memory}
🎨 Rang: {color}
🔥 Chegirma: {discount}%
"""
