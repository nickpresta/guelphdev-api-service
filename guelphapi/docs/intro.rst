Introduction
============

GuelphAPI allows people to build software utilizing data extracted from the University of Guelph websites.
The API is mostly read-only but does support some authenticated requests.

How to access the API?
**********************

At the present time, the API is open to everyone, without any sort of API key. This will change in the future.
To access a resource, browse to:

    http://guelphapis.herokuapp.com/api/v1/

This will show you a listing of the resources, their schemas, and their endpoints for LIST operations.

Output Formats Supported
************************

You may append ?format=FORMAT to the end of any URI, where FORMAT is equal to:

* json
* jsonp
* xml
* yaml

For example:

    http://guelphapis.herokuapp.com/api/v1/?format=json

You will get back JSON:

.. code-block:: javascript

    {
      course: {
        list_endpoint: "/api/v1/course/",
        schema: "/api/v1/course/schema/"
      },
      news: {
        list_endpoint: "/api/v1/news/",
        schema: "/api/v1/news/schema/"
      }
    }

Contact Information
*******************

If you have any questions, or suggestions, please email:

  someemail@example.com
