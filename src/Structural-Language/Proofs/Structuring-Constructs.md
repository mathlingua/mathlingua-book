# Structuring Constructs


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

