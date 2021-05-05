from setuptools import setup, find_packages
from jq_repl import __version__

setup(
    name="jq-repl",
    version=__version__,
    author_email="pawelsacawa@gmail.com",
    url="https://github.com/psacawa/jq-repl",
    packages=find_packages(),
    entry_points={"console_scripts": ["jqr= jq_repl.main:main"]},
)
