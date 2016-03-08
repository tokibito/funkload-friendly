from unittest import TestCase


class TestCaseTest(TestCase):
    def getTarget(self):
        from funkload_friendly.test import TestCase

        class target(TestCase):
            log_directory = '/tmp/'
            result_directory = '/tmp/'

            def dummy(self):
                pass

        return target

    def getOne(self, *args, **kwargs):
        return self.getTarget()(*args, **kwargs)

    def test_set_session_id(self):
        """update session_id
        """
        testcase = self.getOne(methodName='dummy')
        testcase.session_id_key = 'sessionid'
        testcase.set_session_id('test_id')
        self.assertEqual(
            testcase.cookie[testcase.session_id_key],
            'test_id')


class DescriptionTest(TestCase):
    def getTarget(self):
        from funkload_friendly.test import description as target
        return target

    def test_decorate_method(self):
        """decorate instance method
        """
        description = self.getTarget()

        class Target(object):
            @description("spam description")
            def described_method(self):
                pass

        target = Target()
        self.assertEqual(
            target.described_method.description,
            "spam description")
