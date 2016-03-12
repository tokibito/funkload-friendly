=====
Usage
=====

Install
=======

Install funkload-friendly with easy_install into system python environment or virtualenv.

::

   $ easy_install funkload-friendly

.. note::

   This package uses the easy_install to install.
   Because it can not "pip install funkload".

Getting Started
===============

1. Writing your load testing code. 

   **loadtest.py**:

   .. code-block:: python

      from funkload_friendly.test import TestCase, description


      class MainTest(TestCase):
          @description("Load top_page")
          def test_top_page(self):
              self.get(self.site_url + "/")

2. create config file(e.g. ``funkload.conf``).

   **funkload.conf**:

   .. code-block:: ini

      [main]
      title = My Project Loadtest
      description = load testing for myproject
      url = http://www.example.com
   
      [ftest]
      log_to = console file
      log_directory = ./
      result_directory = ./
      sleep_time_min = 0
      sleep_time_max = 0
   
      [bench]
      cycles = 1:3:10
      duration = 10
      startup_delay = 0.01
      sleep_time = 0.01
      cycle_time = 1
      sleep_time_min = 0
      sleep_time_max = 0.5
      log_to = console file
      log_directory = ./
      result_directory = ./

3. run benchmark test with fl-run-bench.

   ::

      $ fl-run-bench --config=funkload.conf loadtest MainTest.test_top_page

4. build the benchmark report.

   ::

      $ fl-build-report --html test_top_page.xml

.. note::

   There are some example codes: https://github.com/tokibito/funkload-friendly-example
