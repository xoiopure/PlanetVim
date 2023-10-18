class TestNumbers:
    def test_numbers(self):
        pass

class TestSubclass(Subclass):
    def test_subclass(self):
        pass

class Test_underscores_and_123(Subclass):
    def test_underscores(self):
        pass

class UnittestClass(unittest.TestCase):
    def test_unittest(self):
        pass

class SomeTest(TestCase):
    def test_foo(self):
        foo = date(2017, 11, 16)
