from setuptools import find_packages, setup

setup(
    name='translator',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'two1==3.4.1',
    ],
    author='Jason Walsh',
    url='https://github.com/rightlag/21-translator'
)
