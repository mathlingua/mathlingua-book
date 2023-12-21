
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

TODO: Add this

```yaml
partwise:
part+: <ProofItemKind>+
```

TODO: Add else?: section
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

TODO: Update this

```yaml
forContradiction: <ProofItemKind>+
```

TODO: Update this

```yaml
forInduction: <ProofItemKind>+
```

TODO: Add this

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

TODO: Add this

```yaml
sufficesToShow: <ProofItemKind>+
```

TODO: Add this

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

TODO: ADD THIS

```yaml
absurd:
```

TODO: ADD THIS

```yaml
contradiction:
```

TODO: ADD THIS

```yaml
done:
```

TODO: ADD THIS

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
"target :> latex"
"epsilon :> \varepsilon"
"a(i) :> a?_{i?}"
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

# To Delete

## Overview

TODO: REMOVE THIS

```yaml
independently:
```

