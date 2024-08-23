from vkbottle import API

from handlers.auth_handler import get_token
from handlers.json_group_handler import (
    load_group_data,
    remove_group_data,
    save_group_data,
)
from handlers.json_spamtexthandler import JSONSpamTextHandler
from handlers.json_spamphotohandler import JSONSpamPhotoHandler


class Api:

  def __init__(self, config):
    self.config = config
    self.token = get_token()
    self.api = API(token=self.token)

  async def activate_wall_posting(self):
    await self.api.wall.post(
        owner_id=-192897459,
        message='Привет!',
        attachments=[
            'photo327938093_457252003'
        ])

  async def get_group_info(self):
    group_link = str(input(self.config.get_message('input_group')))
    group = await self.api.groups.get_by_id(group_id=group_link)
    group_data = {'id': -group[0].id, 'name': group[0].name}
    save_group_data(group_data)

  def retrieve_group_data(self):
    load_group_data()

  def delete_group_data(self):
    group_id = int(input("Введите ID группы для удаления:"))
    remove_group_data(group_id)

  def get_text(self):
    JSONSpamTextHandler('spam.json').pretty_print_data()

  def save_text(self):
    text = str(input("Введите текст для спама:"))
    JSONSpamTextHandler('spam.json')._save_data(text)

  def delete_text(self):
    id = int(input("Введите ID текста для удаления:"))
    JSONSpamTextHandler('spam.json')._delete_data_by_id(id)

  def get_photo(self):
    JSONSpamPhotoHandler('spam.json').pretty_print_data()

  def save_photo(self):
    text = str(input("Введите фото для спама:"))
    JSONSpamPhotoHandler('spam.json')._save_data(text)

  def delete_photo(self):
    id = str(input("Введите ID фото для удаления:"))
    JSONSpamPhotoHandler('spam.json')._delete_data_by_id(id)


  async def start_menu(self):

    while True:
      try:
        print("-------------------------")
        command = int(input(self.config.get_message('api_prompt')))
        match command:
          case 1:
            print("-------------------------")
            await self.get_group_info()
          case 2:
            print("-------------------------")
            self.delete_group_data()
          case 3:
            print("-------------------------")
            self.retrieve_group_data()
          case 4:
            print("-------------------------")
            self.save_text()
          case 5:
            print("-------------------------")
            self.delete_text()
          case 6:
            print("-------------------------")
            self.get_text()
          case 7:
            print("-------------------------")
            self.save_photo()
          case 8:
            print("-------------------------")
            self.delete_photo()
          case 9:
            print("-------------------------")
            self.get_photo()
          case 10:
            print("-------------------------")
            await self.activate_wall_posting()
          case _:
            print("-------------------------")
            print(self.config.get_message('invalid_command'))
      except ValueError:
        print("-------------------------")
        print(self.config.get_message('value_error'))
