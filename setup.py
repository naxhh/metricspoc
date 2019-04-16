from setuptools import setup, find_packages

setup(
    name='metricspoc',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click==7.0'
    ],
    entry_points='''
        [console_scripts]
        metrics=scripts.cli:cli
    ''',
)
