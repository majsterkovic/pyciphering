import setuptools

NAME = 'pyciphering'
VERSION = '0.1.1'
DESCRIPTION = 'An awesome package to text ciphering'
CLASSIFIERS = [
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]

setuptools.setup(
    name=NAME,
    version=VERSION,
    author='majsterkovic',
    author_email='mariusz8h@o2.pl',
    description=DESCRIPTION,
    long_description=open('DESCRIPTION.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/majsterkovic/ciphers',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[],
    keywords=['ciphers', 'encryption', 'encode', 'decode'],
    classifiers=CLASSIFIERS
)