from setuptools import setup


setup(
    name="test-module-name-goes-here",
    version="1.33.7",
    author="author-name-goes-here",
    author_email="author.name@mail.com",
    description="test module description goes here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"test": "."},
)

