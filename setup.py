from setuptools import setup, find_packages

def extract_dependencies() -> list[str]:
    with open('requirements.txt', 'r') as f:
        requirements = []
        for item in f.readlines():
            requirements.append(item.replace('\n', ''))

    return requirements

setup(
    name='poorlib',
    version='0.0.5',
    description='Python library for poor-man',
    author='Farhan Purdi',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=extract_dependencies(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest==8.3.2'],
    test_suite='tests',
)