######################################
Design Note: Persistent Data Model
######################################

:ref:`architecture`

Sepecifically, see :ref:`Database Design Alternatives`.

Problem
=======

There are several representations for X12 messages (like Claims), all of which need to be
either reconciled into a single model or mappings created among the representations.

-   As a ``Claim`` object structure.  Very hard to read and write -- requires
    complex marshalling and unmarshalling methods.  Very easy to manipulate.

-   As an ``X12Message`` structure.  Easy to read and write, since it's standardized flat
    text.  Hard to navigate and manipulate.

-   As RDBMS tables and columns.  Easy to summarize multiple messages using
    SQL techniques.  Easy to persist.  Very hard to read and write, moderately
    hard to manipulate.

Note that the 837 claims form a natural-looking class hierarchy with common features
and subclass-unique features.  A proper class hierarchy simplifies the application
programming by making use of class inheritance techniques.

Forces
======

Generic X12 structures must be used as the source and destination for 
application-specific structures like Claims or Eligibility.  It's
standardized, and readily available.

RDBMS structures must be used for persistence.  It's standardized and readily
available.  Further, simple ORM layers can bridge between a useeful object
model and a RDBMS persistence model.

There are three use cases for this structure:

-   Defining the structure in the first place.  X12 messages have 57 different
    types of segments.  Some segment types are heavily reused -- sometimes in separate
    loops, sometimes within a single loop -- leading to 100's of variations.

-   Persistence of the entire X12 message, for example, a Claim.

-   Navigation and basic get/set of elements within a segment within an instance
    of a loop.

-   Adding and removing X12 segments and loops to fundamentally alter the
    claim structure.  Adding or removing a Loop generally means that a number of
    closely-related segments are added or removed.
    
-   Synthesizing a message from scratch.

We have two external, persistent representations of claims: X12 Text and RDBMS.
We must map between both external representations using a common internal model --
either at the ``X12Message`` level or at the application level (e.g. ``Claim``).

-   **X12Message**.  In this case, each individual "attribute" is an
    X12 element, accessible via an XPath-like query that navigates through the X12 structure
    to the requested attribute.

    -   Definition.  This comes from the ``.SEF`` files and the implementation guide.
        the ``tools.convertPyX12``, ``tools.convertSEF`` applications can generate
        the entire DB schema from metadata.
        
        Any application-specific definitions must be folded in manually.

    -   Persistence.  This is problem-domain independent, and highly reusable.

    -   Navigation.

        -   Since this representation can map via Django's ORM,
            the admin pages are (in effect) generated automatically by this
            implementation.

        -   This pushes the X12/XPath navigation into the application.

    -   Structure Changes. Simply adding a Segment in the Django admin pages can
        lead to creating an incomplete Loop. Either some validation is required
        to prevent this, or some application logic is required to define the
        complete Loop and step the user through each segment required.

-   **Application-Specific, e.g. Claim**.
    In this case, each individual attribute is an actual
    object attribute.

    -   Definition.
        This would be application-specific.
        The X12 mappings, however, for marshalling and unmarshalling X12 messages must
        be folded in manually.

    -   Persistence.  Application-specific persistence adds a layer of processing between
        the X12 unmarshalling and the application-specific structure.

        -   The application operates at a level closer to the user's understanding.

        -   We have a more complex (and less transparent) two-step marshalling and unmarshalling
            of X12 text to X12 structures to usable objects (e.g., Claims or Eligibility).

    -   Navigation.  It allows the application to be defined in functional user terms, leading
        to clear terms.  

    -   Structure Changes.  If we persist at the application level, then the default Django admin
        pages would present the user's view of the object, e.g. Claim or Eligibility.

-   **Both**.  In this case, we use X12Message structures for persistence, but present
    application (i.e. Claim) structures to users.  This implies two tiers of GUI (X12-level and Claim-level).
    This also implies a manual mappping between the user-oriented view of a Claim or
    Eligbility and the X12 message view.

    -   Definition.  This comes from the ``.SEF`` files and the implementation guide.
        the ``tools.convertPyX12``, ``tools.convertSEF`` applications.

        -   We can build a Claim object from the X12Message object. This forces us
            to assure that we either use the Claim exclusively or create a two-way
            mapping between Claim data and X12 data.

        -   Define an application object as a **Facade** that uses the X12-XPath
            mappings. In this case, we don't duplicate the X12 data to make a Claim,
            instead we package the various "Claim to X12" mappings as get/set methods
            of a Claim that provide access to the underlying X12 objects. In this
            case, an application object (e.g. Claim) is just a "view" of the X12 data.

    -   Persistence.  This is done via the X12 solution, see above.

    -   Navigation.  There are two levels: X12 and Application.  This leads to building two tiers
        of GUI.  The lower level is a transparent view of the X12 message.  The higher
        level is a friendly, business-focused view of a application object like a Claim.

    -   Structure Changes.  At the X12 level, this is requires knowing the Loop structure
        so that appropriate segments can be added.  At the Claim level, some validation
        rules need to be in place to assure that attribute values are provided in a way
        that forces creation of appropriate X12 segments to create a valid loop structure.

Solution
========
 
Application class hierarchies is often essential for having user-friendly,
functional presentation in the application.

Defining a application object (e.g., Claim) that is a **Facade** over an X12
message provides the application structure without duplicating data. This
avoids duplicating data, which avoids defining  two-way mappings between
X12 and the application objects. (Note that ORM is already a two-way mapping between
RDBMS and X12 structures.)

If a Claim is a view, defined over the X12 message structure, we can define the
higher-level, Claim-oriented GUI separately from the low-level X12 GUI that is
built automatically by Django. The higher-level GUI could be more easily
customized to include Customer-specific Implmentation Guide nuances.

+-----------------+-----------------+-------------------+
|Model            |Presentation     |Access             |
+=================+=================+===================+
|Claim Structure  |Claim GUI        |**Facade** over X12|
| - Claim         |                 |                   |
| - Claim Details |                 |                   |
| - Patient       |                 |                   |
| - Provider      |                 |                   |
| - Submitter     |                 |                   |
| - Subscriber    |                 |                   |
| - Sevice Line   |                 |                   |
+-----------------+-----------------+-------------------+
|X12 Structure    |Django Admin  UI |ORM over SQL Tables|
| - Loops         |                 |                   |
| - Segment Types |                 |                   |
| - Elements      |                 |                   |
+-----------------+-----------------+-------------------+
|SQL Structure    |No GUI           |DB Access in ORM   |
| - Table per     |                 |                   |
|   Segment Type  |                 |                   |
+-----------------+-----------------+-------------------+

This leads to building two tiers of claim UI: the lower-level X12 Structure UI
is the default Django admin pages.  The higher-level Claim UI would
have to be built "by hand" to present the user with a meaningful Claim structure.

An application object model, being a **Facade** over the X12 structure would tend
to build properly persistent X12 objects in the normal course of events.

Consequences
============

We need simple-looking application class hierarchies that handle the relevant
data items, and provides the proper level of reuse. A simple class hierarchy can
provide proper polymorphism.

Each "attribute" of a claim can become a Python property. The Python property
definition binds a getter/setter pair; these both use Python navigation to locate
the element within the segment within the proper loop structure.

Note that we need to track instances correctly so that we can navigate to the
correct loop instance when a loop occurs multiple times.
