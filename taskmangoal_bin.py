from user_object import User
import hashlib

User.read_users()


def register():
    gd = input('gender: ')
    fn = input('first_name: ')
    ln = input('last_name: ')
    un = input('user_name: ')
    pw = input('password: ')
    return User.create_user(gd, fn, ln, un, pw)


def login():
    user_name = input('user_name: ')
    password = input('password: ')
    if User.user_name_exists(user_name):
        user = User.get_user(user_name)
        if user.authenticate(password):
            return user
        else:
            return False


active_user = None
while True:
    login_or_register = input('Dou you want to login or register?').lower()
    if login_or_register == 'login':
        active_user = login()

    elif login_or_register == 'register':
        active_user = register()
    else:
        print('please input "login" or "register')

    if active_user:
        print('Welcome', active_user.fullname())
        break

User.save_users()
