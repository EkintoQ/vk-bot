import json
import uuid
from typing import Any, Dict

from handlers.json_handler import JSONHandler


class JSONSpamTextHandler(JSONHandler):

    def _load_data(self) -> Dict[str, Any]:
        try:
            with open(self.filename, 'r') as file:
                existing_data = json.load(file)
                if "text" not in existing_data:
                    existing_data["text"] = []
                return existing_data
        except FileNotFoundError:
            return {"text": []}
        except json.JSONDecodeError as e:
            """NEED TO CREATE ERROR HANDLER"""
            print(f"Файл JSON побился: {e}")
            return {"text": []}

    def _save_data(self, data: str):
        if not isinstance(data, str):
            print('Неверный тип данных')
            raise ValueError("Data must be a string.")

        if len(data) > 300:
            print(
                'Текст слишком длинный. Он должен быть не более 300 символов.')
            raise ValueError("Text exceeds the 300 character limit.")

        if len(data) == 0:
            print('Текст не может быть пустым.')
            raise ValueError("Text cannot be empty.")

        existing_data = self._load_data()

        new_entry = {"id": int(uuid.uuid4()), "text": data}

        existing_data["text"].append(new_entry)

        with open(self.filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
        print('Данные успешно сохранены в файле.')

    def _delete_data_by_id(self, id: str):
        existing_data = self._load_data()

        updated_texts = [
            entry for entry in existing_data["text"] if entry["id"] != id
        ]

        if len(updated_texts) == len(existing_data["text"]):
            print(f"Текст с ID {id} не найден.")
        else:
            existing_data["text"] = updated_texts
    
            with open(self.filename, 'w') as file:
                json.dump(existing_data, file, indent=4)
            print(f"Текст с ID {id} успешно удален.")

    def pretty_print_data(self):
        data = self._load_data()

        texts = data.get("text", [])

        if not texts:
            print("Нет данных для отображения.")

        for entry in texts:
            entry_id = entry.get("id")
            text_content = entry.get("text")
            print(f"ID: {entry_id}\nТекст: {text_content}\n{'-' * 15}")
