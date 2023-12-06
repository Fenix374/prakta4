class User:
    def __init__(self, username, password, role, full_name):
        self.username = username
        self.password = password
        self.role = role
        self.full_name = full_name


class Order:
    def __init__(self, user, products):
        self.user = user
        self.products = products


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Database:
    users = []
    orders = []
    products = []

    @classmethod
    def add_user(cls, user):
        cls.users.append(user)

    @classmethod
    def add_order(cls, order):
        cls.orders.append(order)

    @classmethod
    def add_product(cls, product):
        cls.products.append(product)

def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    role = input("Выберите роль (client/employee/admin): ")
    full_name = input("Введите ваше полное имя: ")

    new_user = User(username, password, role, full_name)
    Database.add_user(new_user)
    print("Регистрация прошла успешно!")


def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    for user in Database.users:
        if user.username == username and user.password == password:
            return user

    print("Неверное имя пользователя или пароль.")
    return None


def display_products():
    print("Товары в магазине:")
    for product in Database.products:
        print(f"{product.name} - {product.price} руб.")


def filter_products_by_price():
    min_price = float(input("Введите минимальную цену: "))
    max_price = float(input("Введите максимальную цену: "))

    filtered_products = [product for product in Database.products if min_price <= product.price <= max_price]

    print("Отфильтрованные товары:")
    for product in filtered_products:
        print(f"{product.name} - {product.price} руб.")


def add_product_to_order(user, order):
    display_products()
    product_name = input("Введите название товара, который хотите добавить в заказ: ")

    product = next((p for p in Database.products if p.name == product_name), None)

    if product:
        order.products.append(product)
        print(f"Товар {product.name} добавлен в ваш заказ.")
    else:
        print("Такого товара нет в магазине.")


def view_order(user, order):
    if order.products:
        print("Ваш заказ:")
        for product in order.products:
            print(f"{product.name} - {product.price} руб.")
    else:
        print("Ваш заказ пуст.")


def remove_order(user, order):
    if order.products:
        order.products = []
        print("Ваш заказ удален.")
    else:
        print("Ваш заказ уже пуст.")


def display_all_products():
    print("Все товары в магазине:")
    for product in Database.products:
        print(f"{product.name} - {product.price} руб.")


def add_product():
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))

    new_product = Product(name, price)
    Database.add_product(new_product)
    print(f"Товар {name} успешно добавлен.")


def edit_product():
    display_all_products()
    product_name = input("Введите название товара для редактирования: ")

    product = next((p for p in Database.products if p.name == product_name), None)

    if product:
        new_name = input("Введите новое название товара: ")
        new_price = float(input("Введите новую цену товара: "))

        product.name = new_name
        product.price = new_price
        print("Товар успешно отредактирован.")
    else:
        print("Такого товара нет в магазине.")


def delete_product():
    display_all_products()
    product_name = input("Введите название товара для удаления: ")

    product = next((p for p in Database.products if p.name == product_name), None)

    if product:
        Database.products.remove(product)
        print("Товар успешно удален.")
    else:
        print("Такого товара нет в магазине.")


def display_all_employees():
    print("Список сотрудников:")
    for user in Database.users:
        if user.role == "employee":
            print(f"{user.full_name} - {user.username}")


def add_employee():
    username = input("Введите имя пользователя сотрудника: ")
    password = input("Введите пароль сотрудника: ")
    full_name = input("Введите полное имя сотрудника: ")

    new_employee = User(username, password, "employee", full_name)
    Database.add_user(new_employee)
    print(f"Сотрудник {full_name} успешно добавлен.")


def edit_employee():
    display_all_employees()
    employee_username = input("Введите имя пользователя сотрудника для редактирования: ")

    employee = next((u for u in Database.users if u.username == employee_username and u.role == "employee"), None)

    if employee:
        new_username = input("Введите новое имя пользователя: ")
        new_password = input("Введите новый пароль: ")
        new_full_name = input("Введите новое полное имя: ")

        employee.username = new_username
        employee.password = new_password
        employee.full_name = new_full_name
        print("Данные сотрудника успешно отредактированы.")
    else:
        print("Такого сотрудника нет в списке.")


def delete_employee():
    display_all_employees()
    employee_username = input("Введите имя пользователя сотрудника для удаления: ")

    employee = next((u for u in Database.users if u.username == employee_username and u.role == "employee"), None)

    if employee:
        Database.users.remove(employee)
        print("Сотрудник успешно удален.")
    else:
        print("Такого сотрудника нет в списке.")


def client_menu(user):
    current_order = Order(user, [])

    while True:
        print("\nМеню клиента:")
        print("1. Просмотреть товары")
        print("2. Фильтрация товаров по цене")
        print("3. Добавить товар в заказ")
        print("4. Просмотреть заказ")
        print("5. Удалить заказ")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_products()
        elif choice == "2":
            filter_products_by_price()
        elif choice == "3":
            add_product_to_order(user, current_order)
        elif choice == "4":
            view_order(user, current_order)
        elif choice == "5":
            remove_order(user, current_order)
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


def employee_menu(user):
    while True:
        print("\nМеню сотрудника:")
        print("1. Просмотреть все товары")
        print("2. Добавить новый товар")
        print("3. Редактировать товар")
        print("4. Удалить товар")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_all_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


def admin_menu(user):
    while True:
        print("\nМеню админа:")
        print("1. Просмотреть всех сотрудников")
        print("2. Добавить нового сотрудника")
        print("3. Редактировать данные сотрудника")
        print("4. Удалить сотрудника")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_all_employees()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            edit_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


def main():
    while True:
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                if user.role == "client":
                    client_menu(user)
                elif user.role == "employee":
                    employee_menu(user)
                elif user.role == "admin":
                    admin_menu(user)
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
