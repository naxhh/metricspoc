from setuptools import setup

setup(
    name='metrics',
    version='0.1',
    py_modules=['metrics'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        metrics=metrics:cli
    ''',
)
