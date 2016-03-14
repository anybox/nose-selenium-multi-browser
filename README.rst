===========================
Nose selenium multi browser
===========================

.. image:: https://api.travis-ci.org/anybox/nose-selenium-multi-browser.svg?branch=master
   :target: https://travis-ci.org/anybox/nose-selenium-multi-browser
   :alt: Travis

nose-selenium-multi-browser is a plugin for nose that provides support to launch
selenium tests, the same test case is launched over all browsers you define in
parallel.

QuickStart
==========

Your test case class should inherit SeleniumTestCase helper class to get an
instance of selenium driver (this helper class already inherit from
``unittest.TestCase``).

If you define more than one capabilities, each classes will be duplicate
and run over different capabilities.

Those classes will be launched at the same time in different process::

    from nose_selenium_multi_browser.selenium import SeleniumTestCase


    class MyTestCase(SeleniumTestCase):

        def test_python_web_site(self):
            self.selenium.get('https://www.python.org/')
            self.assertEquals(selenium.title, 'Welcome to Python.org')


To run it that::

    nosettests -v -s --with-selenium --selenium-config selenium.json \
                --processes 2 --process-timeout 5 test_selenium.py


where ``selenium.json`` looks like::

    {
      "drivers": [
        {
          "class": "selenium_extra.drivers.local.Chrome"
        },
        {
          "class": "selenium_extra.drivers.local.Firefox"
        },
        {
          "class": "selenium_extra.drivers.remote.Grid",
          "capabilities": {
              "command_executor": 'http://127.0.0.1:4444/wd/hub'
          },
          "request_drivers": [
            {
              "browserName": "firefox",
              "platform": "LINUX",
              "version": "",
              "capabilities": {
              }
            },
            {
              "browserName": "chrome",
              "platform": "LINUX",
              "version": "",
              "capabilities": {
              }
            }
          ]
        }
      ],
      "global_capabilities": {
      }
    }

Your tests will run on your local chrome and firefox browser and on a local
grid wich should contains nodes with chrome and firefox on linux machine.

Contribute
==========

You require chrome webdriver, firefox webdriver and a grid to run it locally

Setup local webdriver
---------------------

* **chrome**: https://sites.google.com/a/chromium.org/chromedriver/
* **firefox**: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver


Setup grid and nodes
--------------------

* https://hub.docker.com/r/selenium/
* https://github.com/SeleniumHQ/docker-selenium


Run tests
---------

In a single processes::

    nosetests nose_selenium_multi_browser/tests/ -v -s --log-config logging.conf

Using 2 processes::

    nosetests examples/ -v -s --log-config logging.conf --with-selenium \
              --processes 2 --process-timeout 5


Know issues
===========

* It looks like setupClass is called Twice in multiprocess
* There is something wrong unit testing selenium nose pluggin in multiprocess