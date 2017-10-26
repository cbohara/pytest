from setuptools import setup, find_packages

setup(
    name='some_package',
    description='Demostrate packaging and distribution',
    version='1.0',
    author="Charlie O'Hara",
    email="dummyemail@example.com",
    url="https://github.com/cbohara/pytest",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
