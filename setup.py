import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 0):
    sys.exit("Sorry, Python < 3.0 is not supported")

import re

VERSIONFILE = "mputils/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

install_requires = [
    "pywin32 >= 227",
]

setup(
    name="mputils",
    version=verstr,
    description="mputils",
    long_description="Please visit `Github <https://github.com/saycv/mputils>`_ for more information.",
    author="mputils project developers",
    author_email="",
    url="https://github.com/saycv/mputils",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    entry_points={},
    include_package_data=True,
    install_requires=install_requires,
)
