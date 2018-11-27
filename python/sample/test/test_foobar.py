from unittest import TestCase, mock
from unittest.mock import MagicMock

from foobar import Foobar


class TestFoobar(TestCase):

    def setUp(self):
        print('I run before every test')

    def tearDown(self):
        print('I run after every test')

    def test_yes(self):
        self.assertTrue(True)

    def test_foobar_is_true(self):
        # setup
        foobar = Foobar()

        # exercise
        result = foobar.i_am_true()

        # verify
        self.assertTrue(result)

    def test_is_happy(self):
        """This is testing a private method"""
        # setup
        foobar = Foobar()

        # exercise
        result = foobar._i_am_happy(True)

        # verify
        self.assertEqual("happy", result)

    def test_list_buckets(self):
        """This is replacing a private member with a mock"""
        # setup
        foobar = Foobar()
        s3_mock = MagicMock()
        s3_mock.list_buckets.return_value = {'bucketa', 'bucketb'}
        foobar.s3 = s3_mock

        # exercise
        result = foobar._list_buckets()

        # verify
        self.assertIn('bucketa', result)

    @mock.patch('foobar.sys')
    def test_is_unhappy(self, sys_mock):
        """This is mocking the complete library. Try that in Java."""
        # setup
        foobar = Foobar()

        # exercise
        foobar._i_am_happy(False)

        # Verify
        self.assertEqual(1, sys_mock.exit.call_count)

#
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestFoobar)
#     unittest.TextTestRunner().run(suite)
