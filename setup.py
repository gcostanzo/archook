from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "archook", "VERSION")) as f:
    version = f.read().strip()

with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="archook",
    version=version,
    description="Locates arcpy and makes it available to the running python distribution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="ArcGIS, arcpy",
    author="James Ramm",
    author_email="nospam@example.com",
    maintainer="Matt Wilkie",
    maintainer_email="matt.wilkie@gov.yk.ca",
    url="https://github.com/JamesRamm/archook",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
    ],
)
