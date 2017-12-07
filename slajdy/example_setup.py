from setuptools import setup, find_packages


setup(
    name='sample',
    version='1.2.0',
    description='A sample Python project',
    url='https://github.com/pypa/sampleproject',
    author='The Python Packaging Authority',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='sample setuptools development',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['peppercorn'],
    package_data={
        'sample': ['package_data.dat'],
    },
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
