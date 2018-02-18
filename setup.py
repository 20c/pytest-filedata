
from setuptools import find_packages, setup


version = open('facsimile/VERSION').read().strip()
requirements = open('facsimile/requirements.txt').read().split("\n")
test_requirements = open('facsimile/requirements-test.txt').read().split("\n")


setup(
    name='pytest_filedata',
    version=version,
    author='20C',
    author_email='code@20c.com',
    description='easily load data from files',
    long_description='',
    license='LICENSE.txt',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages = find_packages(),
    include_package_data=True,
    url='https://github.com/20c/pytest-filedata',
    download_url='https://github.com/20c/pytest-filedata/%s' % version,

    install_requires=requirements,
    test_requires=test_requirements,

    zip_safe=True,
    entry_points={
        'pytest11': [
            'filedata = pytest_filedata',
        ],
    },
)
