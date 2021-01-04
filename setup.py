import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Thomas Dewitte",
    author_email="thomasdewittecontact@gmail.com",

    name='bitcoin_value',
    version='1.3.3',
    license="MIT",
    url='https://github.com/dewittethomas/bitcoin-value',
    python_requires='>= 3.5',
    
    description='Gets the value of one bitcoin',
    long_description=README,
    long_description_content_type="text/markdown",

    package_dir={"bitcoin_value": "bitcoin_value"},
    install_requires=["requests>=2.22.0"],
    
    packages=setuptools.find_packages(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)