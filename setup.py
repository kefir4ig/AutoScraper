from setuptools import find_packages, setup
from pathlib import Path

here = Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="AutoScraper",
    version="1.1.14",
    description="A Smart, Automatic, Fast and Lightweight Web Scraper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kefir4ig/AutoScraper",
    author="kefir4ig",
    author_email="lightmoon0x1017@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="scraping, scraper, web scraping, automation",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.20.0",
        "beautifulsoup4>=4.9.0",
        "lxml>=4.6.0",
    ],
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    project_urls={
        "Bug Reports": "https://github.com/kefir4ig/AutoScraper/issues",
        "Source": "https://github.com/kefir4ig/AutoScraper",
    },
)
