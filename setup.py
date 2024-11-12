from setuptools import setup

setup(
    name='wordlist_generator',
    version='1.0.0',
    description='A custom wordlist generator for penetration testing',
    author='DEERAJ',
    author_email='unnideeraj@proton.me',
    license='MIT',
    py_modules=['wordlist_generator'],
    entry_points={
        'console_scripts': [
            'generate=wordlist_generator:main',
        ],
    },
)
