class TestNumbers:
    def test_numbers(self):
        pass

class TestSubclass(TestCase):
    def test_numbers(self):
        pass

class Test_underscores_and_123(TestCase):
    def test_underscores(self):
        pass

class TestNestedClass:
    def test_nested(self):

        class NestedClass:
            ...
