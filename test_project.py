from project import verify_password, save_password, save_code, retrieve


def test_save_code():
    assert save_code('123456') == 'Password saved successfully'


def test_verify_password():
    assert verify_password('q!:mb[4Eft') == 'This password is in use by Google'
    assert verify_password('luqkwyJF') == 'This password is in use by Amazon'
    assert verify_password('hello') == 'This password is not in use'

def test_retrieve():
    assert retrieve('x([ti|bLmA') == 'Your password is q!:mb[4Eft'
    assert retrieve('hello') == 'Password not found'