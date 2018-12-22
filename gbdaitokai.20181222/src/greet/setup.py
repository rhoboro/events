from setuptools import setup

setup(
    name='greet',
    version='0.1',
    py_modules=['greet'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        greet=greet:cli
    ''',
)
