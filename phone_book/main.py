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
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    email = input("Введите email: ")
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    contacts = load_contacts()
    contacts.append(new_contact)
    save_contacts(contacts)
    print("Контакт добавлен!")

def show_all():
    """Выводит все контакты."""
    contacts = load_contacts()
    print("\n=== Все контакты ===")
    if not contacts:
        print("Телефонная книга пуста.")
        return
        
    for contact in contacts:
        print(f"Имя: {contact['name']} | Телефон: {contact['phone']} | Email: {contact['email']}")

def search_contact():
    """Ищет контакт по имени."""
    search_name = input("Введите имя для поиска: ").lower()
    contacts = load_contacts()
    
    found_contacts = [c for c in contacts if search_name in c['name'].lower()]
    
    print("\nНайденные контакты:")
    if not found_contacts:
        print("Контакты не найдены.")
    else:
        for contact in found_contacts:
            print(f"Имя: {contact['name']} | Телефон: {contact['phone']} | Email: {contact['email']}")

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