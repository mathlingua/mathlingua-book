## Relationship to Other Mathematical Languages

MathLingua is distinct from representational languages like LaTeX or MathML,
transfer languages like OMDoc, evaluative technologies like Sage, MatLab,
and Mathematica and proof languages/theorem proving technologies like Coq,
Lean, etc.

Representational languages are used to describe what mathematical statements
look like when rendered on a screen or printed on a piece of paper but do not
describe the meaning of the statements.  MathLingua is designed to describe
such meaning.

Transfer languages are used to encode mathematical knowledge in a way that can
be stored on a hard drive or transferred between systems.  OMDoc is an example
of such a language, but uses XML as the underlying technology and is very
verbose such that it is not designed to be directly written by hand.  MathLingua,
on the other hand, is designed to be concise and precise and can be easily read
in its raw form and written by hand.

Evaluative systems like Sage, MatLab, and Mathematica are designed to calculate
mathematical expressions.  They are good, for example, at evaluating the definite
integral of a particular function.  MathLingua, on the other hand, is designed to
describe mathematical knowledge, such as the fundamental theorem of calculus,
rather than perform calculations.

Last, proof languages and technologies are designed to describe mathematical
statements in a precise format using a fixed logical framework to allow the proofs
of statements to be automatically verified by computers.

Such systems have a very steep learning code, and require mathematical statements
to be described to using a particular framework.

One common framework used in proof assistants such as Coq and Lean is the Calculus
of Constructions based on Martin-Löf type theory.  This framework follows
intuitionistic mathematics that, roughly speaking, requires constructive proofs
of theorems and mathematical entities.

Another framework is Simple Type Theory or Higher Order Logic that is used by proof
assistants such as Isabelle and HOL and HOL Light.  This framework is an extension
of second order logic.

Mathlingua uses a type theory inspired by Simple Type Theory with some extensions,
but is designed to describe mathematical objects, not describe proofs.  That is,
proofs are written in natural language (although future version of Mathlingua may
provide a proof language),

Moreover, the purpose of Mathlingua is enable one to read and write mathematical
statements in a way that is very similar to the way they are written in mathematical
textbooks and journals without having to know any technical details of type theory.

That is, Mathlingua is designed so that you do not need to know type theory to read,
write, or understand statements written in Mathlingua.
