from setuptools import setup, find_packages

setup(
    name="line_bot_2",
    version="0.1",
    packages=find_packages(where="."),
    package_dir={"": "."},  # srcをルートとして利用
)
