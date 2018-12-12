from User_object import User

if __name__ == '__main__':
    user_name = 'asghar'
    password = 'akbar'
    u = User('male', 'ali', 'behboudi', user_name, password)
    assert u.password != password, 'Password not hashed!'
    assert u.authenticate(password), 'Authentication failed'
    assert not u.authenticate('dummy' + password), 'Authentication should fail with wrong password!'
    assert u.fullname() == 'Mr. ali behboudi', 'Wrong fullname'
    assert u.user_id == 1, 'Uncorrected user_id '
