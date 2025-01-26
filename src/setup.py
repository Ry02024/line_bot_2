from setuptools import setup, find_packages

setup(
    name="line_bot_2",
    version="0.1",
    packages=find_packages(),  # パッケージを自動検出
    package_dir={"": "."},  # src 内のモジュールを検出
)
