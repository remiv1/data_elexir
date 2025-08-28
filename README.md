# 🔮 DataLexir

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/datalexir.svg)](https://badge.fury.io/py/datalexir)

> **Une bibliothèque Python révolutionnaire pour l'exploration interactive de données et la génération automatique de pipelines**

DataLexir transforme votre processus d'exploration de données en permettant de travailler sur des échantillons légers dans des notebooks Jupyter, puis de générer automatiquement des pipelines de production pour Pandas et Spark.

## 🎯 Vision

DataLexir résout un problème majeur des gestionnaires de données : **comment explorer efficacement de gros volumes de données et transformer cette exploration en pipeline de production reproductible ?**

### ✨ Fonctionnalités clés

- 🔬 **Exploration interactive** : Travaillez sur des échantillons de données dans des notebooks
- 🏗️ **Génération automatique de pipelines** : Convertissez votre exploration en code de production
- ⚡ **Multi-moteur** : Support de Pandas et Apache Spark
- 🎮 **Interface intuitive** : Widgets interactifs pour une exploration sans code
- 📊 **Traçabilité complète** : Historique détaillé de toutes les transformations

## 🚀 Installation

### Via pip (recommandé)

```bash
pip install datalexir
```

### Installation en mode développement

```bash
git clone https://github.com/remiv1/data_elexir.git
cd data_elexir
pip install -e .
```

## 🏗️ Architecture

DataLexir est organisé en trois modules principaux :

### 📚 `elexbook` - Exploration Interactive

Module d'exploration de données avec échantillonnage intelligent pour les notebooks Jupyter.

**Fonctionnalités :**

- Échantillonnage intelligent des datasets volumineux
- Interface interactive avec widgets Jupyter
- Historique automatique des transformations
- Assignation dynamique des types de colonnes

### 🐼 `elexdas` - Pipeline Pandas

Générateur et exécuteur de pipelines pour Pandas.

**Fonctionnalités :**

- Conversion des explorations en pipelines Pandas
- Optimisation automatique des opérations
- Support complet de l'écosystème Pandas

### ⚡ `elexpark` - Pipeline Spark

Générateur et exécuteur de pipelines pour Apache Spark.

**Fonctionnalités :**

- Conversion des explorations en pipelines Spark
- Optimisation pour les gros volumes de données
- Distribution automatique des calculs

## 📋 Guide d'utilisation rapide

### 1. Exploration avec Elexbook

```python
import pandas as pd
from datalexir.elexbook import Elexbook

# Chargement d'un dataset volumineux
df = pd.read_csv('mon_gros_dataset.csv')

# Création d'un elexbook avec échantillonnage (30% par défaut)
book = Elexbook(df, sample=0.1)

# Exploration interactive
book.head()
book.describe()
book.dropna()
book.fillna(0)

# Interface interactive pour les types de colonnes
book.dynamic_type_assignment()

# Génération du pipeline
pipeline = book.concatbook()
```

### 2. Application avec Elexdas (Pandas)

```python
from datalexir.elexdas import Elexdas

# Application du pipeline sur les données complètes
elexdas = Elexdas(df)
result = elexdas.pipeline(pipeline)
```

### 3. Application avec Elexpark (Spark)

```python
from datalexir.elexpark import Elexpark
from pyspark.sql import SparkSession

# Initialisation Spark
spark = SparkSession.builder.appName("DataLexir").getOrCreate()
sdf = spark.read.csv('mon_gros_dataset.csv', header=True, inferSchema=True)

# Application du pipeline sur Spark
elexpark = Elexpark(sdf)
result = elexpark.pipeline(pipeline)
```

## 🎯 Cas d'usage : Analyse de données de ventes

Imaginez que vous êtes gestionnaire de données dans une entreprise de e-commerce avec 10 millions de transactions :

```python
# 1. Exploration sur échantillon (100k transactions)
from datalexir.elexbook import Elexbook
import pandas as pd

# Chargement des données
sales_data = pd.read_csv('sales_10M_rows.csv')
print(f"Dataset complet : {len(sales_data):,} lignes")

# Exploration interactive sur 1% des données
book = Elexbook(sales_data, sample=0.01)
print(f"Échantillon : {len(book.sample):,} lignes")

# Nettoyage interactif
book.dropna(subset=['customer_id', 'amount'])
book.fillna({'category': 'Unknown'})
book.astype({'amount': 'float64'})

# Analyse exploratoire
book.groupby('category')['amount'].sum().sort_values(ascending=False)
book.plot(x='date', y='amount', kind='line')

# Génération du pipeline
cleaning_pipeline = book.concatbook()
```

```python
# 2. Application en production sur les 10M de lignes
from datalexir.elexdas import Elexdas

# Application du pipeline sur toutes les données
processor = Elexdas(sales_data)
clean_sales_data = processor.pipeline(cleaning_pipeline)

# Ou pour de très gros volumes avec Spark
from datalexir.elexpark import Elexpark
spark_processor = Elexpark(spark_sales_data)
clean_sales_data_spark = spark_processor.pipeline(cleaning_pipeline)
```

## 🔧 Installation des dépendances

### Dépendances principales

```bash
pip install pandas numpy ipywidgets jupyter
```

### Pour le support Spark (optionnel)

```bash
pip install pyspark
```

### Pour le développement

```bash
pip install -r requirements-dev.txt
```


## 📚 Documentation

Pour une documentation complète, consultez :

- [Guide de démarrage rapide](documentation/guide-demarrage.md)
- [Référence API](documentation/api-reference.md)
- [Exemples d'utilisation](documentation/exemples.md)
- [Notebooks de démonstration](notebooks/)

## 🤝 Contribuer

Nous encourageons les contributions ! DataLexir est un projet open source en pleine croissance.

### Comment contribuer

1. **Fork** le repository
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b feature/ma-nouvelle-fonctionnalite`)
3. **Committez** vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. **Pushez** vers la branche (`git push origin feature/ma-nouvelle-fonctionnalite`)
5. **Ouvrez** une Pull Request

### Directives de contribution

- Suivez les conventions de code Python (PEP 8)
- Ajoutez des tests pour toutes les nouvelles fonctionnalités
- Documentez vos changements
- Assurez-vous que tous les tests passent

Pour plus de détails, consultez [CONTRIBUTING.md](CONTRIBUTING.md).

## 👥 Équipe

**Créateur et mainteneur principal**:

- **Rémi Verschuur** ([@remiv1](https://github.com/remiv1)) - *Créateur et architecte principal*

### Rejoignez l'équipe !

Nous recherchons des contributeurs passionnés pour faire grandir DataLexir. Si vous êtes intéressé par :

- Le développement Python
- L'ingénierie des données
- L'UX/UI pour les outils de données
- La documentation technique

N'hésitez pas à nous contacter !

## 📄 Licence

Ce projet est sous licence Apache License 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```txt
Copyright 2025 DataLexir Contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 🎯 Roadmap

Bien qu'aucune roadmap formelle ne soit définie pour le moment, les prochaines étapes incluront :

- Amélioration de l'interface utilisateur interactive
- Support de formats de données supplémentaires
- Optimisation des performances
- Documentation étendue et tutoriels

---

⭐ **Si DataLexir vous aide dans vos projets, n'hésitez pas à nous donner une étoile sur GitHub !**

## 🔗 Liens utiles

- [Issues GitHub](https://github.com/remiv1/data_elexir/issues)
- [Discussions](https://github.com/remiv1/data_elexir/discussions)
- [PyPI Package](https://pypi.org/project/datalexir/)
