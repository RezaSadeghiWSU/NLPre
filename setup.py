import setuptools
import os

__local__ = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
long_description = '''NLPre
=================================
A collection of Natural Language Preprocessing (NLPre) utilities, suitable
for a pipeline.
'''

setuptools.setup(
    name='nlpre',

    # Versions should comply with PEP440. 
    version='0.1.0',

    description='Natural Language Preprocessing (NLPre) utilities.',
    long_description=long_description,

    # The project's main homepage.
    url="https://github.com/NIHOPA/NLPre",

    # Author details
    author="Travis Hoppe",
    author_email="travis.hoppe+nlpre@gmail.com",

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',

        'Natural Language :: English',
        
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
        
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords="NLP",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['nlpre'],

    # Include package data...
    include_package_data=True,

    # entry_points={
    #    'console_scripts': [
    #        'miniprez=miniprez.__main__:main',
    #    ]
    #},

    test_suite="tests",

    # Fill this in when ready...
    download_url='',
)