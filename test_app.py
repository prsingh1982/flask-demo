from app import rollthedice


def test_app():
    assert 1 or 2 or 3 or 4 or 5 or 6 in rollthedice()
