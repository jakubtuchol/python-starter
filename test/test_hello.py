from src.hello import hello


class TestHello(object):

    def test_basic(self):
        assert 'hello' == hello()
