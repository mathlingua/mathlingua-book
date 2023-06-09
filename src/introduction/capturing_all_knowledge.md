# Capturing All Aspects of a Piece of Mathematical Knowledge

MathLingua not only allows the precise description of a mathematical statement but is designed to record all aspects of knowledge about that statement, such as what it is called when spoken, how it is written, its background and impact, who discovered it, etc.

Consider the following example (Some parts of the example have been omitted with `...` for clarity.  Full examples with follow later in this document):

```yml
[\definite.riemann.integral[x]{f[x]}:from{a}:to{b]]
Defines: S
...
Documented:
. written: "\int_{a?}^{b?} f?(x?) \: d x?"
. called: "Definite Riemann Integral of $f?(x?)$ on $[a?, b?]$"
. overview: "Precisely speaking, the Rieman Integral is ..."
. motivation: "The Rieman Integral was developed because ..."
. discovered: "@Bernhard.Riemann"
...
References:
. "$Royden.Real.Analysis.Edition2:page{23}"
```

Note that the `Documented:written:` section describes how the definite Riemann integral of a function on an interval is rendered with LaTeX.  The `Documented:called:` section, on the other hand, describes how one would describe the definite Riemann integral when spoken out loud.

The `Documented:overview` section contains a description of the Riemann Integral in a natural langugage.  In addition, the motivation behind its importance is recorded in the `Documented:motivation:` section, and a list of people that contributed to its discovery in the `Documented:discovered:` section.

Last, the `References:` section provides a list of references for further information.  As such, the MathLingua entry for the Definite Riemann Integral captures many aspects of the definition of the Definite Riemann Integral besides its formal statement.

> Note the use of `@` in `@Bernhard.Riemann` and `$` in `$Royden.Real.Analysis.Edition2:page{23}`.  These are sigils used to reference people and references.  Similarly, the sigil `\` is used to reference definitions, theorems, axioms, and conjectures.  We will learn more about these sigils later in the text.

The `Documented:written:` section is very important since it decouples the way a mathematical concept is represented on paper from the name used to reference the concept, in this case `\definite.riemann.integral[x]{f[x]}:from{a}:to{b}`.  The full reference name can be long so that it is clear what it represents, while the 'Documented:written:' section is used to "render" a statement written in Mathlingua to provide a form that matches how the concept is written on paper.

As an example, consider an example theorem (with parts omitted with `...` for clarity).

```yaml
Theorem:
...
then:
. '\definite.riemann.integral[x]{f(x)}:from{0}:to{1} = 0'
```

The MathLingua build tool `mlg` (discussed in later sections) uses the LaTeX form of `\definite.riemann.integral' in its `Documented:written:` section to render the theorem statement as:

```yaml
Theorem:
...
then:
. $\int_{0}^{1} f(x) \: dx = 0$
```

Thus, the rendered form of the statement expresses the definite Riemann integral in the way it is typically written on paper, while the original MathLingua source can be viewed to see what the statement precisely means in case of ambiguities.

To understand when such ambiguities might exist, suppose the rendered form of a MathLingua statement contained the rendered item:

\\[ \int f \\]

What does that text represent?  It could mean the Riemann integral, Lebesgue integral, Daniel integral, or perhaps something entirely different.  However, the original source of the MathLingua statement would be explicit.  Perhaps it would say `\riemann.integral{f}` or `\lebesgue.integral{f}` to be unambiguous.
