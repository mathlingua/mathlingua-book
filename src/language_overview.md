# The Language Overview

The Mathlingua language consists of two parts, an outer structural language and an inner formulation language.

Again consider the example:

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
  . 'a = b*q + r'
Documented:
. name:
  . "The Division Algorithm"
  . "[es]División Euclídea"
```

The structural language provides structure to the mathematical statement and uses indentation to connect related items and `. ` for arguments.

In the above example,

```yaml
Theorem:
given:
where:
then:
Documented:
```

is one structural unit while

```yaml
exists:
where:
suchThat:
```

is another structural unit and

```yaml
name:
```

is another structural unit.

Each structural unit is called a *group* and each part of a *group* is called a *section*.  For example, the group `exists:where:suchThat:` has three groups, `exists:`, `where:` and `suchThat:`.  Notice that a `:` follows a group name which is followed by one or more arguments.

Multiple arguments can be specified on the same line, as long as they are not groups themselves, and are separated by commas.

For example, in `exists: q, r` the group has arguments `q` and `r`.  These arguments could also be specified on their own lines (preceded with `. `) either as:

```yaml
exists: q
. r
```

or

```yaml
exists:
. q
. r
```

However, if an argument to a section is a group, it must be specified on its own line.  That is why in:

```yaml
then:
. exists: q, r
  where: 'q, r is \integer'
  suchThat:
  . '0 <= r'
  . 'r < b'
  . 'a = b*q + r
```

The `exists:where:suchThat:` is on a new line preceded by a `. `.

Notice that the `q` and `r` in `exists: q, r` are not surrounded by single quotes while `where: 'q, r is \integer'` has an argument in single quotes.

Forms (such as `q`, `r`, `f(x)`, `(X, *)`, `{(x, y) | ...}`) can be specified in the structural language in sections that introduce names (such as `exists:`, `forAll:`, `given:` etc.) and they introduce a name as well as the shape of that name.

For example, `q` specifies a single opaque entity, `f(x)` represents a function-like object with `x` representing the input, `(X, *)` representing a tuple like object, and `{(x, y) | ...}` a set like object of tuples.

Because the structural language specifies the form of names introduced, operators like `*` in `(X, *)` can be specified and are treated as names, not as an operation acting on inputs (such as `1 * 2`).

Text in single quotes, on the other hand, such as `'q, r is \integer'` is written using the formulation language that describes computations and statements.

That is, `q, r is \integer` is a statement that `q` and `r` are integers (The `is` keyword will be discussed in more detail later).

In the formulation language any sequence of characters (with some caveats discussed later) from:

```
~ ! @ # $ % ^ & * - _ + = | / < >
```

are treated as operators.  Thus `1 + 2` is interpreted as an operator `+` with arguments `1` and `2`.  Similarly, `1 @& 2` is interpreted as an operator `@&` with the same arguments.

*Stropping* is used to represent an operator itself.  That is, `"+"` (note the double quotes) represents the name of the operator `+` itself.

Thus, the structural language describes the structure of a piece of mathematical knowledge while the formulation language describes computations and statements.

Last, notice the section:

```yaml
Documented:
. name:
  . "The Division Algorithm"
  . "[es]División Euclídea"
```

with arguments in double quotes, `"The Division Algorithm"` and `"[es]División Euclídea"`.

Text in double quotes are text-items, and represent textual information.  This text is UTF-8 encoded and by default is interpreted as English.

If the text is in another language, the text can start with an ISO 639-1 language code in a square braces to specify the language.

For example in `"[es]División Euclídea"` the `[es]` specifies that the text is in Spanish.
