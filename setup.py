from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name="recurrence",
        author="MDWGROGAN",
        packages=find_packages(exclude=["tests*"]),
        setup_requires=["nose", "pylint", "setuptools-lint"],
        tests_require=["coverage", "mock"],
    )
