# Overview


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

