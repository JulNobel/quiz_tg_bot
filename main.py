from user import User


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def say_something(number: int, word: str):
    word = word.capitalize()
    return word * number


def get_user_info(user: User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


if __name__ == '__main__':
    print_hi('Julia')
    print(say_something(4, 'Julia'))
    user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
    print(get_user_info(user_1))