import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Logistic System",
    version = "0.0.1",
    author = "Lilia Mudryk",
    author_email = "liliia.mudryk@ucu.edu.ua",
    description= "Project to use simple logistic system",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url =" ",
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Licence",
        "Operating System :: OS Independent",
    ],
    python_requires ='>=3.8'   
)
