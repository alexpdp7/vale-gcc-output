#!/usr/bin/env python3
import json
import subprocess
import sys


def print_error(file, line, column, severity, msg):
    print(f"{file}:{line}:{column}: {severity}: {msg}", file=sys.stderr)


def main():
    process = subprocess.run(["vale", "--output=JSON", "."], stdout=subprocess.PIPE)
    result = json.loads(process.stdout)
    for file, actions in result.items():
        for action in actions:
            line = action["Line"]
            column = action["Span"][0]
            severity = action["Severity"]
            msg = action["Message"]
            print_error(file, line, column, severity, msg)


if __name__ == "__main__":
    main()
