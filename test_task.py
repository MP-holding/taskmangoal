from task_object import Task

if __name__ == '__main__':
    t = Task('programming', '2019/1/12', 0, 'Maryam_kia')
    assert t.get_dict() == {'user_id': 'Maryam_kia',
                            'id': t.id,
                            'summary': 'programming',
                            'due_date': '2019/1/12',
                            'progress': 0,
                            }
    t.save()
    t2 = Task.load(str(t.id))
    assert t == t2, 'load/save Error'

    t.__str__()
