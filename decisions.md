# Mathlingua Decisions
* Let `f` be a function then `f` or `f(?)` or `f(x?)` can be used to refer to the function itself while `f(x)` refers to the output of `f` applied to `x`.
* The above is needed so that `? \.natural.+./ ?` refers to the operator itself while `x \.natural.+./ y` refers to the output of the operator.
* Otherwise, if `*` is an operator in scope then `"*"` and `? * ?` both refers to the operator itself.
* `:=` is used to define things.  Only `:=` is needed and not `:=`, `:==`, and `:-` as was previously thought because what the `:=` refers to is determined from the context.  Only `:=` is provided, to make it easier for people to write text.
* A `specifies:` or `where:` can have any `:=` except things of the form `f(x) := ...` that should be in a `satisfying:`.
* A `when:` can have a `:=` only if it is of the form `x... := y...`, `x := y`.  That is, it cannot contain `f(x) := ...` or expressions like `x := \real` or `x := 1 + \sin(y)`.
* An item of the form `f(x)` specifies a function
* An item of the form `f[x, y]` specifies that `f` is an expression that depends on the symbols `x` and `y`
* `:->` and `:=>` items are needed to specify if an alias represents a specification alias or an expression alias because it cannot be determined from context.  This is because `x is \something` can be a predicate or a type description.
* In `written:` only symbols in a `Describes:` or `Defines:` section can be referenced.  Not symbols that are inputs to the Describes or Defines.
* In IDs: The form `x{i := 1...n}`, `x...` and `x{i := 1...}` (as well as `x{(i,j) := (1,1) ... (m,n)}` etc.) specifies that `x` is variadic with index `i` or (`i,j` in the other example).  This is similar to how `f(x)` specifies `f` is functional with `x` representing the input symbol.  This form is not allowed in expressions.  The index must start at 1 and making the 1 explicit makes the form more clear and is forward facing in case I want to support other starting indices.
* In expressions: `x...` or `x{1...}` or `x{1...n}` is used to specify the sequence of values of a variadic symbol.  Thus one writes `x... := y...` or `x{1...n} := y{1...n}`.   One cannot write `x{2...(n-1)}` (i.e. use a starting index other than 1 or an ending index other than `n` in places where `:=` and `is` is used.  Though those can be used in computational places).
* The index `i` in `x{i}` cannot be specified as `i is ...`.  It is a `positiveInt` and the specification of what a `positiveInt` is in `Specify:positiveInt:` is used to determine if a symbol can be used `j` can be used in `x{j}`.
* The positiveInt symbols support using 1,2,... as starting indices and `-` to subtract from ending indices.  So one can write `x{1...(n-1)}` or `x{2...n}`.  This is used, for example to recursively define `\real.sum:of{x{i := 1...n}}`.
* Variadic symbols do not support nesting.  That is, `x{i{j}}` is not supported.  This is because I don't see a strong use case for this, but will reconsider in the future if one comes up.
* Double check this, but perhaps a positiveInt symbol can only be used in a `matching` construct and not an `if:then:else` construct since positiveInts are special symbols that the system knows has arithmetic.















