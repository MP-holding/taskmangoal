from with_object import User

if __name__ == '__main__':
    user_name = 'asghar'
    password = 'akbar'
    u = User('ali', 'behboudi', user_name, password)
    assert u.password != password, 'Password not hashed!'
    assert u.authenticate(), 'Authentication failed'
    password = 'dummy' + password
    # assert not u.authenticate('dummy' + password), 'Authentication should fail with wrong password!'
    assert not u.authenticate(), 'Authentication should fail with wrong password!'
    print(u.fullname())
    print(u.user_id)
