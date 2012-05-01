GuelphDev API Service Resources
===============================

The resources that you can interact with through the API are described below.

.. note::

    If you hit a stumbling block, you can email: npresta@uoguelph.ca

This documentation assumes you have a basic understanding of REST-style APIs.


News
----

A News resource object represents a news item from the University of Guelph's news feed.

====== =================
METHOD URI
====== =================
LIST   /api/v1/news/
GET    /api/v1/news/<id>
====== =================

Object Representation
^^^^^^^^^^^^^^^^^^^^^

**LIST**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/news/?format=json

.. code-block:: javascript

    {
      meta: {
        limit: 20,
        next: null,
        offset: 0,
        previous: null,
        total_count: 15
      },
      objects: [
        {
          category: "Campus Bulletin",
          content: "President Alastair Summerlee is calling for nominations for the 2012...",
          datetime_published: "2012-05-01T13:13:15+00:00",
          id: "1",
          link: "http://www.uoguelph.ca/news/2012/05/nominees_sought_5.html",
          resource_uri: "/api/v1/news/1/",
          title: "Nominees Sought for Exemplary Staff Awards, Deadline Today"
        },
        {
          category: "Campus Bulletin",
          content: "The University of Guelph is moving forward with one of the...",
          datetime_published: "2012-04-30T13:42:48+00:00",
          id: "2",
          link: "http://www.uoguelph.ca/news/2012/04/school_for_civi.html",
          resource_uri: "/api/v1/news/2/",
          title: "School for Civil Society Consultations Begin",
        },
        ...
    }

**GET**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/news/?format=json

.. code-block:: javascript

    {
      category: "Campus Bulletin",
      content: "President Alastair Summerlee is calling for nominations for the 2012...",
      datetime_published: "2012-05-01T13:13:15+00:00",
      id: "1",
      link: "http://www.uoguelph.ca/news/2012/05/nominees_sought_5.html",
      resource_uri: "/api/v1/news/1/",
      title: "Nominees Sought for Exemplary Staff Awards, Deadline Today"
    }

Events
------

An Event resource object represents an event item from the University of Guelph's Student Affairs website.

====== =================
METHOD URI
====== =================
LIST   /api/v1/event/
GET    /api/v1/event/<id>
====== =================

Object Representation
^^^^^^^^^^^^^^^^^^^^^

**LIST**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/event/?format=json

.. code-block:: javascript

    {
      meta: {
        limit: 20,
        next: "/api/v1/event/?limit=20&offset=20&format=json",
        offset: 0,
        previous: null,
        total_count: 41
      },
      objects: [
        {
          advanced_registration: "This event requires 3 hours of advanced registration. Please register before May 02, 2012, 12:00 PM",
          contact: "Jane Burpee",
          date: "Wednesday May 2, 2012",
          description: "Students completing their Graduate degrees...",
          eligibility: "Master Thesis students, Doctoral students, Faculty Theses Advisors and staff.",
          event_format: "Workshop",
          id: "1",
          instructors: "Jane Burpee",
          link: "http://www.uoguelph.ca/studentaffairs/reg/index.cfm?event_id=5786",
          location: "Basement Computer Lab, Room 034, Library",
          maximum_attendance: "14",
          more_information: "",
          organization: "The Learning Commons",
          qualifies_as: "",
          resource_uri: "/api/v1/event/1/",
          time: "3:00 PM - 4:00 PM (1 hours)",
          title: "Electronic Thesis and Dissertations:  Hands-on submission workshop",
          topic: "Graduate Student Programs"
        }
        {
          advanced_registration: "This event requires 48 hours of advanced registration. Please register before May 07, 2012, 11:30 PM",
          contact: "Debbie 519 824 4120 ext 53744",
          date: "Wednesday May 9, 2012",
          description: "Take advantage of your lunch break on May 9th to get to know the teachers and staff of ELPas well as your classmates! Enjoy some free delicious sushi!",
          eligibility: "ELP students",
          event_format: "Special Event",
          id: "2",
          instructors: "Lily Suggett, Allison Dyjach, Debbie Noorland",
          link: "http://www.uoguelph.ca/studentaffairs/reg/index.cfm?event_id=5788",
          location: "To Be Confirmed",
          maximum_attendance: "50",
          more_information: "",
          organization: "English Language Programs (ELP)",
          qualifies_as: "",
          resource_uri: "/api/v1/event/2/",
          time: "11:30 PM - 1:30 AM (2 hours)",
          title: "Sushi Social",
          topic: "ELCP Event"
        }
        ...
    }

**GET**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/event/1/?format=json

.. code-block:: javascript

    {
      advanced_registration: "This event requires 3 hours of advanced registration. Please register before May 02, 2012, 12:00 PM",
      contact: "Jane Burpee",
      date: "Wednesday May 2, 2012",
      description: "Students completing their Graduate degrees...",
      eligibility: "Master Thesis students, Doctoral students, Faculty Theses Advisors and staff.",
      event_format: "Workshop",
      id: "1",
      instructors: "Jane Burpee",
      link: "http://www.uoguelph.ca/studentaffairs/reg/index.cfm?event_id=5786",
      location: "Basement Computer Lab, Room 034, Library",
      maximum_attendance: "14",
      more_information: "",
      organization: "The Learning Commons",
      qualifies_as: "",
      resource_uri: "/api/v1/event/1/",
      time: "3:00 PM - 4:00 PM (1 hours)",
      title: "Electronic Thesis and Dissertations:  Hands-on submission workshop",
      topic: "Graduate Student Programs"
    }

Courses
-------

A Course resource object represents a course item from the University of Guelph's Academic Calendar.

====== =================
METHOD URI
====== =================
LIST   /api/v1/course/
GET    /api/v1/course/<id>
====== =================

Object Representation
^^^^^^^^^^^^^^^^^^^^^

**LIST**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/course/?format=json

.. code-block:: javascript

    {
      meta: {
        limit: 20,
        next: "/api/v1/course/?limit=20&offset=20&format=json",
        offset: 0,
        previous: null,
        total_count: 1837
      },
      objects: [
        {
          code: "ACCT2220",
          credit: "0.50",
          department: "ACCT",
          description: "An introductory course designed to develop an understanding of...",
          id: "1",
          number: "2220",
          prerequisites: "1 of ECON1050, ECON1100, ENGG3240, FARE1400",
          resource_uri: "/api/v1/course/1/",
          restrictions: "Priority Access course. Enrolment may be restricted to particular programs or specializations. See department for more information.",
          semesters: "F,W",
          title: "Financial Accounting"
        },
        ...
        {
          code: "ZOO4950",
          credit: "0.25",
          department: "ZOO",
          description: "This course provides a practical experience in the study of Mammalogy. ...",
          id: "1837",
          number: "4950",
          prerequisites: "ZOO4910",
          resource_uri: "/api/v1/course/1837/",
          restrictions: "",
          semesters: "W",
          title: "Lab Studies in Mammalogy"
        },
    }

**GET**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/course/1/?format=json

.. code-block:: javascript

    {
      code: "ACCT2220",
      credit: "0.50",
      department: "ACCT",
      description: "An introductory course designed to develop an understanding of...",
      id: "1",
      number: "2220",
      prerequisites: "1 of ECON1050, ECON1100, ENGG3240, FARE1400",
      resource_uri: "/api/v1/course/1/",
      restrictions: "Priority Access course. Enrolment may be restricted to particular programs or specializations. See department for more information.",
      semesters: "F,W",
      title: "Financial Accounting"
    }

Mealplan
--------

A Mealplan resource object represents a meal plan from the University of Guelph's Hospitality Services.

====== =========================== ============= ========================================================================
METHOD URI                         Authenticated Notes
====== =========================== ============= ========================================================================
GET    /api/v1/mealplan/<username> Yes           The `userid` value must be the student's central login name (e.g. jdoe).
====== =========================== ============= ========================================================================

Object Representation
^^^^^^^^^^^^^^^^^^^^^

**GET**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/mealplan/jdoe/?format=json

.. code-block:: javascript

    {
      balance: "16.07",
      resource_uri: "/api/v1/mealplan/jdoe/",
      type: "Ultra Meal Plan",
      user: "jdoe"
    }

Schedule
--------

A Schedule resource object represents a class schedule from the University of Guelph's WebAdvisor site.

====== =========================== ============= ========================================================================
METHOD URI                         Authenticated Notes
====== =========================== ============= ========================================================================
GET    /api/v1/schedule/<username> Yes           The `userid` value must be the student's central login name (e.g. jdoe).
====== =========================== ============= ========================================================================

Object Representation
^^^^^^^^^^^^^^^^^^^^^

**GET**::

    https://apiguelph-nickpresta.dotcloud.com/api/v1/schedule/jdoe/?format=json

.. code-block:: javascript

    {
      resource_uri: "/api/v1/schedule/jdoe/",
      schedule: [
        {
          days: "Tues, Thur ",
          end_date: "2012/04/20",
          location: "ROZH, Room 101,1",
          name: "ANTH*1150*01",
          start_date: "2012/01/09",
          times: "10:00AM - 11:20AM",
          type: "LEC"
        },
        {
          days: "Thur ",
          end_date: "2012/04/19",
          location: "ROZH, Room 101,2",
          name: "ANTH*1150*01",
          start_date: "2012/04/19",
          times: "07:00PM - 09:00PM",
          type: "EXAM"
        },
        {
          days: "Days TBA",
          end_date: "2012/04/20",
          location: "Room TBA,2",
          name: "PHIL*2140*DE",
          start_date: "2012/01/09",
          times: "Times TBA",
          type: "Distance Education"
        },
        {
          days: "Wed ",
          end_date: "2012/04/18",
          location: "MACN, Room 113",
          name: "PHIL*2140*DE",
          start_date: "2012/04/18",
          times: "11:30AM - 01:30PM",
          type: "EXAM"
        }
      ],
      user: "jdoe"
    }


