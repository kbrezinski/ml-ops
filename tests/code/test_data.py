
import pandas as pd


# Test data frame
def test_df():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    assert df.shape == (3, 2)


# Base fruit class
class Fruit(object):
    def __init__(self, name):
        self.name = name

# Test fruit class
class TestFruit(object):
    @classmethod
    def setup_class(cls):
        """Set up the state for any class instance."""
        pass

    @classmethod
    def teardown_class(cls):
        """Teardown the state created in setup_class."""
        pass

    def setup_method(self):
        """Called before every method to setup any state."""
        self.fruit = Fruit(name="apple")

    def teardown_method(self):
        """Called after every method to teardown any state."""
        del self.fruit

    def test_init(self):
        assert self.fruit.name == "apple"