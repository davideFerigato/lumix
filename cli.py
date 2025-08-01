#!/usr/bin/env python3

import argcomplete
from lumix.cli.main import run_cli

if __name__ == "__main__":
    argcomplete.autocomplete()
    run_cli()