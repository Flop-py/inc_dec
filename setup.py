import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inc_dec",
    version="0.0.1",
    author="Floppy",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Flop-py/inc_dec",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
