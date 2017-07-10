import k_mapper.kmapper as kmap
from unittest.mock import patch

def test_two_var():
    print("\n------Two variable test------")
    # Test two variable map
    with patch('sys.argv', [kmap.__file__,'-n', '2', '-m', '0', '1']):
        kmap.main()
def test_three_var():
    print("\n------Three variable test------")
    # Test three variable map
    with patch('sys.argv', [kmap.__file__,'-n', '3', '-m', '0', '1', '2', '7']):
        kmap.main()

def test_four_var():
    print("\n------Four variable test------")
    # Test four variable map
    with patch('sys.argv', [kmap.__file__,'-n', '4', '-m', '0', '1', '4', '5']):
        kmap.main()

def run_test():
    test_two_var()
    test_three_var()
    test_four_var()


if __name__ == '__main__':
    run_test()
