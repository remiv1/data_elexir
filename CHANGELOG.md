# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Non publié]

### Planifié
- Interface web pour DataLexir
- Support de formats de données supplémentaires (Parquet, Avro)
- Optimisations de performance pour les gros datasets
- Documentation interactive avec exemples en direct

## [0.1.0] - 2025-08-28

### Ajouté
- **Elexbook** : Module d'exploration interactive de données
  - Échantillonnage intelligent des datasets volumineux
  - Interface interactive avec widgets Jupyter
  - Historique automatique des transformations
  - Assignation dynamique des types de colonnes
  - Méthode `concatbook()` pour générer les pipelines

- **Structure de base** pour les modules Elexdas et Elexpark
  - Architecture modulaire pour Pandas et Spark
  - Framework de génération de pipelines

- **Documentation complète**
  - README détaillé avec exemples d'utilisation
  - Guide de contribution (CONTRIBUTING.md)
  - Notebook de démonstration complet
  - Configuration pour l'installation via pip

- **Configuration du projet**
  - Licence Apache 2.0
  - Configuration pyproject.toml moderne
  - Dépendances de développement
  - Structure de tests avec pytest
  - Configuration pour Black, flake8, mypy

- **Fonctionnalités Elexbook**
  - Initialisation avec échantillonnage paramétrable
  - Logging automatique des opérations pandas
  - Interface `__getattr__` pour transparence avec pandas
  - Support des widgets interactifs IPython

### Configuration
- Python 3.8+ requis
- Dépendances : pandas, numpy, ipywidgets, ipython, matplotlib, jupyter
- Dépendances optionnelles : pyspark pour le support Spark

### Documentation
- Guide d'installation et d'utilisation
- Exemples de cas d'usage pour gestionnaires de données
- Architecture détaillée des trois modules
- Instructions de contribution pour la communauté

---

## Types de changements

- `Ajouté` pour les nouvelles fonctionnalités.
- `Modifié` pour les changements dans les fonctionnalités existantes.
- `Déprécié` pour les fonctionnalités qui seront supprimées dans les versions futures.
- `Supprimé` pour les fonctionnalités supprimées dans cette version.
- `Corrigé` pour toute correction de bug.
- `Sécurité` pour inviter les utilisateurs à mettre à jour en cas de vulnérabilités.
