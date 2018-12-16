import pickle
import hashlib


class Task:
    def __init__(self, summary, due_date, progress, user_id):
        self.summary = summary
        self.due_date = due_date
        self.progress = progress
        self.user_id = user_id
        self.id = hashlib.sha3_256(str(self.__dict__).encode('utf-8')).hexdigest()[:8]

    def get_dict(self):
        return dict(self.__dict__)

    def save(self):
        with open(str(self.id), 'wb') as handle:
            pickle.dump(self, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return 'user_id = {}, task_id = {}, summary = {}, due_date = {}, progress = {}'\
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

