# DataLexir

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/datalexir.svg)](https://badge.fury.io/py/datalexir)

> **Une bibliothèque Python révolutionnaire pour l'exploration interactive de données et la génération automatique de pipelines**

DataLexir transforme votre processus d'exploration de données en permettant de travailler sur des échantillons légers dans des notebooks Jupyter, puis de générer automatiquement des pipelines de production pour Pandas et Spark ou encore dans des langages compilés comme Go et Rust.

## 🎯 Vision

DataLexir résout un problème majeur des gestionnaires de données : **comment explorer efficacement de gros volumes de données et transformer cette exploration en pipeline de production reproductible et léger ?**

## Problématique

Les gestionnaires de données font face à des défis majeurs :

- **Exploration inefficace** : Travailler sur des échantillons limités dans des notebooks, puis réécrire manuellement les transformations pour les appliquer à l'ensemble des données.
- **Manque de traçabilité** : Difficulté à suivre les transformations appliquées lors de l'exploration, ce qui rend la reproduction et le débogage complexes.
- **Transition laborieuse vers la production** : Convertir les étapes d'exploration en pipelines de production est souvent fastidieux et sujet à erreurs.
- **Performance** : Travailler sur des échantillons peut ne pas refléter les performances réelles sur l'ensemble des données, rendant l'optimisation difficile.
- **Langages compilés** : Les gestionnaires de données qui souhaitent utiliser des langages compilés pour la production doivent souvent réécrire entièrement leur logique d'exploration.
- **Support multi-moteur** : Les outils existants sont souvent limités à un moteur de traitement de données spécifique, ce qui rend difficile l'adaptation à différents environnements.

## Solution proposée

DataLexir propose une approche innovante pour résoudre ces problèmes :

1. **Exploration interactive sur échantillons** : Permet de travailler sur des échantillons légers dans des notebooks Jupyter, avec une interface intuitive et des widgets interactifs.
2. **Capture de l'intention** : Enregistre automatiquement toutes les transformations appliquées lors de l'exploration, créant un historique complet et traçable.
3. **Conservation de la logique en TOML** : Stocke la logique d'exploration dans un format TOML léger, facilitant la conversion en pipelines de production ainsi que la possibilité de commenter l'intention métier.
4. **Génération automatique de pipelines** : Convertit la logique d'exploration en pipelines de production pour Pandas, Spark, Go, Rust, etc., avec une optimisation automatique des opérations.
5. **Support multi-moteur** : Permet de générer des pipelines pour différents moteurs de traitement de données, offrant une flexibilité maximale pour les gestionnaires de données.
6. **Evolutivité** : Permet de faire évoluer les pipelines en fonction de l'évolution des données et des besoins métier, avec une traçabilité complète des changements et de leur impact sur les performances.

## Fonctionnalités clés

- 🔬 **Exploration interactive** : Travaillez sur des échantillons de données dans des notebooks
- 📝 **Capture de l'intention** : Historique complet de toutes les transformations appliquées
- 🏗️ **Génération automatique de pipelines** : Convertissez votre exploration en code de production
- ⚡ **Multi-moteur** : Support de Pandas et Apache Spark, mais aussi de langages compilés comme Go et Rust
- 🎮 **Interface intuitive** : Widgets interactifs pour une exploration sans code
- 📊 **Traçabilité complète** : Historique détaillé de toutes les transformations et versionning des pipelines

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
book = Elexbook.read_csv('sales_10M_rows.csv', sample=0.01)
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

## 📚 Documentation

Pour une documentation complète, consultez (_Documentation à réaliser_) :

- [Guide de démarrage rapide](documentation/guide-demarrage.md)
- [Référence API](documentation/api-reference.md)
- [Exemples d'utilisation](documentation/exemples.md)
- [Notebooks de démonstration](notebooks/)

## Contribuer

Nous encourageons les contributions ! DataLexir est un projet open source encore en phase de projet.

Pour plus de détails, consultez [CONTRIBUTING.md](CONTRIBUTING.md).

## Équipe

**Créateur et mainteneur principal**:

- **Rémi Verschuur** ([@remiv1](https://github.com/remiv1))

### Rejoignez l'équipe

Nous recherchons des contributeurs passionnés pour faire grandir DataLexir. Si vous êtes intéressé par :

- Le développement Python
- L'ingénierie des données
- L'UX/UI pour les outils de données
- La documentation technique
- Le développement Go ou Rust pour les pipelines de production

N'hésitez pas à me contacter !

## 📄 Licence

Ce projet est sous licence Apache License 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

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
