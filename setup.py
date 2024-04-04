from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bitcoin_value",
    version="1.6.0",
    author="Thomas Dewitte",
    author_email="thomasdewittecontact@gmail.com",
    license="MIT",
    url="https://github.com/dewittethomas/bitcoin-value",
    description="A module to fetch the latest value of Bitcoin in different currencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"bitcoin_value": "bitcoin_value"},
    install_requires=["requests>=2.28.1"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="bitcoin currency value worth btc usd eur gbp crypto fetch",
)
