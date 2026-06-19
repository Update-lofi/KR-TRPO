import json
import os

FILE_NAME = 'contacts.json'

def load_contacts():
    """Загружает контакты из JSON-файла."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    """Сохраняет контакты в JSON-файл."""
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def add_contact():
    """Добавляет новый контакт."""
    # TODO: запросить имя, телефон, email у пользователя
    # TODO: добавить контакт в список и сохранить
    pass

def show_all():
    """Выводит все контакты."""
    contacts = load_contacts()
    # TODO: вывести все контакты в формате: Имя | Телефон | Email
    pass

def search_contact():
    """Ищет контакт по имени."""
    contacts = load_contacts()
    # TODO: запросить имя для поиска
    # TODO: найти контакты с таким именем и вывести
    pass

def show_menu():
    """Показывает меню и обрабатывает выбор пользователя."""
    while True:
        print("\n=== Телефонная книга ===")
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Поиск по имени")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            show_all()
        elif choice == '3':
            search_contact()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == '__main__':
    show_menu()