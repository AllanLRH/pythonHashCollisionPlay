# Playing around with Python hash collisions

Investigate how Python handles hsh collisions in sets.

As [this Stackoverflow answer](https://stackoverflow.com/a/2159241/1623829) states, python uses the `==` operator (the `__eq__`-method) to resolve hash collitions.
