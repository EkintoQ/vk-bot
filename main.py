import asyncio

from api import Api
from bot import Bot
from config_loader import ConfigLoader
from menu import Menu


def main():
    config = ConfigLoader('config.json')
    menu = Menu(config)
    choice = asyncio.run(menu.handle_commands())
    if choice == 1:
        bot = Bot(config)
        asyncio.run(bot.start_bot())
    elif choice == 2:
        api = Api(config)
        asyncio.run(api.start_menu())


if __name__ == "__main__":
    main()
