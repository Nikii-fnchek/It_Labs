class UserAccount:
    def __init__(self, username, email, password):
        # Созаём аккаунт пользователя
        self.username = username
        self.email = email
        self.__password = hash(password)  # Приватное место для хранения хеш-пароля

    def set_password(self, new_password):
        # Тут изменяем пароль аккаунта
        self.__password = hash(new_password)

    def check_password(self, password):
        # Это проверяет корректность введенного пароля
        return self.__password == hash(password)

# Создаем объект класса UserAccount
user_account = UserAccount("user", "userexample@chto-to.com", "123password")

# Проверяем текущий пароль
print("Проверка пароля (правильный):", user_account.check_password("123password"))  # Должно вернуть True
# Изменяем пароль
user_account.set_password("new_password")
# Проверяем новый пароль
print("Проверка пароля (новый):", user_account.check_password("new_password"))  # Должно вернуть True
# Проверяем старый пароль
print("Проверка пароля (старый):", user_account.check_password("123password"))  # Должно вернуть False