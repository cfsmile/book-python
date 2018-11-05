************************
Python HTTP using stdlib
************************


``http.HTTPStatus``
===================

Using statuses
--------------
.. code-block:: python

    from http import HTTPStatus

    HTTPStatus.OK
    HTTPStatus.OK == 200

    HTTPStatus.OK.value
    HTTPStatus.OK.phrase
    HTTPStatus.OK.description

    list(HTTPStatus)

Most common statuses
--------------------
.. code-block:: python

    from http import HTTPStatus


    HTTPStatus.OK                       # 200
    HTTPStatus.CREATED                  # 201
    HTTPStatus.MOVED_PERMANENTLY        # 301
    HTTPStatus.FOUND                    # 302
    HTTPStatus.BAD_REQUEST              # 400
    HTTPStatus.UNAUTHORIZED             # 401
    HTTPStatus.FORBIDDEN                # 403
    HTTPStatus.METHOD_NOT_ALLOWED       # 405
    HTTPStatus.NOT_FOUND                # 404
    HTTPStatus.INTERNAL_SERVER_ERROR    # 500

All statuses
------------
.. csv-table:: ``http.HTTPStatus``
    :header-rows: 1
    :widths: 15, 85

    "Code", "Description"
    "100", "``CONTINUE``"
    "101", "``SWITCHING_PROTOCOLS``"
    "102", "``PROCESSING``"
    "200", "``OK``"
    "201", "``CREATED``"
    "202", "``ACCEPTED``"
    "203", "``NON_AUTHORITATIVE_INFORMATION``"
    "204", "``NO_CONTENT``"
    "205", "``RESET_CONTENT``"
    "206", "``PARTIAL_CONTENT``"
    "207", "``MULTI_STATUS``"
    "208", "``ALREADY_REPORTED``"
    "226", "``IM_USED``"
    "300", "``MULTIPLE_CHOICES``"
    "301", "``MOVED_PERMANENTLY``"
    "302", "``FOUND``"
    "303", "``SEE_OTHER``"
    "304", "``NOT_MODIFIED``"
    "305", "``USE_PROXY``"
    "307", "``TEMPORARY_REDIRECT``"
    "308", "``PERMANENT_REDIRECT``"
    "400", "``BAD_REQUEST``"
    "401", "``UNAUTHORIZED``"
    "402", "``PAYMENT_REQUIRED``"
    "403", "``FORBIDDEN``"
    "404", "``NOT_FOUND``"
    "405", "``METHOD_NOT_ALLOWED``"
    "406", "``NOT_ACCEPTABLE``"
    "407", "``PROXY_AUTHENTICATION_REQUIRED``"
    "408", "``REQUEST_TIMEOUT``"
    "409", "``CONFLICT``"
    "410", "``GONE``"
    "411", "``LENGTH_REQUIRED``"
    "412", "``PRECONDITION_FAILED``"
    "413", "``REQUEST_ENTITY_TOO_LARGE``"
    "414", "``REQUEST_URI_TOO_LONG``"
    "415", "``UNSUPPORTED_MEDIA_TYPE``"
    "416", "``REQUEST_RANGE_NOT_SATISFIABLE``"
    "417", "``EXPECTATION_FAILED``"
    "421", "``MISDIRECTED_REQUEST``"
    "422", "``UNPROCESSABLE_ENTITY``"
    "423", "``LOCKED``"
    "424", "``FAILED_DEPENDENCY``"
    "426", "``UPGRADE_REQUIRED``"
    "428", "``PRECONDITION_REQUIRED``"
    "429", "``TOO_MANY_REQUESTS``"
    "431", "``REQUEST_HEADER_FIELDS_TOO_LARGE``"
    "500", "``INTERNAL_SERVER_ERROR``"
    "501", "``NOT_IMPLEMENTED``"
    "502", "``BAD_GATEWAY``"
    "503", "``SERVICE_UNAVAILABLE``"
    "504", "``GATEWAY_TIMEOUT``"
    "505", "``HTTP_VERSION_NOT_SUPPORTED``"
    "506", "``VARIANT_ALSO_NEGOTIATES``"
    "507", "``INSUFFICIENT_STORAGE``"
    "508", "``LOOP_DETECTED``"
    "510", "``NOT_EXTENDED``"
    "511", "``NETWORK_AUTHENTICATION_REQUIRED``"


``urllib``
==========
.. literalinclude:: src/http-urllib.py
    :name: listing-http-urlib
    :language: python
    :caption: ściąganie danych z internetu, które trzeba rozpakować, Dane są w formacie TSV (tab separator values), można je rozpakować modułem CSV i podać jako ``delimiter='\t'``


``http.server``
===============
.. warning:: ``http.server`` is not recommended for production. It only implements basic security checks.

* https://docs.python.org/3.7/library/http.server.html#module-http.server

.. code-block:: python

    def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()

``http.client``
===============

GET Request
-----------
.. code-block:: python

    import http.client


    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("GET", "/")
    response = conn.getresponse()

    response.status         # 200
    response.reason         # OK

    data = response.read()  # This will return entire content.
    conn.close()

GET Request in chunks
---------------------
.. code-block:: python

    import http.client


    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("GET", "/")
    response = conn.getresponse()

    # The following example demonstrates reading data in chunks.
    while not response.closed:
        print(response.read(200))   # 200 bytes

GET Request to Not Existing Resource
------------------------------------
.. code-block:: python

    import http.client


    conn = http.client.HTTPSConnection("www.python.org")

    # Example of an invalid request
    conn.request("GET", "/parrot.spam")
    response = conn.getresponse()

    response.status         # 404
    response.reason         # Not Found

    data = response.read()  # This will return entire content.
    conn.close()

HEAD Request
------------
.. code-block:: python

    import http.client

    conn = http.client.HTTPSConnection("www.python.org")

    conn.request("HEAD", "/")
    response = conn.getresponse()

    response.status         # 200
    response.reason         # OK

POST Request
------------
.. code-block:: python

    import http.client
    import urllib.parse


    params = urllib.parse.urlencode({
        '@number': 12524,
        '@type': 'issue',
        '@action': 'show'
    })

    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain"
    }

    conn = http.client.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)

    response = conn.getresponse()

    response.status     # 301
    response.reason     # 'Moved Permanently'

    data = response.read()
    # b'<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>301 Moved Permanently</title>\n</head><body>\n<h1>Moved Permanently</h1>\n<p>The document has moved <a href="https://bugs.python.org/">here</a>.</p>\n<hr>\n<address>Apache/2.2.16 (Debian) Server at bugs.python.org Port 80</address>\n</body></html>\n'

    conn.close()


Assignments
===========

REST API
--------
#. Używając biblioteki standardowej w Pythonie zaciągnij informacje o repozytoriach użytkownika Django na https://github.com
#. w przeglądarce internetowej wygeneruj w swoim profilu token https://github.com/settings/tokens
#. Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``.

    .. code-block:: python

        "name": "django",
        "full_name": "django/django",

        # wyszukaj "commits_url": ???

#. Przeglądnij to repozytorium i jego listę commitów.
#. Podaj datę i opis ostatniego commita
#. Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu

:About:
    * Filename: ``http_advanced.py``
    * Lines of code to write: 50 lines
    * Estimated time of completion: 30 min

:The whys and wherefores:
    * Komunikacja HTTP (request, response)
    * Parsowanie odpowiedzi HTTP
    * Sprawdzanie stanu połączenia
    * Serializacja i parsowanie *JSON*
    * Korzystanie z API i dokumentacji
    * Regexpy
    * Używanie biblioteki standardowej i bibliotek zewnętrznych

:Hints:
    .. code-block:: rest

        https://api.github.com/

        GET /orgs/django/repos
        GET /repos/django/django/commits

    .. code-block:: console

        $ curl https://api.github.com/orgs/django/repos
        $ curl https://api.github.com/repos/django/django/commits

    .. code-block:: python

        auth = b'username:token'
        key = base64.b64encode(auth).decode("ascii")
        headers={
            'Authorization': 'Basic {key}',
            'User-Agent': 'Python HTTP',
        }

        # ...

        body = resp.read().decode()
        data = json.loads(body)
