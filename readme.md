# Импорт пользователей в Redmine

Импортирует список пользователей из csv файла в redmine.
Каждому пользователю отправляется на почту информация по учетной записи.

## Установка

* Установить python 3.6
* Скачать или клонировать репозиторий
* В каталоге выполнить команду
 
```
    pip install -r requirements.txt
```
## Использование

В каталоге выполнить команду

```
python import.py -address [ADDRESS] -apikey [APIKEY] -filename [FILENAME]
```
где
* ADDRESS - адрес redmine, например http://127.0.0.1
* APIKEY - ключ доступа к API из профиля пользователя
* FILENAME - csv файл со списком пользователей


## Формат csv файла

* login (string) – (required). User login.
* password (string) – (optional). User password.
* firstname (string) – (required). User name.
* lastname (string) – (required). User surname.
* mail (string) – (required). User email.
* auth_source_id (int) – (optional). Authentication mode id.
* mail_notification (string) – (optional). Type of mail notification, one of:
    * all
    * selected
    * only_my_events
    * only_assigned
    * only_owner
    * none
* notified_project_ids (list) – (optional). Project IDs for a “selected” mail notification type.
* must_change_passwd (bool) – (optional). Whether user must change password.
* generate_password (bool) – (optional). Whether to generate password for the user.
* custom_fields (list) – (optional). Custom fields as [{‘id’: 1, ‘value’: ‘foo’}].