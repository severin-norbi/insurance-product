# insurance-product

This demo package shows simple usage of Django and Django Rest Framework to
set up a system with dynamic schemas.

Django Rest Framework is chosen as the main API tool due to it's popularity
and completeness, and also because it has tools that help you test the API
through the browser, which helps in debugging and development.

The database chemas are:

## RiskType

This is the fundamental dynamic schema, each RiskType has a set of fields
that can be configured on a per RiskType basis.

## RiskTypeField

Each field, with titles and descriptions and a type. The field types
available are currently hardcoded. If the choice gets more complex there
should probably be a type registry and type classes, but that also depends on
the form library used, some form libraries have classes like that alredy.

## EnumOption

Of the types of fields, the "enum" type is a choice between a fixed set
of values, those choices are stored in the EnumOption field.

This database layout makes is quick and easy to get all the fields for one
RiskType, including the choices in the EnumField.
