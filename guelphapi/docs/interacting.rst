Interacting with GuelphDev API Service
==========================================

.. note::

    If you hit a stumbling block, you can email: npresta@uoguelph.ca

This documentation assumes you have a basic understanding of REST-style APIs and how to use `cURL <http://curl.haxx.se/>`_.

Authenticated Requests
----------------------

All requests must be authenticated by your developer username and API key.
In all examples, we omit the username and API key, but you should add them.

.. note::

    For all examples, remember to add username=<yourusername>&api_key=<yourapikey> to the URL string.

Front Matter
------------

GuelphDev API Service tries to treat all clients & all serialization types as equally as possible.
It also tries to be a good 'Net citizen & respects the HTTP method used as well as the ``Accepts`` headers sent.
Between these two, you control all interactions through relatively few endpoints.

.. warning::

  Should you try these URLs in your browser, be warned you **WILL** need to
  append ``?format=json`` (or ``xml`` or ``yaml``) to the URL. Your browser
  requests ``application/xml`` before ``application/json``, so you'll always
  get back XML if you don't specify it.

  That's also why it's recommended that you explore via cURL, because you
  avoid your browser's opinionated requests & get something closer to what
  any programmatic clients will get.

Output Formats Supported
------------------------

You may append ?format=FORMAT to the end of any URI, where FORMAT is equal to:

* json
* xml
* yaml

Simple Example
--------------

Let's fetch some information about our API::

    curl https://apiguelph-nickpresta.ca/api/v1/

.. code-block:: javascript

    {
      course: {
        list_endpoint: "/api/v1/course/",
        schema: "/api/v1/course/schema/"
      },
      event: {
        list_endpoint: "/api/v1/event/",
        schema: "/api/v1/event/schema/"
      },
      mealplan: {
        list_endpoint: "/api/v1/mealplan/",
        schema: "/api/v1/mealplan/schema/"
      },
      news: {
        list_endpoint: "/api/v1/news/",
        schema: "/api/v1/news/schema/"
      },
      schedule: {
        list_endpoint: "/api/v1/schedule/",
        schema: "/api/v1/schedule/schema/"
      }
    }

We can see that we have a few resources, and their list enpoints, and schemas. Let's fetch information about a resource::

    curl https://apiguelph-nickpresta.ca/api/v1/news/schema/

.. code-block:: javascript

    {
      "filtering": {
        "category": [
          "exact", 
          "iexact", 
          "contains", 
          "icontains"
        ], 
        "datetime_published": [
          "exact", 
          "range", 
          "gt", 
          "gte", 
          "lt", 
          "lte"
        ]
      }, 
      "allowed_detail_http_methods": [
        "get"
      ], 
      "fields": {
        "category": {
          "nullable": false, 
          "default": "", 
          "readonly": false, 
          "blank": false, 
          "help_text": "Unicode string data. Ex: \"Hello World\"", 
          "unique": false, 
          "type": "string"
        }, 
        "title": {
          "nullable": false, 
          "default": "", 
          "readonly": false, 
          "blank": false, 
          "help_text": "Unicode string data. Ex: \"Hello World\"", 
          "unique": false, 
          "type": "string"
        }, 
        "content": {
          "nullable": false, 
          "default": "", 
          "readonly": false, 
          "blank": false, 
          "help_text": "Unicode string data. Ex: \"Hello World\"", 
          "unique": false, 
          "type": "string"
        }, 
        "link": {
          "nullable": false, 
          "default": "No default provided.", 
          "readonly": false, 
          "blank": false, 
          "help_text": "Unicode string data. Ex: \"Hello World\"", 
          "unique": false, 
          "type": "string"
        }, 
        "id": {
          "nullable": false, 
          "default": "", 
          "readonly": false, 
          "blank": false, 
          "help_text": "Unicode string data. Ex: \"Hello World\"", 
          "unique": true, 
          "type": "string"
        }, 
        "datetime_published": {
          "nullable": false, 
          "default": "No default provided.", 
          "readonly": false, 
          "blank": false, 
          "help_text": "A date & time as a string. Ex: \"2010-11-10T03:07:43\"", 
          "unique": false, 
          "type": "datetime"
        }, 
        "resource_uri": {
          "nullable": false, 
          "default": "No default provided.", 
          "readonly": true, 
          "blank": false, 
          "help_text": "Unicode string data. Ex: \"Hello World\"", 
          "unique": false, 
          "type": "string"
        }
      }, 
      "default_format": "application/json", 
      "default_limit": 20, 
      "allowed_list_http_methods": [
        "get"
      ]
    }

Here you can see all the fields and associated types, as well as any filtering options.

.. note::

    For more information about how to fetch data for a specific resource, see: :doc:`resources`


