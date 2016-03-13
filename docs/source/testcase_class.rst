=======================
friendly TestCase class
=======================

funkload-friendly provides a TestCase, it is extended FunkLoadTestCase.

This class features: 

- Keep cookie data between multiple requrests.
- Be able to configure log and result output directory.
- decorator for test description

Cookie support
==============

Configration support
====================

Description decorator
=====================

**Example**:

.. code-block:: python

   from funkload_friendly.test import TestCase, description


   class MainTest(TestCase):
       @description("Load top_page")
       def test_top_page(self):
           self.get(self.site_url + "/")

**Result(log)**::

   test_top_page: Starting -----------------------------------
           Load top_page
   test_top_page: GET: http://localhost:8000/
           Page 1:  ...
   test_top_page:  Done in 0.005s
   test_top_page:  Load css and images...
   test_top_page:   Done in 0.000s
