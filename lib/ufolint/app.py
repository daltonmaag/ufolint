#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ====================================================
# Copyright 2017 Christopher Simpkins
# MIT License
# ====================================================

import sys

from commandlines import Command
from standardstreams import stdout, stderr

from ufolint.settings import HELP, VERSION, USAGE
from ufolint.controllers.runner import MainRunner


def main():
    c = Command()

    if c.does_not_validate_missing_args():
        stderr("[ufolint] ERROR: Please include the appropriate arguments with your command.")
        sys.exit(1)

    if c.is_help_request():
        stdout(HELP)
        sys.exit(0)
    elif c.is_version_request():
        stdout(VERSION)
        sys.exit(0)
    elif c.is_usage_request():
        stdout(USAGE)
        sys.exit(0)

    # TODO: add support for multiple UFO file tests in same command
    hh = MainRunner(sys.argv[1])
    hh.run()


