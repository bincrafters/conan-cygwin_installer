#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_installer
import os

if __name__ == "__main__":

    builder = build_template_installer.get_builder()

    builder.add({"arch_build": os.environ["CONAN_ARCHS"]}, {}, {}, {})

    builder.run()
