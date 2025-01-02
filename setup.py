from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="runtime-analysis",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for runtime performance analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/runtime-analysis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'psutil>=5.8.0',
        'matplotlib>=3.4.0',
    ],
    extras_require={
        'test': ['pytest>=6.2.0'],
    },
)
