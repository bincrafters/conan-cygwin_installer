#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from conans.errors import ConanException
import os


class TestPackage(ConanFile):
    default_options = "cygwin_installer:exclude_files=*/link.exe"

    def test(self):
        bash = tools.which("bash.exe")

        if bash:
            self.output.info("using bash.exe from: " + bash)
        else:
            raise ConanException("No instance of bash.exe could be found on %PATH%")

        self.run('bash.exe -c ^"uname -a^"')
        self.run('bash.exe -c ^"test -L /etc/networks^"')
        self.run('bash.exe -c ^"! test -f /bin/link"')
