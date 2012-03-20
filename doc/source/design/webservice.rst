#########################################
Design Note: Web Services Ports and URL's
#########################################

:ref:`architecture`

Problem
=======

TigerShark exposes two web-based (HTTP) interfaces: a user-oriented, HTML-based UI,
and an RESTful web services interface. What is the relationship between these
two? What port number and URL's should be used?

Web Services generally have a unique URL. Additionally, they can have unique
port numbers. Should port numbers be used? If so, how?

Forces
======

The user interface uses simple URL's and port 80.  The "/" URL is treated as if it
was a request for ``index.html``; providing a typical user experience.

Django, generally, ignores the port number, and only processes the URL.

Django can easily handle RESTful web services.  They're just URL's with
four internal methods for GET, POST, PUT and DELETE.

This is a multi-interface application.  The Django front-end relies on the web
services.  Also, external applications rely on the web services.

Solution
========

Use Apache to listen on port 80.

-   Some requests have the media pr static URLs,
    which are handled immediately by Apache

-   Other requests have the REST URL's which go through Django.

-   All other requests are HTML URL's, which also go through Django.

Behind Apache ``mod_wsgi`` can support a number of Django instances.

Consequences
============

Secure RESTful web services don't have sessions and don't use cookies.
Instead a secure token can be provided.  Or HTTP Digest can be used.

Authentication is handled by any of a large number of authentication
middleware projects.  For examples, see http://authkit.org/,
and http://lukearno.com/projects/barrel/.

Note that the standard approach to authentication
is a 401-reply to initiate a challenge-response cycle.
If a nonce can be reused then a number of requests can be
handled before a 401 challence.

Consistent with 3rd party authentication (i.e. ForgeRock OpenAM) a series
of web services to establish a session token may also be a sensible implementation
choice.