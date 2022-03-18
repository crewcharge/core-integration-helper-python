from setuptools import find_packages, setup

setup(
    name='crewcharge_core',
    packages=find_packages(include=["crewcharge_core"]),
    version='1.0.0',
    description='Crewcharge is a customer analytics, customer success tool for SaaS companies. The core package allows logging triggers and performing user crud operations within Crewcharge',
    author='Bharadwaj Giridhar',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
