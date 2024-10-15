from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llm-explore",
    version="0.1.0",  # Package version
    author="Jade Wibbels",
    author_email="jade.wibbels@gmail.com",
    description="Working and learning in public: LLMs and knowledge graphs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/JadeCara/llm_explore",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "transformers>=4.0.0",
        "sentencepiece>=0.2.0",
        "networkx>=2.5",
        "scikit-learn>=0.24",
        "keybert>=0.3.0",
        "matplotlib>=3.4.0",
        "neo4j>=4.0.0",
        "pandas>=1.2.0",
        "numpy>=1.19.0",
        "jupyterlab>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8.0",
            "black>=21.0",
        ],
    },
    entry_points={
        "console_scripts": [],
    },
    include_package_data=True,
)
