from setuptools import setup


def read_requirements(path):
    with open(path, "r", encoding="utf-8") as f:
        return [i.strip() for i in f.read().splitlines() if i]


requirements = read_requirements("./requirements.txt")
version = "0.0.5"

readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

packages = [
    "ZyGinator",
]

setup(
    name="ZyGinator",
    author="zyrexxx",
    author_email="tihonburdakov572@gmail.com",
    url="https://github.com/zyrexxx/ZyGinator",
    project_urls={
        "Documentation": "https://github.com/zyrexxx/ZyGinator/blob/main/README.md",
        "Issue tracker": "https://github.com/zyrexxx/ZyGinator/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A Python library to easily create embed paginators",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
from setuptools import setup


def read_requirements(path):
    with open(path, "r", encoding="utf-8") as f:
        return [i.strip() for i in f.read().splitlines() if i]


requirements = read_requirements("./requirements.txt")
version = "0.0.5"

readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

packages = [
    "ZyGinator",
]

setup(
    name="ZyGinator",
    author="zyrexxx",
    author_email="tihonburdakov572@gmail.com",
    url="https://github.com/zyrexxx/ZyGinator",
    project_urls={
        "Documentation": "https://github.com/zyrexxx/ZyGinator/blob/main/README.md",
        "Issue tracker": "https://github.com/zyrexxx/ZyGinator/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A Python library to easily create embed paginators",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
