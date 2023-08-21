# Project Structure

Mathlingua files are text files encoded in UTF-8 that end with a `.math` extension.

If you open a terminal and execute the `mlg` tool, it will process all files with a
`.math` extension recursively in the current working direction ignoring any files or
directories that start with a `.`.

> Ignoring files and directories starting with a `.` means the `.git` directory used
by `git` to store information, and other similar directories are automatically ignored.
