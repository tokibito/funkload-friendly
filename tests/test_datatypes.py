from unittest import TestCase


class JSONDataTest(TestCase):
    def getTarget(self):
        from funkload_friendly.datatypes import JSONData as target
        return target

    def getOne(self, *args, **kwargs):
        return self.getTarget()(*args, **kwargs)

    def test_encoded_data(self):
        """JSONData object has encoded json string.
        """
        data = self.getOne({'spam': 'egg'})
        self.assertEqual(data.data, '{"spam": "egg"}')
