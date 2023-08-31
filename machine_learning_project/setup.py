#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Ashvini Alashetty",
    author_email='cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This is the basic end to end ml project",
    entry_points={
        'console_scripts': [
            'machine_learning_project=machine_learning_project.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='machine_learning_project',
    name='machine_learning_project',
    packages=find_packages(include=['machine_learning_project', 'machine_learning_project.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Ashvini Alashetty/machine_learning_project',
    version='0.0.1',
    zip_safe=False,
)
