=================
JSON data support
=================

``funkload_friendly.datatypes.JSONData`` class extends ``funkload.utils.Data``. And support JSON parameter in HTTP POST.

.. code-block:: python

   from funkload_friendly.test import TestCase, description
   from funkload_friendly.datatypes import JSONData


   class APITest(TestCase):
       @description("Load REST API")
       def test_calculate_add(self):
           response = self.post(self.site_url + "/calculate/add/",
               params=JSONData({
                   'value1': 100,
                   'value2': 50,
               })
           )
           self.assertEqual(response.code, 200)
           self.assertEqual(response.data['result'], 150)
