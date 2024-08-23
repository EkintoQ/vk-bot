import json
from typing import Any, Dict

from handlers.json_handler import JSONHandler


class JSONSpamPhotoHandler(JSONHandler):

    def _load_data(self) -> Dict[str, Any]:
        try:
            with open(self.filename, 'r') as file:
                existing_data = json.load(file)
                if "photo" not in existing_data:
                    existing_data["photo"] = []
                return existing_data
        except FileNotFoundError:
            return {"photo": []}
        except json.JSONDecodeError as e:
            """NEED TO CREATE ERROR HANDLER"""
            print(f"Файл JSON побился: {e}")
            return {"photo": []}

    def _save_data(self, data: str):
        if not isinstance(data, str):
            print('Неверный тип данных')
            raise ValueError("Data must be a string.")

        if len(data) == 0:
            print('ID фото не может быть пустым.')
            raise ValueError("ID cannot be empty.")

        existing_data = self._load_data()

        new_entry = {"id": data}

        existing_data["photo"].append(new_entry)

        with open(self.filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
        print('Данные успешно сохранены в файле.')

    def _delete_data_by_id(self, id: int):
        existing_data = self._load_data()

        updated_texts = [
            entry for entry in existing_data["photo"] if entry["id"] != id
        ]

        if len(updated_texts) == len(existing_data["photo"]):
            print(f"Фото с ID {id} не найден.")
        else:
            existing_data["photo"] = updated_texts

            with open(self.filename, 'w') as file:
                json.dump(existing_data, file, indent=4)
            print(f"Фото с ID {id} успешно удален.")

    def pretty_print_data(self):
        data = self._load_data()

        photos = data.get("photo", [])

        if not photos:
            print("Нет данных для отображения.")

        for entry in photos:
            entry_id = entry.get("id")
            print(f"ID: {entry_id}\n{'-' * 15}")
