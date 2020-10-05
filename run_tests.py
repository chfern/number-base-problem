import unittest

def run_tests():
    loader = unittest.TestLoader()
    start_dir = './test'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()