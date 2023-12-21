### The Formulation Language

#### Forms

##### Identifiers
      * Describe that underscores can be used
      * Describe stropping is done with ""
      * Describe that backtick is used for quote
##### Tuples
      * Describe that `(x)` and `x` are equivalent and
        `f((x,y,z))` and
        `f(x, y, z)` are equivalent
##### Fixed sets
##### Conditional sets
      * Describe variadic args
##### Mappings
      * Describe how `f(x)` means the structure in structural view
        and value otherwise
      * Describe variadic args
   
    * Describe how ordinal calls can be used `x{i}` and `f(x){i}`.
    * Details
      * Forms can be nested
      * Forms describe structure

#### Commands
    * Examples
    * Usage
    * Directed `@[]`
    * Variadic
    * Signatures
      * Only allows for overloading in directions but whenever any
        part of the
        command is variadic, the whole this is treated as variadic
         and
        there can only be one variadic form
    * Describe how `[]{}` and `[]{:}` is sugar for mapping and
      conditional
      set inputs
  * `is`, `as`, `extends`
    * just a brief intro
  * `:=`
    * Describe how identifiers can only be set once
  * `=`
    * Describe that it is built-in but has no meaning
  * `:=>`
    * Describe it is used for aliases that match the type of the
      input
  * `:->`
    * Describe it is used for is-like forms and the rules around
      it
      
#### Commands

Commands are of the form `\(name.)*name([]?{}(@name[])?)?(:name[]?{}(@name[])?)*(())?`.  For example, the following are valid:

```yaml
\abc
\f{x}
\some.name:abc{x, y}:xyz{a, b}
\some.name{1, 2}:abc{x, y}:xyz{a, b}
\some.name{1, 2}:abc{x, y}:xyz{a, b}(a, b)
```

In particular, if a `{}` accepts exactly one argument, and that argument is a mapping or conditional set, then the `{}` can be suffixed with `@name[vars]` where `name` is optional and can be any name and `vars` is one or more vars from the mapping or conditional set:

```yaml
\int[x, y]{x^2 + y^2}@d[x]
\int[x, y]{x^2 + y^2}@d[x, y]
\int[x, y]{x^2 + y^2}@d[y, x]
\something[x,y]{x | x > y}@[x]
\something[u(x), v(x)]{u(x)^2 + v(x)^2}@[u(x)]
\some[x]{x}@[x]
```


#### Literals

Mathlingua supports the following literal forms that describe the structure of items:

```yaml
(a, b, c)       specifies tuples
{a, b, c}       specifies a fixed set-like item
[a,b]{(a, b) | ...}  specifies a conditional set-like item
f(x, y)         specifies a mapping-like item
X               specifies a name
```

that have the corresponding literal expression forms:

```yaml
(a, b, c)
{a, b, c}
[a,b]{(a, b) | a is \something ; a > 0}
x => x + 1
(x, y) => x + y
X
```

**Note:** Literals forms can have any other literal form for placeholder vars (for example params in mapping-like and conditional set-like items).  For example:

```yaml
f(x, y)
f(u(x), v(x))
f({a, b, c})
f((a,b), (c,d))
[u(x), v(x)]{(u(x), v(x)) | u(x) + v(x) > x}
```

However, a single tuple `(x)` is the same as `x`.  As such, `f((a, b))` is the same as `f(a, b)`.

**Note:** Command arguments in curly parens support a short form for literals:

That is:

```yaml
\some.command[x,y]{x^2 + y^2}
```

is equivalent to:

```yaml
\some.command{(x, y) => x^2 + y^2}
```

and

```yaml
\some.command[x,y]{(x, y) | x > 0 ; y > 0}
```

is equivalent to:

```yaml
\some.command{[x,y]{(x, y) | x > 0 ; y > 0}}
```

**Note:** If a literal is supplied to a command, the `when:` section specifies what is *assumed* holds for the literal instead of verifying the input.

#### Variable Shadowing

Variables cannot shadow other variables within an entity except in one instance: Placeholder variables can be shadowed as a non-placeholder variable.

For example,

```yaml
[\bounded.function:by{M}]
Defines: f(x)
...
satisfies:
. forAll: x
  then: 'f(x) <= M'
```

On the `Defines:` line the `x` is a placeholder var and the `x` on the `forAll` line is a non-placeholder var.

      
      
#### Operators
    * Order of operations
    * General prefix, postfix, infix
    * Enclosed (`[G.*]` and `[\[a.b.c].*]`)
    * `:` for resolution
#### Built in types
    * `[[statement]]`, `[[spec]]`, `[[value]]`, `[[kind]]`
    * [[statement|spec|value|kind]]
####  Specs vs clauses

### The Structural Language
  * Guiding principles
    * Structural language is fixed and formulation language is
      fluid
    * Indentation based with dot space for arguments
####  Building blocks:

```yaml
not:  Clause
```


```yaml
allOf:  Clause+
```


```yaml
anyOf:  Clause+
```


```yaml
oneOf:  Clause+
```


```yaml
exists:    Target+
where?:    Spec+
suchThat:  Clause+
```


```yaml
existsUnique:  Target+
where?:        Spec+
suchThat:      Clause+
```


```yaml
forAll:     Target+
where?:     Spec+
suchThat?:  Clause+
then:       Clause+
```


```yaml
if:    Clause+
then:  Clause+
```


```yaml
iff:   Clause+
then:  Clause+
```


```yaml
piecewise:
(if:         Clause+
 then:       Clause+)+
else?:       Clause+
```


```yaml
when:  Spec+
then:  Clause+
```


```yaml
given:      Target+
where?:     Spec+
suchThat?:  Clause+
then:       Clause+
```


#### Common aspects
    * `[ids]`
      * MetaIds
      * Documented
        * describe each item
      * References
        * brief overview with reference to the References section
      * Aliases
      * Justification

##### Labels

Labels can contain any text, `\[some.signature]` or `\[some.operator]/` specifies an entire definition or result and `\[some.signature]::[some label]` or `\[some.operator]/::[some label]` refers to a label inside of a definition or result.


##### Aliases Items

An alias is used to provide a shortened way to describe an operation.  For example, `a * b :=> a \real.*/ b` specifies that `*` represents real multiplication.

```yaml
alias:       Alias
written?:    Text
```

###### Provides Items

Provides items are used to describe the operations or members provided by a defined entity.  For example, items in a group provide a `*` operation and provides an `e` member that represents the identity of the group.

```yaml
symbol:    Alias
written?:  Text
```

```yaml
connection:
to:          Target
using?:      Target+
means:       Spec
signifies?:  Spec
viewable?:
through?:    Expression
```


###### Documented Items

Documented items are used to document parts of a mathematical entity such as how it is written in text or spoken aloud, a overview of the item, and informal description, its history, etc.

```yaml
written:  Text
```

```yaml
called:  Text
```

```yaml
writing:  Target
as:       Text
```

```yaml
overview:  Text
```

```yaml
motivation:  Text
```

```yaml
history:  Text
```

```yaml
example:  Text+
```

```yaml
related:  Text+
```

```yaml
discoverer:  Author+
```

```yaml
note:  (Text|describing:)+
```


```yaml
describing:  Text
content:     Text
```


###### References Items

References are used in items to specify the justification for different labeled parts of the item.

```yaml
label:    Text
by:       Text|Signature
comment:  Text
```

```yaml
by:       Text|Signature
comment:  Text
```

###### Metadata Items

```yaml
id:  Text
```

#### Definitions
##### Declares
      * Describe this is like abstract type
      * Describe how to assign symbols
      * Describe how to assign connections
##### Defines
      * Describe this is like concrete type
      * Describe how to assign symbols
      * Describe how to assign connections
      * Describe `generalizes:`

##### Definitions

A `Describes:` item is used to define an abstract mathematical entity.

```yaml
[\...]
Describes:    Target
with?:        Target+
using?:       Target+
when?:        Spec+
suchThat?:    Clause+
extends?:     Spec+
satisfies?:   Clause+
Provides?:    ProvidedItem+
Justified?:   JustifiedItem+
Documented?:  DocumentedItem+
References?:  ReferencesItem+
Aliases?:     AliasesItem+
Metadata?:    MetadataItem+
```

A `Defines:` item is used to define a concrete mathematical entity.


```yaml
[\...]
Defines:      Target
with?:        Target+
using?:       Target+
when?:        Spec+
suchThat?:    Clause+
generalizes?: Formulation[Signature]+
means?:       Spec
specifies:    Clause+
Provides?:    ProvidesItem+
Justified?:   JustifiedItem+
Documented?:  DocumentedItem+
References?:  ReferencesItem+
Aliases?:     AliasesItem+
Metadata?:    MetadataItem+
```

A `States:` item is used to describe the relationship between two mathematical entities.

```yaml
[\...]
States:
with?:        Target+
using?:       Target+
when?:        Spec+
suchThat?:    Clause+
that?:        Spec+
satisfies?:   Clause+
Documented?:  DocumentedItem+
Justified?:   JustifiedItem+
References?:  ReferencesItem+
Aliases?:     AliasesItem+
Metadata?:    MetadataItem+
```


#### Results

An `Axiom:` item describes a mathematical result that assumed to be true.

```yaml
[\...]?
Axiom:
given?:       Target+
where?:       Spec+
if|iff?:      Clause+
then:         Clause+
Documented?:  DocumentedItem+
References?:  ReferencesItem+
Aliases?:     AliasesItem+
Metadata?:    MetadataItem+
```

A `Conjecture:` item is used to describe a mathematical result that is thought to be true but no proof of the result exists.

```yaml
[\...]?
Conjecture:
given?:       Target+
where?:       Spec+
if|iff?:      Clause+
then:         Clause+
Documented?:  DocumentedItem+
References?:  ReferencesItem+
Aliases?:     AliasesItem+
Metadata?:    MetadataItem+
```

A `Theorem:` item is used to describe a mathematical result that has a proof.

```yaml
[\...]?
Theorem:
given?:       Target+
where?:       Spec+
if|iff?:      Clause+
then:         Clause+
Proof?:       (Proof:|Text)
Documented?:  DocumentedItem+
References?:  ReferencesItem+
Aliases?:     AliasesItem+
Metadata?:    MetadataItem+
```

A `Proof:` item is used to describe a proof for a mathematical theorem.

```yaml
[\...]?
Proof:
of:           Text
content:      Text
References?:  ReferencesItem+
Metadata?:    MetadataItem+
```


An item that specifies the proof of a theorem.

> THIS WAS DUPLICATED: DETERMINE WHICH ONE IS CORRECT <

```yaml
[\...]
Proof:
of: TextItem
content: TextItem
References?:  ReferencesItem+
```



#### Resources

A resource is used to describe a book, article, website, etc.

```yaml
[$...]
Resource: ResourceItem+
```


##### Resource Items

```yaml
title: Text
```

```yaml
author: Person+
```

```yaml
offset: Text
```

```yaml
url: Text
```

```yaml
homepage:  Text
```

```yaml
type: Text
```

```yaml
edition:  Text
```

```yaml
editor:  Text+
```

```yaml
institution:  Text+
```

```yaml
journal:  Text+
```

```yaml
publisher: Text+
```

```yaml
volume:  Text
```

```yaml
month:  Text
```

```yaml
year:  Text
```

```yaml
description:  Text
```


#### Specify

A specify item is used to describe how number literal should be viewed.  For example `2` is an integer and `2.5` is a real number.

```yaml
Specify:  SpecifyItem+
```

##### Specify Items

```yaml
positive:
int:
is:        Signature
```

```yaml
negative:
int:
is:        Signature
```

```yaml
zero:
is:    Signature
```

```yaml
positive:
decimal:
is:        Signature
```

```yaml
negative:
decimal:
is:        Signature
```


#### Person

A person item is used to describe a person such as an author.

```yaml
[@...]
Person:
. name: Text+
. biography: Text
```

#### Topic

A topic is used to describe the general area of mathematics such as Real Analysis.

```yaml
[#...]
Topic:
content:      Text
References?:  ReferencesItem+
Metadata?:    MetadataItem+
```


## Rendering Mathlingua Documents
  * Describe how functions, tuples, etc. are rendered
  * Describe how `called:`, `written:`, and `writing:` are used
  * Describe purpose of separating description with rendering
  * Pretty printing
    * Describe how alpha, beta, etc. are automatically rendered as greek letters
    * Describe how `a_1` and `a1` are valid identifiers and they are rendered the same

## The Type System
  * Flow based typing with something similar to intersection types
  * Describe how `is` works and how types are a collection of  
    signatures
  * Describe how `extends` works
  * Describe how every name must share a common ancestor type
  * Describe how `f(x)`, `f`, and `x` are all different names
  * Describe relation to simple type theory

## Symbol Resolution
  * Describe how operators and commands are resolved
  * Describe how `:->` is used during spec resolution
  * Describe how names are resolved (looking in local scope, then global, and then `Specify:`)

## Checking Mathlingua Documents
  * Guiding principles
    * Describe the cost/benefit tradeoff justifying why the
      checker is
      design the way it is
  * Items that are checked
    * *todo list them all here*
  * Items that are not checked

## Project Status

| Feature                               | Parser Support | `mlg check` Support |
|:--------------------------------------|:---------------|---------------------|
| Name forms                            |  x             |                     |
| Tuple forms                           |  x             |                     |
| Mapping forms                         |  x             |                     |
| Set forms                             |  x             |                     |
| Tuple literals                        |  x             |                     |
| Mapping literals                      |  x             |                     |
| Set literals                          |  x             |                     |
| Commands without direction            |  x             |                     |
| Commands with direction               |  x             |                     |
| `[]{}` function argument sugar        |  x             |                     |
| `[]{|}` set argument sugar            |  x             |                     |
| Meta types i.e. `[[statement]]`       |  x             |                     |
| Regular prefix operators              |  x             |                     |
| Regular postfix operators             |  x             |                     |
| Regular infix operators               |  x             |                     |
| Enclosed prefix member operators      |  x             |                     |
| Enclosed postfix member operators     |  x             |                     |
| Enclosed infix member operators       |  x             |                     |
| Enclosed type-level prefix operators  |                |                     |
| Enclosed type-level postfix operators |                |                     |
| Enclosed type-level infix operators   |                |                     |
| Group labels                          |  x             |                     |
| Inline labels                         |                |                     |
| Signatures for casting                |  x             |                     |
| Signatures with labels for references |  x             |                     |
| `is` syntax                           |  x             |                     |
| `as` syntax                           |  x             |                     |
| `extends` syntax                      |  x             |                     |
