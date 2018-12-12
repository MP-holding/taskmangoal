import hashlib
import datetime


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
            print('Welcome!', User.fullname(self))
            return True
        else:
            print('Invalid username or password')

    def fullname(self):
        title = self.title_of_gender[self.gender.lower()]
        return '{} {} {}'.format(title, self.first_name, self.last_name)


class Task:
    def __init__(self, task_id, task_summary, task_date, progress):
        self.task_id = task_id
        self.task_summary = task_summary
        self.task_date = task_date
        self.progress = progress

    def create(self):
        task_date = datetime.datetime.strptime(self.task_date, '%Y/%m/%d')
        till_date = task_date - datetime.datetime.today()
        task_info = {'user_id': User.user_id,
                     'task_id': self.task_id,
                     'task_summary': self.task_summary,
                     'task_date': self.task_date,
                     'task_progress': self.progress,
                     'task_duration': till_date
                     }
        return task_info

    def show_task(self):
        print(Task.task_info)

        pass

    def load_task(self):
        pass
