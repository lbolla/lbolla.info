import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "lbolla.info",
    version = "0.1",
    author = "Lorenzo Bolla",
    author_email = "lbolla@gmail.com",
    description = ("Lorenzo Bolla's Homepage"),
    license = "BSD",
    keywords = "lorenzo bolla lbolla homepage",
	url = "https://github.com/lbolla/lbolla.info",
    packages=find_packages(),
    long_description=read('README.txt'),
    classifiers=[
		"Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)

