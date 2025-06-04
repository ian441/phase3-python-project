from setuptools import setup, find_packages

setup(
    name="health_simplified",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "sqlalchemy",
        "python-dateutil",
    ],
    entry_points={
        "console_scripts": [
            "myapp=health_simplified.main:app",
        ],
    },
)