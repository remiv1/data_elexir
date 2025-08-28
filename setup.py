"""
Setup configuration for DataLexir package.
"""

from setuptools import setup, find_packages

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="datalexir",
    version="0.1.0",
    author="Rémi Verschuur",
    author_email="remi.verschuur@example.com",  # Remplacez par votre vraie adresse
    description="Une bibliothèque Python pour l'exploration interactive de données et la génération automatique de pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/remiv1/data_elexir",
    project_urls={
        "Bug Reports": "https://github.com/remiv1/data_elexir/issues",
        "Source": "https://github.com/remiv1/data_elexir",
        "Documentation": "https://github.com/remiv1/data_elexir/blob/main/README.md",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "spark": ["pyspark>=3.0.0"],
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
            "jupyter>=1.0",
            "notebook>=6.0",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.17",
        ],
    },
    entry_points={
        "console_scripts": [
            # Ajoutez ici des scripts en ligne de commande si nécessaire
            # "datalexir-cli=datalexir.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "datalexir": ["*.json", "*.yaml", "*.yml"],
    },
    keywords="data exploration pandas spark pipeline jupyter notebook data science",
    license="Apache License 2.0",
)
