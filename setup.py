from setuptools import setup, find_packages

setup(
    name="classics",
    packages=find_packages(where="src"),
    version="0.1.0",
    package_dir={"": "src"},
)
