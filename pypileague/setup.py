from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='leaguenames',
    version='0.0.1',
    description='A library that turns league of legends champions ids to champions names.',
    py_modules=["leaguenames"],
    package_dir={'':'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = ["requests",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
