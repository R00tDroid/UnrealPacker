from setuptools import setup, find_packages

setup(
    name='uepacker',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'uepacker=Source.UePack:main'
        ]
    },
    install_requires=[
    ],
    author='Your Name',
    description='Description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/R00tDroid/UnrealPacker',
    license='MIT',
)