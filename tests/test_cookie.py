from unittest import TestCase


class CookieDictTest(TestCase):
    """test for CookieDict
    """
    def getTarget(self):
        from funkload_friendly.cookie import CookieDict as target
        return target

    def getOne(self, *args, **kwargs):
        return self.getTarget()(*args, **kwargs)

    def test_render_to_string(self):
        """CookieDict.render_to_string
        """
        cookie = self.getOne([('spam', 'egg'), ('ham', 'bacon')])
        self.assertEqual(cookie.render_to_string(), 'spam=egg;ham=bacon;')

    def test_from_cookie_string(self):
        """CookieDict.from_cookie_string
        """
        cookie = self.getOne()
        cookie.from_cookie_string('spam=egg;ham=bacon;')
        self.assertEqual(cookie, {'spam': 'egg', 'ham': 'bacon'})
