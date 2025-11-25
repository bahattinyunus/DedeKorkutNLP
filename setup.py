from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dedekorkut",
    version="0.1.0",
    author="DedeKorkutNLP Contributors",
    description="A Turkish NLP library and evaluation toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bahattinyunus/DedeKorkutNLP",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Natural Language :: Turkish",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "nltk",
        "scikit-learn",
        "pandas",
        "tqdm",
    ],
)
