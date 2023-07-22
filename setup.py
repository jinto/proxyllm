from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="proxyllm",
    version="0.0.1",
    author="jaypark",
    author_email="jaypark@gmail.com",
    description="Language Model Proxy",
    long_description_content_type="text/markdown",
    url="https://github.com/jinto/proxyllm",
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=["chatbot", "ai", "ml", "llm"],
    python_requires=">=3.10",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
)
