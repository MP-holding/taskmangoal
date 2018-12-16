import pickle
import hashlib
import os
import csv


class Task:
    def __init__(self, summary, due_date, progress, user_id):
        self.summary = summary
        self.due_date = due_date
        self.progress = progress
        self.user_id = user_id
        self.id = hashlib.sha3_256(str(self.__dict__).encode('utf-8')).hexdigest()[:8]
        self.tasks_list = []

    def get_dict(self):
        return dict(self.__dict__)

    def save(self):
        with open(str(self.id), 'wb') as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return 'user_id = {}, task_id = {}, summary = {}, due_date = {}, progress = {}' \
            .format(self.user_id, self.id, self.summary, self.due_date, self.progress)

    def __eq__(self, other):
        return self.id == other.id

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as handle:
            return pickle.load(handle)

    # def revert(self):
    #     with open(str(self.id), 'r') as handle:
    #         return pickle.load(handle)

    def read_tasks(self):
        if os.path.isfile('tasks.csv'):
            with open('tasks.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for task in reader:
                    self.tasks_list.append(Task(**task))

    def create_task(self, *args, **kwargs):
        self.tasks_list.append(Task(*args, **kwargs))

    def get_task(self, requested_id):
        requested_task = [task for task in self.tasks_list if task['id'] == requested_id][0]
        return requested_task

    def sort_by_id(self):
        return sorted(self.tasks_list, key=lambda x: x['duration'])

    def writ_tasks(self):
        with open('tasks.csv', 'w', newline='') as csvfile:
            fieldnames = [key for key in self.__dict__.keys()]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks_list:
                writer.writerow(task)
