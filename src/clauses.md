# Clauses


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

