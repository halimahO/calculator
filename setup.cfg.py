import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tesla",
    version="0.0.1",
    author="Halimah Oladosu",
    author_email="haleemaholadosu@gmail.com",
    description="A tesla factory package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/halimahO/tesla-factory-package",
    project_urls={
        "Bug Tracker": "https://github.com/halimahO/tesla-factory-package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "tesla"},
    packages=setuptools.find_packages(where="tesla"),
    python_requires=">=3.6",
)