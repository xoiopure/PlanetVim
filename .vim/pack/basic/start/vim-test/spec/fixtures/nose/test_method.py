def test_numbers():
    pass

def test_foo():
    class CustomException(Exception):
        pass
    mocker.patch('some.module', side_effect=CustomException())

    assert something
