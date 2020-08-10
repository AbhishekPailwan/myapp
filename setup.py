import setuptools

with open ("README.md","r") as ab:
  desc=ab.read()

# This call to setup() does all the work
setuptools.setup(
    name="functions",
    version="0.0.1",
    description="Read the latest Real Python tutorials",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/myapp/myfunctions",
    author="Abhishek",
    author_email="pailwan.abhishek22@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independant",
    ],
    python_requires='>=3.7',
)
