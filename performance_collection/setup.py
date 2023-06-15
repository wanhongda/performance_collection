from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="performance_collection",  # 这里是pip项目发布的名称
    version="0.0.3",  # 版本号，数值大的会优先被pip，每次更新需要修改这个为更高的版本
    keywords=("performance_collection"),
    description="A public script library",
    long_description="Public Script Library of quality management department",
    license="Apache License 2.0",

    url="https://github.com/wanhongda/performance_collection.git",  # 项目相关文件地址，一般是github
    author="wanhongda",
    author_email="451546614@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["solox"]  # 这个项目需要的第三方库
)
