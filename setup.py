import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="trafolta",
    version="0.0.1",
    description="Coordinate Transformations for Swiss Reference Systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eraymann/trafolta",
    author="Elias Raymann",
    author_email="elias.raymann@swisstopo.ch",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7"
)
