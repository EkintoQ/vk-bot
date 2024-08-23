from vkbottle.user import Message, User

from handlers.auth_handler import get_token


class Bot:

    def __init__(self, config):
        self.config = config
        self.token = None

    async def start_bot(self):
        self.token = get_token()

        bot = User(token=self.token)

        def extract_title(message: Message):
            for attachment in message.attachments:
                if attachment.video:
                    return attachment.video.title
            return None

        @bot.on.chat_message(text="да")
        async def hi_handler(message: Message):
            await message.answer("пизда")

        @bot.on.chat_message()
        async def circle_handle(message: Message):
            title = extract_title(message)
            if title == "Видеосообщение от @tomato_avtomato":
                print('wtf')
                if message.from_id == self.config.get_user_id('krica_id'):
                    print('wtf2')
                    await message.answer("@idmaknau НОВЫЙ КРУЖОК")

        @bot.on.chat_message(text="спам")
        async def spam_handler(message: Message):
            await message.answer("так точно sir")

        await bot.run_polling()
