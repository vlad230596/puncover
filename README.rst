.. image:: https://img.shields.io/travis/HBehrens/puncover.svg
    :target: https://travis-ci.org/HBehrens/puncover
.. image:: https://img.shields.io/codecov/c/github/HBehrens/puncover.svg
    :target: https://codecov.io/gh/HBehrens/puncover

puncover
========

.. image:: https://raw.githubusercontent.com/HBehrens/puncover/master/images/overview.png
Analyzes C/C++ binaries for code size, static variables and stack usages.
It creates a report with dissambler and call-stack analysis per directory, file, or function.

Run
    * ``python.exe -m pip install .``    
    * ``python runner.py --arm_tools_dir="C:\Program Files (x86)\Arm GNU Toolchain arm-none-eabi\13.3 rel1" --elf_file ./Test.elf``
