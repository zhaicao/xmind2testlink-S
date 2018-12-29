"""
Documentation
-------------
xmind2testlink is a tool to help you convert xmind file to testlink recognized xml files,
then you can import it into testlink as test suite and test cases.

For more detail, please go to: https://github.com/tobyqin/xmind2testlink_s

"""
from codecs import open
from os import path

from setuptools import setup, find_packages

current_dir = path.abspath(path.dirname(__file__))
long_description = __doc__

with open(path.join(current_dir, "CHANGELOG.md"), encoding="utf-8") as f:
    long_description += "\n" + f.read()

classifiers = ["License :: OSI Approved :: MIT License",
               "Topic :: Software Development",
               "Topic :: Utilities",
               "Operating System :: Microsoft :: Windows",
               "Operating System :: MacOS :: MacOS X"] + [
                  ("Programming Language :: Python :: %s" % x) for x in "2.7 3.5".split()]


def command_line():
    target = "xmind2testlink.main:main"
    entry_points = []
    entry_points.append("xmind2testlink=%s" % target)
    return entry_points


def main():
    setup(
        name="xmind2testlink-S",
        description="Convert xmind to TestLink xml",
        keywords="xmind testlink import converter testing testcase",
        long_description=long_description,
        classifiers=classifiers,
        version="1.0.0",
        author="Ricky Chai",
        author_email="Ricky2971@hotmail.com",
        url="https://github.com/zhaicao/xmind2testlink_s",
        packages=find_packages(exclude=['tests', 'tests.*']),
        package_data={},
        install_requires=[],
        entry_points={"console_scripts": command_line(), },
        zip_safe=False
    )


if __name__ == "__main__":
    main()