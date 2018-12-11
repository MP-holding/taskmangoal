import hashlib


class User:
    user_id = 0
    user_list = {}

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        self.password = password
        if user_name not in User.user_list:
            User.user_id += 1

    def authenticate(self):
        user_list = {self.user_name: self.password}
        if self.user_name in user_list:
            if self.password == user_list[self.user_name]:
                print('Welcome!', User.fullname(self))
                return True
            else:
                print('Invalid username or password')

    def fullname(self):
        gender = input('what is your gender(Male or Female)? ')
        if gender == 'female' or gender == 'Female':
            title = 'Ms.'
        else:
            title = 'Mr.'
        return '{} {} {}'.format(title, self.first_name, self.last_name)


class Task:
    def __init__(self, user_id, task_id, tak_summary, task_date, progress ):
        user_id = User.user_id

    def show_task(self):
        pass

    def save_task(self):
        pass

    def load_task(self):
        pass


