from os import path
from setuptools import setup
from importlib.machinery import SourceFileLoader

### To run the tests:
# python setup.py test

### To install on a machine:
# sudo python setup.py install

### To install in a home directory (~/lib):
# python setup.py install --home=~
LONG_DESCRIPTION = open(path.join(path.dirname(__file__), 'README.md')).read()

# avoid loading the package before requirements are installed:
version = SourceFileLoader('version', 'foss42/version.py').load_module()

DEPENDENCIES = ["Unidecode",
                "titlecase",
                "typeguard",
                ]

setup(name="foss42",
      version=str(version.VERSION),
      author="foss42",
      author_email="foss42.org@gmail.com",
      keywords='foss42 utility coversion validation generate transform ml bi visualization charts language graphs data map',
      description="Core Python library used by foss42 APIs.",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/foss42/foss42",
      project_urls={
            "Homepage": "https://foss42.com",
            "Source Code": "https://github.com/foss42/foss42",
            "Bug Tracker": "https://github.com/foss42/foss42",
            "Documentation": "https://github.com/foss42/foss42/issues",
      },
      test_suite="test",
      packages=['foss42'],
      install_requires=DEPENDENCIES,
      tests_require=DEPENDENCIES,
      python_requires='>=3.10',
      classifiers=[  
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Natural Language :: English',
      ],      
      )
