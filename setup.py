from setuptools import setup, find_packages

setup(
    name='Unreal Engine Packer',
    version='1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'uepacker=Source.UePack:main'
        ]
    },
    install_requires=[
    ],
    author='R00tDroid',
    description='A commandline tool to automatically package Unreal Engine projects or plugins',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/R00tDroid/UnrealPacker',
    license='MIT',
)
