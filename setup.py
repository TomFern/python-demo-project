import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demo_project",
    version="0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A demo Python project for CI/CD exercises.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/demo_project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

