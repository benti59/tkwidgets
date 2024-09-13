from setuptools import setup, find_packages

setup(
    name="tkwidgets",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["windnd",],
    author="Benti",
    author_email="t3137904401@outlook.com",
    description="A collection of custom Tkinter widgets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tkwidgets",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.6',
)
