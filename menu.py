from handlers.auth_handler import save_token, save_token_via_credentials


class Menu:

    def __init__(self, config):
        self.config = config

    async def input_credentials(self):
        login = input(self.config.get_message('input_login'))
        password = input(self.config.get_message('input_password'))
        await save_token_via_credentials(login, password)

    def input_token(self):
        token = input(self.config.get_message('input_token'))
        save_token(token)

    def exit_program(self):
        print(self.config.get_message('finish'))
        exit(0)

    async def handle_commands(self) -> int:
        while True:
            try:
                command = int(input(self.config.get_message('command_prompt')))
                match command:
                    case 1:
                        await self.input_credentials()
                    case 2:
                        self.input_token()
                    case 3:
                        return 1
                    case 4:
                        return 2
                    case 0:
                        self.exit_program()
                    case _:
                        print(self.config.get_message('invalid_command'))
            except ValueError:
                print(self.config.get_message('value_error'))
