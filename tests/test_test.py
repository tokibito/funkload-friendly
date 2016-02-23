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
