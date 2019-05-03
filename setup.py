"""tzf.pyramid_routing installation file."""

import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)


def read(fname):
    """
    Read file.

    :param str fname: filename

    :returns: file content

    """
    return open(os.path.join(here, fname)).read()


test_requires = [
    'pytest==4.4.1',
    'pytest-pyramid==0.3.1',
    'pytest-cov==2.7.1',
]

extras_require = {
    'docs': ['sphinx'],
    'tests': test_requires
}

setup(
    name='tzf.pyramid_routing',
    version='0.1.2',
    description='Reads and sets routing configuration from a package',
    long_description=(
        read('README.rst') + '\n\n' + read('CHANGES.rst')
    ),
    keywords='pyramid routing',
    author='Grzegorz Sliwinski',
    author_email='username: fizyk, domain: fizyk.net.pl',
    url='https://github.com/fizyk/pyramid_routing',
    license="MIT License",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    namespace_packages=['tzf'],
    install_requires=[
        'pyramid',
    ],
    tests_require=test_requires,
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
)
