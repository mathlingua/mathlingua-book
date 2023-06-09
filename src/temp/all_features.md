# All Features

* `mlg` command
  * view
  * version
  * check
  * help
* command and infix command format
  * use of . and :
* id forms
  * infix commands
  * non-infix commands
    * args:
      * x
      * f(...)
      * () => ...
      * []{... | ...}
      * (?, ?, ?)
      * :=
    * var-args:
      * x...
      * f(...)
      * f()...
      * ()...
      * []{}...
      * that ()... and []{}... needs to be of the form `X... := ...`
  * []{... | ...} shortcuts
  * []{...} to () => {...} shortcuts
  * directed @[...]
  * difference between {} and () in commands
    * a command with a () at the end is for a function
    * if a command has () in the id it must be a function form (but not the other way around)
* coercion
  * how names can represent anything
  * non-forms cannot represent other non-name forms without a conversion specified in view:
* use of x? in formulations (represents a variable) (also can use ?)
* values
  * x
  * numbers (int and float)
  * f(x)
  * () => ...
  * []{... | ...}
  * (?, ?, ?)
  * x{...} <- ordinal calls
  * special operators (*, +, -)
  * infix commands `x \op/ y`
  * enclosed infix `x [G.*] y`
  * operator order of operations (precedence and associativity)
  * chains `A.b.c`
  * `x as X`
* ordinals
  * x{i...}
  * x{i...n}
  * x{(i,j)...(m,n)}
  * how 'x...' is interpreted (in particular, the expected type are used)
    * i.e. `x...` that expects specs will use the specs and `x...` where
      clauses are expected will use the clauses
  * how `a... := b...` is interpreted (but `a, b := c, d` is not allowed)
  * how `a... = b...` is interpreted (but `a, b = c, d` is not allowed)
* broadcasting
  * `a, b, c is A`
  * `a, b, c extends A`
  * `a, b, c [in]: A`
  * but `a, b is A, B` is not allowed
* how type checking works
  * spec aliases act like type operators
  * `is` specifies what is and what is expected depending on the context
  * how checking if `x is y` looks up the extends chain
  * for checking conforming to a definition, first the definition is "resolved" and then verified
  * definitions must be fully specified
    * if a definition is a Captures: then the first matching item is used
* what link: and view: describe
  * how view: is used to specify something can be treated as something else
* rendering
  * difference of called: and written:
  * when called: vs written: is used (precedence)
  * what does exprssed: do
  * how rendering a Captures: works
* scoping
  * variable shadowing
  * placeholder vs non-placeholder
  * how non-placeholder can shadow placeholder but not the other way around
  * how placeholders can be used multiple times (i.e. f(x) and g(x))
* directed operators, aliases, spec aliases
  * +: vs :+ vs + (but :+: is not allowed)
* aliases
  * how they are local and applied first before resolution
  * how variables can reference outer variables
* resolution
  * how spec aliases work
  * how spec aliases have ; on the right-hand-side
  * how spec aliases can only describe variables on the right hand side
  * how spec aliases can reference outer scoped names
  * how spec aliases can only have an `is` or another spec alias on the right hand side
  * how value aliases are resolved
  * how value aliases always refer to outer scope variables
  * G.x aliases must use outer scope variable (G in this case)
  * how value aliases can be set on Defines: or Describes: to be specific for particular
    concrete types
* extends, means
  * how each identifier can be specified (x is ..., y is ...)
* when/where vs suchThat
  * how `is` and spec aliases can only go in when/where
  * how := and other claueses can only go in suchThat (since := requires evaluation)
  * how `when/where` is the only thing used to verify type conformance
* how `extends` is used to loop back on a definition
* text
  * how text blocks and text elements use commonmark
  * how [[$a.b.c]] and [[\a.b.c:for{x, y}]]{x := ...}{y := ...} is used to reference items
  * how the double square brackets part need to be id forms where values are specified in {...}
    after the [[]]
* concreate vs abstract types (defines vs describes)
* connections between things (states)
* specify
  * how number literals types are resolved (int, float, ...)
* how describes, defines content in specifies/satisfies is not used for type analysis
* how f(x) := ... specifies a function value while f := ... specifies the function itself
* expression vs structural context
* stropping in expression context but not needed in structural context
* nested structural forms X := (y := (a, b, [c]{c | ...}))
* how left hand side of := must be function or name
* meta types (parametric polymorphism)
* sigils `\\`, `$`, and `@`
* labels
  * how labels are defined in an item
    * above groups
    * to the right of formulations
  * how labels are references
  * how textblocks have labels ::a.b.c to reference in overview: etc.
* signatures
  * describe their syntax and how they are used
* documented:
  * describe the purpose of each thing
* Id:
  * how it unique identifies each item
  * how it is auto generated
* text items
  * some places expect only a signature or a number
  * others allow arbitrary commonmark
* formulations
  * describe that backtick is an identifier character in addition to letters and numbers
* how name scoping works (i.e. a `0` define in a local scope takes precedence over global scope)
* how commands are all at global level but the `.` in `\a.b.c` allows for grouping
  * explain how `<adjective>.<noun>:<property>(<topic>)` is a good approach
    (i.e. `\continuous.function:inMetricSpace{S}`)
