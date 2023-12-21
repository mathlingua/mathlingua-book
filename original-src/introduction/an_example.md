## An Example

To get a feel for the MathLingua language, consider the
following theorem:

```yaml
Theorem:
given: a, b
where: 'a, b is \integer'
then:
. exists: q, r
  where: 'q, r is \integer'
  suchThat:
  . '0 <= r'
  . 'r < b'
  . 'a = b * q + r'
```

It states that given two integers `a` and `b` then there
exists integers `q` and `r` with `0 <= r < b` such that
`a = b*q + r`.

Notice that MathLingua uses indendation to describe the
structure of a piece of mathematical knowledge with elements
at the same indentation consisting of a single unit.

That is, in the example above, `Theorem:given:where:then:`
constitutes one unit and `exists:where:suchThat:` constitues
another unit.  The first describes the overal structure of the
theorem while the second describes the structure of statement
of the existence of a particular mathematical entity with some
properties.

These text elements are part of MathLingua's structural sublanguage
that describes the structure of the theorem. The text in single
quotes, on the other hand, is written in MathLingua's formulation
sublanguage and describes the details of the theorem.

Next notice that if the theorem is read out loud, left to right,
from top to bottom, it sounds very similar to how the theorem could
be written in english in a textbook.

MathLingua is designed to have the same level of formality as, and
a similar read to, the way mathematics is described in textbooks while
have a structure that allows the content to be discoverable.

The goal of MathLingua is that anyone that can read and understand
mathematical definitions, theorems, axioms, and conjectures can easily
learn to read mathematical knowledge written in MathLingua.  However,
compared to mathematical knowledge written in natural languages like
english, MathLingua provides consistency, conciseness, and precision.
