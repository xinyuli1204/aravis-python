import io

from setuptools import setup
import sys
from typing import List
import platform
import sysconfig
import os

from setuptools._distutils.util import convert_path
def package_files(directorys):
    paths = []
    for directory in directorys:
        for (path, directories, filenames) in os.walk(directory):
            for filename in filenames:
                paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files(['aravis/bin','aravis/include'])

def get_version():
    if os.environ.get("ARAVIS_VERSION") is not None:
        tag = os.environ.get("ARAVIS_VERSION_VERSION")
    else:
        main_ns = {}
        ver_path = convert_path('./ionpy/version.py')
        with open(ver_path) as ver_file:
            exec(ver_file.read(), main_ns)
        tag = main_ns["__version__"]
    return tag

def main():
    long_description = io.open("README.md", encoding="utf-8").read()
    package_data: List[str] = []

    if platform.system() == 'Windows':
        pkg_path = os.path.join(os.path.dirname(__file__), 'aravis\lib\pkg_path')
        os.environ["PKG_CONFIG_PATH"] = pkg_path
        package_data = extra_files
    elif platform.system() == 'Darwin':

    elif platform.system() == 'Linux':
        package_data = []

    setup(
        name="aravis-python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/fixstars/ion-kit",
        python_requires=">=3.8.0",
        packages=["aravis"],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
        ],
        description="Python Binding for ion-kit",
        package_data={"aravis": package_data},
        install_requires=["pygobject"],
        # ext_modules=EmptyListWithLength(),
        include_package_data=False,

    )


# This creates a list which is empty but returns a length of 1.
# Should make the wheel a binary distribution and platlib compliant.
class EmptyListWithLength(list):
    def __len__(self):
        return 1


if __name__ == "__main__":
    main()