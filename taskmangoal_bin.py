from user_object import User
import hashlib

User.read_users()


def register(gender, first_name, last_name, user_name, password):
    for profile in User.user_list:
        if user_name in profile['user_name']:
            print('This user is available. please try another one.')
        else:
            continue

    user_profile = {}
    password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
    user_profile['gender'] = gender.lower()
    user_profile['first_name'] = first_name
    user_profile['last_name'] = last_name
    user_profile['user_name'] = user_name
    user_profile['password'] = password
    print(user_profile)
    User.user_list.append(user_profile)
    User.user_id += 1
    print('Successful Registration')


def login(user_name, password):
    for profile in User.user_list:
        if user_name not in profile['user_name']:
            print('Invalid user_name!')
        else:
            continue
    t = [profile for profile in User.user_list if profile['user_name'] == user_name][0]
    u = User(t['gender'], t['first_name'], t['last_name'], t['user_name'], t['password'])
    if u.authenticate(password) is True:
        print('Welcome', u.fullname())


login_or_register = input('Dou you want to login or register?')
if login_or_register == 'login'.lower():
    un = input('user_name: ')
    pw = input('password: ')
    login(un, pw)
elif login_or_register == 'register'.lower():
    gd = input('gender: ')
    fn = input('first_name: ')
    ln = input('last_name: ')
    un = input('user_name: ')
    pw = input('password: ')
    register(gd, fn, ln, un, pw)
else:
    print('please input "login" or "register')

print(User.user_list)
User.save_users()
