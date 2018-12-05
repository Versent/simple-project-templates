from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug|title }}
from unittest import TestCase, mock
from unittest.mock import MagicMock

"""Tests for `{{ cookiecutter.project_slug }}` package."""

class Test{{ cookiecutter.project_slug|title }}(TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        print('I run before every test')

    def tearDown(self):
        """Tear down test fixtures, if any."""
        print('I run after every test')

    def test_yes(self):
        self.assertTrue(True)

    def test_foobar_is_true(self):
        # setup
        {{ cookiecutter.project_slug.lower() }} = {{ cookiecutter.project_slug|title }}()

        # exercise
        result = {{ cookiecutter.project_slug.lower() }}.i_am_true()

        # verify
        self.assertTrue(result)

    def test_is_happy(self):
        """This is testing a private method"""
        # setup
        {{ cookiecutter.project_slug.lower() }} = {{ cookiecutter.project_slug|title }}()

        # exercise
        result = {{ cookiecutter.project_slug.lower() }}._i_am_happy(True)

        # verify
        self.assertEqual("happy", result)

    def test_list_buckets(self):
        """This is replacing a private member with a mock"""
        # setup
        {{ cookiecutter.project_slug.lower() }} = {{ cookiecutter.project_slug|title }}()
        s3_mock = MagicMock()
        s3_mock.list_buckets.return_value = {'bucketa', 'bucketb'}
        {{ cookiecutter.project_slug.lower() }}.s3 = s3_mock

        # exercise
        result = {{ cookiecutter.project_slug.lower() }}._list_buckets()

        # verify
        self.assertIn('bucketa', result)

    @mock.patch('{{ cookiecutter.project_slug.lower() }}.sys')
    def test_is_unhappy(self, sys_mock):
        """This is mocking the complete library. Try that in Java."""
        # setup
        {{ cookiecutter.project_slug.lower() }} = {{ cookiecutter.project_slug|title }}()

        # exercise
        {{ cookiecutter.project_slug.lower() }}._i_am_happy(False)

        # Verify
        self.assertEqual(1, sys_mock.exit.call_count)

#
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestFoobar)
#     unittest.TextTestRunner().run(suite)
