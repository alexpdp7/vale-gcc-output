# vale-gcc-output

This is just a simple wrapper for [Vale](https://github.com/errata-ai/vale).
`vale-gcc-output` converts `vale` output into a format similar to that of tools like `gcc`.
This means that `vale-gcc-output` can integrate with tools that understand that format.

## Usage

Drop the Python file somewhere in your path (e.g. `$HOME/.local/bin` in some Linux distributions, `/usr/local/bin` on macOS, etc.).
Ensure the file is executable.

Invoke the Python script.
The script should print to standard error lines like the following:

```
path/to/file:14:75: warning: warning message here
```

Editors and tools that understand `gcc` errors should understand this output.
For example, running `vale-gcc-output` from the editor, should allow you to select errors are jump to the problematic file.

## Known Working Editors

* [Kate, using the Build Plugin](https://docs.kde.org/stable5/en/kate/kate/kate-application-plugin-build.html)

  Double clicking on an error jumps to the line of the error.
  You can jump to the next/previous errors.
  You can filter warnings.
