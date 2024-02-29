import setuptools

PROJECT_NAME = "textSummarizer"
VERSION = "0.0.0"

AUTHOR = "Cheng"
AUTHOR_EMAIL = "fanchenghhh@outlook.com"
URL = "https://github.com/fanchenghhh/text_summarizer"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name=PROJECT_NAME,
    version=VERSION,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)