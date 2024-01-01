# Introduction

## Overview

Mathlingua is a language specially designed to create encyclopedias of mathematical knowledge.  That is, it is created with the unique needs for recording mathematical knowledge.  Examples of such unique needs are:

* that a Hilbert space extends the concept of a vector space with additional properties, and, although it is not directly a Banach space, it can be viewed as one
* that an integer is, strictly speaking, *not* a real number, but it can be viewed as one
* that in the expression $x + n$ where $x$ is a real number an $n$ is an integer, $+$ is interpreted as *real* addition because the integer $n$ is *viewed as* a real number
* that a function can be though of abstractly as a standalone concept that is a mapping from an input to a unique output, but can also be *encoded* as a set of pairs, and thus thought of as a set if needed
* that a continuous function is an abstract concept while the real-valued function $f(x) := \sin(x)$ is a concrete example of a continuous function on $\mathbb{R}$
* that a group can be thought of as a *tuple* $G := (X, *, e)$, where a tuple-like object is different from a function like object, is different from a set-like object
* that when one says $x \in G$ where $G := (X, *, e)$ with $X$ a set that one means $x \in X$
* that $\int f$ can potentially represent the Riemann integral, Lebesgue integral, Daniel integral, etc. of a function $f$ and thus, math symbols can be ambiguous.  Mathlingua addresses this by separating the name defining a concept and how it is rendered.
* that in the expression
$$
   \int_a^b f(x) \: dx
$$
the exact symbols $a$, $b$, and $f$ are important, but the symbol $x$ can be replaced with any symbol (other than $a$, $b$, or $f$) without changing the meaning of the expression.
* that definitions and theorems expect certain types of mathematical objects as inputs.  That is, if a theorem says given a monoid $M$, one cannot use a continuous function $f$ for $M$ because a continuous function is not a monoid.  However, one could use a group $G$ because a group *is* a monoid.
* that when one says $A \subset B$ for some sets $A$ and $B$ that it is implied that also $B \supset A$.
* that in the expression $x + y * z$, where $x$, $y$, and $z$ are real numbers, the expression should be evaluated as $x + (y * z)$.
* that to describe $f$ verbally one could say that $f$ is a function from $A$ to $B$, but in writing would write $f \: : \: A \rightarrow B$.
* that if $G := (X, *, e)$ is a group and $x,y$ are elements of $G$ then the $*$ in $x * y$ refers to the $*$ in the tuple $(X, *, e)$.
* that when specifying a definition, theorem, axiom, conjecture, or proof, to remove ambiguity, it is essential to allow the *type* of each symbol used be determined.  That is, do not just write $x + n$ but specify that $x$ is real and $n$ is an integer.
* to fully record mathematical knowledge, it is important to not just record statements of definitions, theorems, etc. but also describe their history, importance, use, and how how they related to other math concepts
* in addition to definitions, theorems, etc. it is important to record information about math resources such as books, articles, etc. as well as people that discovered mathematical results

## The Need for a Recording Mathematics

There are many examples in mathematics of concepts being rediscovered.  This could be from the fact that it is often times difficult to find what has already been discovered.  This is compounded by the observation that different authors can use very different nomenclature and notation for the same concepts.

Further, as more and more mathematics is discovered, it is becoming harder and harder for any individual to follow everything new.  This is especially difficult since many discoveries may be in journals that are hard to search and require subscriptions, and thus are not accessible to most.

As a result, a standard repository of all mathematics in a clear, consistent format is needed to help this and future generations discover and record mathematics.

## Existing Math Collections

Existing collections of mathematical knowledge typically fall into two categories.  First are books, articles, journals, encyclopedias, etc. while the second are collections written in theorem proving languages such as Lean, Coq, Mizar, etc.

For the first category, different math concepts can be spread across different books or other resources.  Even for encyclopedias, nomenclature and notation can vary across the encyclopedia.

Next, these resources are written in natural language, and are thus difficult for computers to search and understand.  That is, it is not easy to make computer search capabilities to search math books, journals, and encyclopedias and find, for example, all theorems that describe when a function is measurable.

Further, mathematics written in natural language can be imprecise and difficult to read because statements can rely on context or conventions for information.  For example, a theorem might say for all $x$ and $y$ there exists an $n$ such that $x*n > y$, where it is up to the reader to infer, based on convention and the fact that the theorem is in a real analysis book, that $x$ and $y$ refer to real numbers and $n$ an integer.

Last, mathematics written in natural language do not have any automated checking of any aspects of the statements.  In particular, a statement could have a typo in a symbol name, thus using a name that is not defined anywhere or refer to a definition that doesn't exist, and it is up to manual review to catch those mistakes.

In the second category, 

-----

# Formulation Forms

## Names

```yaml
x
x?
"a b"
```

## Functions

```yaml
f(x, y)
```

## Infix Operators

```yaml
x * y
```

## Prefix Operator

```yaml
+x
```

## Suffix Operator

```yaml
x!
```

## Tuples

```yaml
(x, y)
```

## Conditional Sets

```yaml
{x | ...}
{f(x, y) | ...}
```

## Functional Literal

```yaml
x => f(x)
(x, y) => f(x, y)
```

## Conditional Set Id Form

```yaml
[x]{x | f(x)...}
```

## Colon Equals Form

```yaml
X := (a, b)
f(x) := y
```

# Formulation Expressions

## Function Expression

```yaml
f(x + y, z)
(f + g)(x)
```

## Function Literals

```yaml
x => x + 1
(x, y) => x + y
```

## Tuples

```yaml
(x + y, z)
```

## Groupings

```yaml
(x + y)
```

## Invisible Groupings

```yaml
(.x + y.)
```

## Conditional Set Expression

```yaml
[x]{(x, x+1) | x is \real ; x > 0}
[x, y]{(x + y | x is \real ; y > 0}
```

## Command Expressions

```yaml
\function:on{A}:to{B}
\a.b.c{x, y}
\a.b.c(x, y)
\a.b.c[x, y]{x + y}
\a.b.c[x, y]{x + y | x > 0 ; y < 0}
```

## Prefix Operator

```yaml
-x
```

## Postfix Operator

```yaml
x!
```

## Infix Operator

```yaml
x + y
```

## Is Expression

```yaml
x is \y
```

## Equality

```yaml
x = y
x != y
```

## Extends Expression

```yaml
x extends \y
```

## As Expression

```yaml
x as \:y
```

## Ordinal Call Expression

```yaml
x[1]
x[i[k]]
```

## Chain Expression

```yaml
(x + y).z.a.b
```

## Select From Builtin

```yaml
\\select{statement|specification}:from{x}
```

## Signatures

```yaml
\[a.b.c:d:e]
```

## Types

```yaml
\:a.b.c:x{\:a & \:b, \:c}:y{\:d}
\:continuous.function:on{\:set}:to{\:set}
(\:set & \:group) \:to:/ \:set
\:set \:to:/ \:set
```

## Type Builtin

```yaml
\\type{\:set & \:group}
```

## Formulation Builtin

```yaml
\\formulation{expression | statement}
```

## Map Builtin

```yaml
\\map{x[i]}:to{x[i] + 1}
```

## Map Else Builtin

```yaml
\\map{x[i[k]]}:to{x[i[k]] + 1}:else{0}
```

## Colon Equals Expression

```yaml
f(x) := x + 1
```

## Colon Arrow Expression

```yaml
x + y :=> x
```

## Colon Dash Arrow Expression

```yaml
x + y :-> x; y
```

## Enclosed Non-command Operator

```yaml
[.x.]
[.x.]:
:[.x.]
```

## Non-enclosed Non-command Operator

```yaml
*
++
:+
+:
```

## Infix Command Expression

```yaml
\function:on{A}:to{B}/
```

# Ids

## Command Id

```yaml
\function:on{A}:to{B}
\function:on{A}:to[x,y]{f(x,y)}@{x}
\function:on{A}:to[x,y]{f(x,y)}@d{x}
```

## Prefix Operator Id

```yaml
-x
```

## Postfix Operator Id

```yaml
x!
```

## Infix Operator Id

```yaml
x + y
```

## Infix Command Operator Id

```yaml
A \subset/ B
```

## Variadic

```yaml
x...
x[i...]
x[i...n]
x[i[j...n]]
(x[i[j...n]], y[i[j...n]])
f(x...)
f(x...)...
(x...)
(f(x...)...)
X... := (a, b, c)...
X... := {x | ...}...
X... := {f(x) | ...}...
x... := a...
x... is \a
x... extends \a
```

# Structural Language

## Overview

```yaml
Clause ::= <Text>
         | <Formulation>
         | <Spec>
         | all:
         | not:
         | anyOf:
         | oneOf:
         | equivalently:
         | exists:
         | existsUnique:
         | forAll:
         | if:
         | iff:
         | when:
         | piecewise:
         | let:
         | define:
```

## Clauses

```yaml
equivalently: <Clause>+
```


```yaml
allOf: <Clause>+
```


```yaml
anyOf: <Clause>+
```


```yaml
oneOf: <Clause>+
```


```yaml
not: <Clause>
```


```yaml
exists: <Target>+
using?: <Target>+
where?: <Spec>+
suchThat: <Clause>+
```


```yaml
existsUnique: <Target>+
using?: <Target>+
where?: <Spec>+
suchThat: <Clause>+
```


```yaml
forAll: <Target>+ 
using?: <Target>+
where?: <Spec>+
suchThat?: <Clause>+
then: <Clause>+
```

```yaml
if: <Clause>+
then: <Clause>+
```


```yaml
iff: <Clause>+
then: <Clause>+
```

```yaml
when: <Spec>
then: <Spec>
```

```yaml
piecewise:
if: <Clause>+
then: <Clause>+
elseIf?: <Clause>+
then?: <Clause>+
else?: <Clause>+
```

```yaml
let: <Target>
using?: <Target>+
where?: <Spec>+
suchThat?: <Clause>+
then: <Clause>+
```


```yaml
define: <Target>
using?: <Target>+
when?: <Spec>+
suchThat?: <Clause>+
means?: <Clause>+
as: <Clause>+
```

## Definitions

```yaml
Captures: <Formulation>+
Justified?: <JustifiedKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

```yaml
Defines: <Target>
using?: <Target>+
when?: <Spec>+
suchThat?: <Clause>+
means?: <Spec>+
specifies?: <Clause>+
Provides?: <ProvidesKind>+
Justified?: <JustifiedKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

```yaml
Describes: <Target>
using?: <Target>+
when?: <Spec>+
suchThat?: <Clause>+
extends?: <Spec>+
satisfies?: <Clause>+
Provides?: <ProvidesKind>+
Justified?: <JustifiedKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

```yaml
States:
using?: <Target>+
when?: <Spec>+
suchThat?: <Clause>+
that: <Clause>+
Justified?: <JustifiedKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

## Results

```yaml
Axiom:
given?: <Target>+
using?: <Target>+
where?: <Spec>+
if?: <Clause>+
iff?: <Clause>+
then: <Clause>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```


```yaml
Conjecture:
given?: <Target>+
using?: <Target>+
where?: <Spec>+
if?: <Clause>+
iff?: <Clause>+
then: <Clause>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```


```yaml
Corollary:
to: <Text>+
given?: <Target>+
using?: <Target>+
where?: <Spec>+
if?: <Clause>+
iff?: <Clause>+
then: <Clause>+
Proof?: <ProofItemKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

```yaml
Lemma:
for: <Text>+
given?: <Target>+
using?: <Target>+
where?: <Spec>+
if?: <Clause>+
iff?: <Clause>+
then: <Clause>+
Proof?: <ProofItemKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

```yaml
Theorem:
given?: <Target>+
using?: <Target>+
where?: <Spec>+
if?: <Clause>+
iff?: <Clause>+
then: <Clause>+
Proof?: <ProofItemKind>+
Documented?: <DocumentedKind>+
References?: <Text>+
Aliases?: <Alias>+
Writing?: <WritingTextItem>+
Id?: <IdTextItem>
```

## Resources

```yaml
Resource: <ResourceKind>+
Id?: <IdTextItem>
```

```yaml
ResourceKind ::=
```

```yaml
description: <Text>
```

```yaml
title: <Text>
```

```yaml
type: <Text>
```

```yaml
url: <Text>
```

```yaml
volume: <Text>
```

```yaml
month: <Text>
```

```yaml
offset: <Text>
```

```yaml
publisher: <Text>
```

```yaml
author: <Text>
```

```yaml
edition: <Text>
```

```yaml
editor: <Text>
```

```yaml
homepage: <Text>
```

```yaml
institution: <Text>
```

```yaml
journal: <Text>
```

```yaml
year: <Text>
```

## Configuration

```yaml
Specify: <SpecifyKind>+
Id?: <IdTextItem>
```

```yaml
SpecifyKind ::=
```

```yaml
positiveFloat:
means: <Spec>
```

```yaml
positiveInt:
means: <Spec>
```

```yaml
negativeFloat:
means: <Spec>
```

```yaml
negativeInt:
means: <Spec>
```

```yaml
zero:
means: <Spec>
```

## People

```yaml
Person: <PersonKind>+
Id?: <IdTextItem>
```

```yaml
PersonKind ::=
```

```yaml
name: <Text>+
```

```yaml
biography: <Text>
```

## Documented

```yaml
DocumentedKind ::=
```

```yaml
overview: <Text>+
```

```yaml
related: <Text>+
```

```yaml
written: <Text>+
```

```yaml
called: <Text>+
```

```yaml
writing: <Text>+
```

## Provides

```yaml
symbol: <Alias>
written?: <Text>+
```

```yaml
view:
as: <Target>
using?: <Target>+
where?: <Spec>+
through?: <Formulation>
signifies?: <Formulation>
```

```yaml
encoding:
as: <Target>
using?: <Target>+
where?: <Spec>+
through?: <Formulation>
```

## Justified

```yaml
JustifiedKind ::=
```

```yaml
by: <Text>+
```

```yaml
label: <Text>
by: <Text>+
```

## Proofs

### Structuring Constructs

```yaml
ProofItemKind ::=
```

```yaml
block: <ProofItemKind>+
```

TODO: Add this

```yaml
remark: <text>
```

```yaml
partwise:
part+: <ProofItemKind>+
```

```yaml
casewise:
case+: <ProofItemKind>+
else?: <ProofItemKind>+
```

```yaml
stepwise: <ProofItemKind>+
```

```yaml
withoutLossOfGenerality: <ProofItemKind>+
```

```yaml
forContradiction: <ProofItemKind>+
```

```yaml
forInduction: <ProofItemKind>+
```

```yaml
forContrapositive: <ProofItemKind>+
```

### Introductory Constructs

```yaml
claim:
given?: <Target>+
using?: <Target>+
where?: <Spec>+
if?: <Clause>+
iff?: <Clause>+
then: <Clause>+
Proof?: <ProofItemKind>+
```

```yaml
suppose: <ProofItemKind>+
then: <ProofItemKind>+
```

```yaml
sufficesToShow: <ProofItemKind>+
```

```yaml
toShow: <ProofItemKind>+
observe: <ProofItemKind>+
```

### Symbol Introduction Constructs

```yaml
exists: <Target>+
using?: <Target>+
where?: <Spec>+
suchThat: <ProofItemKind>+
```

```yaml
existsUnique: <Target>+
using?: <Target>+
where?: <Spec>+
suchThat: <ProofItemKind>+
```

```yaml
forAll: <Target>+
using?: <Target>+
where?: <Spec>+
suchThat?: <Clause>+
then: <ProofItemKind>+
```

```yaml
let: <Target>
using?: <Target>+
where?: <Spec>+
suchThat?: <Clause>+
then: <ProofItemKind>+
```

### Reasoning Constructs

```yaml
because: <ProofItemKind>+
then: <ProofItemKind>+
```

```yaml
by: <Text>+
because?: <ProofItemKind>+
then: <ProofItemKind>+
```

### Flow of Thought Constructs

```yaml
hence: <ProofItemKind>+
by?: <Text>+
because?: <ProofItemKind>+
```

```yaml
next: <ProofItemKind>+
by?: <Text>+
because?: <ProofItemKind>+
```

```yaml
notice: <ProofItemKind>+
by?: <Text>+
because?: <ProofItemKind>+
```

```yaml
then: <ProofItemKind>+
by?: <Text>+
because?: <ProofItemKind>+
```

```yaml
therefore: <ProofItemKind>+
by?: <Text>+
because?: <ProofItemKind>+
```

```yaml
thus: <ProofItemKind>+
by?: <Text>+
because: <ProofItemKind>+
```

### Logical Constructs

```yaml
oneOf: <ProofItemKind>+
```

```yaml
allOf: <ProofItemKind>+
```

```yaml
anyOf: <ProofItemKind>+
```

```yaml
equivalently: <ProofItemKind>+
```

```yaml
if: <ProofItemKind>+
then: <ProofItemKind>+
```

```yaml
iff: <ProofItemKind>+
then: <ProofItemKind>+
```

```yaml
not: <ProofItemKind>
```

### Terminating Constructs

```yaml
absurd:
```

```yaml
contradiction:
```

```yaml
done:
```

```yaml
qed:
```

# Labels

## Overview

```yaml
\[a.b.c:d:e]::(some.label)
\(some.label)
```

# Writing

## Overview

```yaml
"target as latex"
"epsilon as \varepsilon"
"a(i) as a?_{i?}"
```
writing: uses the same replacement rules as written:

# Written

## Overview

```yaml
x?
x+?
x-?
x=?
x?{... suffix}
x?{prefix ...}
x?{... infix ...}
x? is the same as x-?
```

# Sigils

# Order of operations

# Type checking

# Symbol Resolution

# Encoded As

# Viewed As
