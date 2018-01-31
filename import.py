import argparse
import csv
import requests
import json
import urllib.parse


def str_to_bool(value):
    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        return value


def import_users(f_obj, address, apikey):
    reader = csv.DictReader(f_obj, delimiter=";")
    headers = {'X-Redmine-API-Key': apikey, 'Content-type': 'application/json'}
    i = 1
    for line in reader:
        print("Импорт строки ", i)
        i = i + 1
        new_user = {}
        for key, value in line.items():
            if value:
                print(key, str_to_bool(value))
                new_user[str(key)] = str_to_bool(value)
        data = {'user': new_user, 'send_information': True}
        data_json = json.dumps(data)
        response = requests.post(urllib.parse.urljoin(address, 'users.json'), data_json, headers=headers)
        if response.status_code == 201:
            print("Импортирован пользователь ", new_user['firstname'], new_user['lastname'])
        else:
            print("Ошибка при импорте ", response.status_code, response.content.decode("UTF-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-address", action="store")
    parser.add_argument("-apikey", action="store")
    parser.add_argument("-filename", action="store")

    args = parser.parse_args()
    if args.filename:
        with open(args.filename, "r") as f_obj:
            import_users(f_obj, address=args.address, apikey=args.apikey)
