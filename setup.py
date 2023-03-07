from pathlib import Path

from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]
style_packages = ["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"]
test_packages = ["pytest==7.1.2"]

setup(
    name="mlops",
    version=0.1,
    description="Machine Learning OPs (MLOps) Template",
    author="Kenneth Brezinski",
    author_email="kenbrezinski@live.com",
    url="https://github.com/kbrezinski",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extra_require={
        "dev": docs_packages + style_packages + test_packages,
        "docs": docs_packages,
        "test": test_packages,
    },
)

# install with pip install -e
# installs in develop mode
