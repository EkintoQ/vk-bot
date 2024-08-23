import json
import os


def save_group_data(group_data, filename='groups.json'):
    existing_data = []

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                print("-------------------------")
                print(f'Произошёл баг JSON в файле {filename}.')

    if not isinstance(existing_data, list):
        existing_data = []

    for item in existing_data:
        if item['id'] == group_data['id']:
            print("-------------------------")
            print(f"Группа с данным ID {group_data['id']}")
            print(f"и именем {group_data['name']} уже существует.")
            break
    else:
        print("-------------------------")
        print(f"Добавление группы с ID {group_data['id']}")
        print(f"и именем {group_data['name']}")
        existing_data.append(group_data)

        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print("-------------------------")
        print(f"Группы обновлены в {filename}.")


def load_group_data(filename='groups.json'):
    try:
        with open(filename, 'r') as f:
            group_data = json.load(f)
            if group_data:
                print("-------------------------")
                print("Данные для групп:")
                for group in group_data:
                    print("-------------------------")
                    print(f"Группа ID: {group['id']}")
                    print(f"Группа название: {group['name']}")
            else:
                print("-------------------------")
                print("Ни одна группа ещё не добавлена")
    except FileNotFoundError:
        print("-------------------------")
        print(f"Файл '{filename}' не найден.")


def remove_group_data(group_id, filename='groups.json'):
    try:
        with open(filename, 'r') as f:
            existing_data = json.load(f)

        updated_data = [group for group in existing_data if group['id'] != group_id]

        if len(updated_data) == len(existing_data):
            print("-------------------------")
            print("Группы с таким ID нет в файле.")
        else:
            with open(filename, 'w') as f:
                json.dump(updated_data, f, indent=4)
            print("-------------------------")
            print(f"Группа с данным ID {group_id} была удалена.")

    except FileNotFoundError:
        print("-------------------------")
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print("-------------------------")
        print(f"Произошёл баг JSON в файле {filename}.")