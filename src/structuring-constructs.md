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

