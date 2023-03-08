#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conan import ConanFile

class TestPackage(ConanFile):
    settings = "os", "arch"
    generators = "VirtualBuildEnv"
    test_type = "explicit"

    def build_requirements(self):
        self.tool_requires(self.tested_reference_str)

    def test(self):
        self.run('cygcheck -c')
        self.run('bash.exe -c ^"uname -a^"')
        self.run('bash.exe -c ^"test -L /etc/networks^"')
