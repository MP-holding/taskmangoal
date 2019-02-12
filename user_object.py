import hashlib
import os
import csv


class User:
    user_id = 0
    user_list = []
    title_of_gender = {'female': 'Ms.', 'male': 'Mr.'}

    def __init__(self, gender, first_name, last_name, user_name, password, passwoed_is_hashed=False):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password if passwoed_is_hashed else hashlib.sha3_256(password.encode('utf-8')).hexdigest()

    @classmethod
    def create_user(cls, *args, **kwargs):
        new_user = cls(*args, **kwargs)
        if not cls.user_name_exists(new_user):
            cls.user_list.append(new_user)
            return new_user
        else:
            return False

    def __eq__(self, other):
        return self.user_name == other.user_name

    @classmethod
    def get_user(cls, user_name):
        if cls.user_name_exists(user_name):
            return [user for user in cls.user_list if user.user_name == user_name][0]

    @classmethod
    def user_exists(cls, user):
        return user in cls.user_list

    @classmethod
    def user_name_exists(cls, user_name):
        return user_name in [user.user_name for user in cls.user_list]

    @classmethod
    def read_users(cls):
        if os.path.isfile('user_list.csv'):
            with open('user_list.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls.user_list.append(cls(**row, passwoed_is_hashed=True))

    @classmethod
    def save_users(cls):
        with open('user_list.csv', 'w', newline='') as csvfile:
            items = ['gender', 'first_name', 'last_name', 'user_name', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=items)
            writer.writeheader()
            for user in cls.user_list:
                writer.writerow(user.__dict__)

    def authenticate(self, new_password):
        new_password = hashlib.sha3_256(new_password.encode('utf-8')).hexdigest()
        if new_password == self.password:
            return True
        else:
            return False

    def fullname(self):
        title = self.title_of_gender[self.gender.lower()]
        return '{} {} {}'.format(title, self.first_name, self.last_name)
