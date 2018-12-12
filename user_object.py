import hashlib


class User:
    user_id = 0
    user_list = {}
    title_of_gender = {'female': 'Ms.', 'male': 'Mr.'}

    def __init__(self, gender, first_name, last_name, user_name, password):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        if user_name not in User.user_list:
            User.user_id += 1

    def authenticate(self, new_password):
        new_password = hashlib.sha3_256(new_password.encode('utf-8')).hexdigest()
        if new_password == self.password:
            return True
        else:
            return False

    def fullname(self):
        title = self.title_of_gender[self.gender.lower()]
        return '{} {} {}'.format(title, self.first_name, self.last_name)
