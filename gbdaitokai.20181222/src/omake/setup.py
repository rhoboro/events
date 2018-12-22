from setuptools import setup

setup(
    name='repo',
    version='0.1',
    py_modules=['repo'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        repo=repo:cli
    ''',
)
