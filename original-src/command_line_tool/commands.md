# Commands

The `mlg` tool is invoked using the format `mlg <command> [options]`
where `<command>` is one of `check`, `view`, `version`, or `help` and
the optional `[options]` a specific to the command specified.  For
any command, the `--help` option can be used to get a printout of help
info for that specific command.

## `check`

Running `mlg check` recursively checks of `.math` files in the current
working directory and prints any diagnostic messages to the console.
The type of checks performed include but are not limited to:

* Syntax errors
* Referencing a non-existent definition, theorem, resource, person, etc.
* The existence of multiple definitions, theorems, resources, people, etc.
  with the same signature
* Referencing a definition, theorem, resource, person, etc. incorrectly
  (i.e. with the wrong number or type of arguments)
* Ambiguous uses of operators

See the chapter, **Checking Mathlingua Documents** for more
information about the type of checks performed and how to fix any
errors returned.

The `mlg check` command can also be given an optional list of one or
more `.math` files.  In that case, all `.math` files in the current
working directory and any subdirectory are checked, but only diagnostic
message in the specified files are printed to the console.  This is
useful for debugging individual files.

##  `view`

As describing in the **Introduction**, Mathlingua files written using
the Mathlingua syntax, where each definition specifies how it would be
represented when written on paper, for example in a textbook or journal.

That information is used to render Mathlingua documents, and the
`mlg view` command starts a server that hosts those documents on
`localhost:8080`.  To view the documents open your browser at
`localhost:8080`.

To use a different port number, use the `--port` option.  For example,
`mlg view --port 3000` will have the documentation served on port 3000.

For more information, see the chapter **Rendering Mathlingua Documents**.

## `version`

The `mlg version` command is used to determine which version of the
Mathlingua tooling you are using.

## `help`

The `mlg help` command is used to print information describing how to
use the `mlg` command.  Each command also supports the `--help` option
to print usage information for that command, for example
`mlg check --help`.
