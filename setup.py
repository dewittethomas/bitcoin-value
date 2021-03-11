from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name = "bitcoin_value",
    version = "1.4.2",
    license = "MIT",
    url = "https://github.com/dewittethomas/bitcoin_value",
    
    description = "A tracker that gets the latest value of Bitcoin in any currency",
    long_description = long_description,
    long_description_content_type = "text/markdown",

    package_dir = {"bitcoin_value": "bitcoin_value"},
    install_requires = [
        "requests>=2.22.0"
    ],

    packages = find_packages(),

    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],

    keywords = "bitcoin currency value worth btc usd eur gbp crypto fetch"
)