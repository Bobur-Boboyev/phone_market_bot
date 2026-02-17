from bot.config.constants import smartphone_message

def get_smartphone_caption(phone):
    return smartphone_message.format(
        name=phone.name,
        price=phone.price,
        description=phone.description,
        brand=phone.brand,
        memory=phone.memory,
        color=phone.color,
        discount=phone.discount
    )