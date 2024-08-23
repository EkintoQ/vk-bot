import json


class ConfigLoader:

    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_message(self, key: str) -> str:
        return self.config['messages'].get(key)

    def get_user_id(self, key: str) -> int:
        return self.config['user_id'].get(key)
