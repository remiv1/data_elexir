# Guide de Contribution - DataLexir

Merci de votre intérêt pour contribuer à DataLexir ! 🎉

Ce guide vous aidera à comprendre comment participer au développement de notre bibliothèque d'exploration de données et de génération de pipelines.

## Comment Contribuer

### Types de Contributions

Nous accueillons plusieurs types de contributions :

- **Corrections de bugs** : Signalement et correction de problèmes
- **Nouvelles fonctionnalités** : Ajout de nouvelles capacités
- **Documentation** : Amélioration de la documentation et des exemples
- **Tests** : Ajout de tests pour améliorer la couverture
- **Interface utilisateur** : Amélioration des widgets Jupyter
- **Performance** : Optimisation des performances

### Workflow de Contribution

1. **Fork du Repository**

   ```bash
   # Fork le repository sur GitHub
   # Puis clone votre fork
   git clone https://github.com/VOTRE-USERNAME/data_elexir.git
   cd data_elexir
   ```

2. **Configuration de l'Environnement de Développement**

   ```bash
   # Créer un environnement virtuel
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   
   # Installer les dépendances de développement
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   pip install -e .
   ```

3. **Créer une Branche**

   ```bash
   git checkout -b feature/ma-nouvelle-fonctionnalite
   # ou
   git checkout -b bugfix/correction-bug-specifique
   ```

4. **Développement**
   - Faites vos modifications
   - Ajoutez des tests si nécessaire
   - Assurez-vous que tous les tests passent
   - Documentez vos changements

5. **Tests et Validation**

   ```bash
   # Exécuter les tests
   pytest tests/
   
   # Vérifier le style de code
   black datalexir/
   flake8 datalexir/
   
   # Vérifier les types
   mypy datalexir/
   ```

6. **Commit et Push**

   ```bash
   git add .
   git commit -m "feat: description claire de la fonctionnalité"
   git push origin feature/ma-nouvelle-fonctionnalite
   ```

7. **Créer une Pull Request**
   - Allez sur GitHub et créez une Pull Request
   - Utilisez le template fourni
   - Décrivez clairement vos changements

## 📋 Standards de Code

### Style de Code

- **PEP 8** : Suivez les conventions Python standard
- **Black** : Utilisez Black pour le formatage automatique
- **Type Hints** : Ajoutez des annotations de type pour toutes les fonctions publiques
- **Docstrings** : Documentez toutes les classes et fonctions publiques

Exemple de fonction bien documentée :

```python
def process_sample(df: pd.DataFrame, sample_size: float = 0.3) -> pd.DataFrame:
    """
    Crée un échantillon aléatoire d'un DataFrame.
    
    Args:
        df: DataFrame source à échantillonner
        sample_size: Fraction du DataFrame à conserver (0.0 à 1.0)
        
    Returns:
        DataFrame échantillonné
        
    Raises:
        ValueError: Si sample_size n'est pas entre 0 et 1
        
    Example:
        >>> df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        >>> sample = process_sample(df, 0.6)
        >>> len(sample) <= len(df)
        True
    """
    if not 0 <= sample_size <= 1:
        raise ValueError("sample_size doit être entre 0 et 1")
    
    return df.sample(frac=sample_size)
```

### Convention de Nommage

- **Classes** : `PascalCase` (ex: `ElexbookProcessor`)
- **Fonctions/Méthodes** : `snake_case` (ex: `process_dataframe`)
- **Constantes** : `UPPER_SNAKE_CASE` (ex: `DEFAULT_SAMPLE_SIZE`)
- **Fichiers** : `snake_case.py` (ex: `data_processor.py`)

### Messages de Commit

Utilisez la convention [Conventional Commits](https://www.conventionalcommits.org/) :

```txt
type(scope): description

[corps optionnel]

[notes de bas de page optionnelles]
```

Types de commits :

- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: modification de documentation
- `style`: changements de formatage (espaces, points-virgules, etc.)
- `refactor`: refactoring du code
- `test`: ajout ou modification de tests
- `chore`: tâches de maintenance

Exemples :

```txt
feat(elexbook): ajouter support pour les DataFrames Polars
fix(elexdas): corriger la conversion des types datetime
docs: mettre à jour le guide d'installation
test(elexpark): ajouter tests pour les transformations Spark
```

## Tests

### Structure des Tests

```txt
tests/
├── unit/
│   ├── test_elexbook.py
│   ├── test_elexdas.py
│   └── test_elexpark.py
├── integration/
│   ├── test_pipeline_pandas.py
│   └── test_pipeline_spark.py
└── fixtures/
    ├── sample_data.csv
    └── test_datasets.py
```

### Écriture de Tests

```python
import pytest
import pandas as pd
from datalexir.elexbook import Elexbook


class TestElexbook:
    """Tests pour la classe Elexbook."""
    
    @pytest.fixture
    def sample_dataframe(self):
        """Fixture avec un DataFrame de test."""
        return pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': ['a', 'b', 'c', 'd', 'e'],
            'C': [1.1, 2.2, 3.3, 4.4, 5.5]
        })
    
    def test_elexbook_initialization(self, sample_dataframe):
        """Test l'initialisation d'Elexbook."""
        book = Elexbook(sample_dataframe, sample=0.6)
        
        assert isinstance(book.df, pd.DataFrame)
        assert isinstance(book.sample, pd.DataFrame)
        assert len(book.sample) <= len(sample_dataframe)
        assert book.history == []
    
    def test_sample_size_validation(self, sample_dataframe):
        """Test la validation de la taille d'échantillon."""
        with pytest.raises(ValueError):
            Elexbook(sample_dataframe, sample=1.5)
```

### Couverture de Code

Visez une couverture de code d'au moins 80% :

```bash
pytest --cov=datalexir --cov-report=html
```

## Documentation

### Documentation du Code

- **Docstrings** : Utilisez le format Google pour les docstrings
- **Type Hints** : Ajoutez des annotations de type partout
- **Exemples** : Incluez des exemples d'utilisation dans les docstrings

### Documentation Utilisateur

- **README** : Maintenez le README à jour
- **Notebooks** : Créez des notebooks de démonstration dans `notebooks/examples/`
- **Guide API** : Documentez toutes les API publiques

## Signalement de Bugs

Utilisez le template GitHub Issues pour signaler des bugs :

**Template Bug Report :**

```markdown
**Description du Bug**
Description claire et concise du problème.

**Reproduction**
Étapes pour reproduire le comportement :
1. Allez à '...'
2. Cliquez sur '....'
3. Faites défiler vers '....'
4. Voir l'erreur

**Comportement Attendu**
Description claire de ce qui devrait se passer.

**Captures d'Écran**
Si applicable, ajoutez des captures d'écran.

**Environnement:**
 - OS: [ex: Ubuntu 20.04]
 - Python: [ex: 3.9.7]
 - DataLexir: [ex: 1.2.3]
 - Pandas: [ex: 1.5.0]

**Contexte Supplémentaire**
Tout autre contexte utile pour le problème.
```

## Proposition de Fonctionnalités

Utilisez GitHub Discussions pour proposer de nouvelles fonctionnalités :

1. **Recherchez** s'il existe déjà une discussion similaire
2. **Décrivez** le problème que vous souhaitez résoudre
3. **Proposez** une solution avec des exemples d'utilisation
4. **Discutez** avec la communauté

## Communication

### Canaux de Communication

- **GitHub Issues** : Pour les bugs et demandes de fonctionnalités
- **GitHub Discussions** : Pour les questions et discussions générales
- **Pull Requests** : Pour les revues de code

### Code de Conduite

Nous attendons de tous les contributeurs qu'ils respectent notre code de conduite :

- **Soyez respectueux** : Traitez tous les membres de la communauté avec respect
- **Soyez constructif** : Donnez des feedbacks constructifs et utiles
- **Soyez collaboratif** : Travaillez ensemble vers des objectifs communs
- **Soyez inclusifs** : Accueillez les contributeurs de tous horizons

## Roadmap des Contributions

### Priorités Actuelles

1. **Construction du modèle** : Finaliser la structure de base et les fonctionnalités principales

### Domaines de Contribution Recherchés

- **Frontend/UX** : Amélioration des widgets interactifs
- **Performance** : Optimisation des algorithmes
- **Documentation** : Guides et tutoriels
- **Tests** : Création des tests unitaires et d'intégration

## Reconnaissance

Les contributeurs réguliers seront :

- **Mentionnés** dans les notes de version
- **Ajoutés** à la liste des contributeurs dans le README
- **Invités** à rejoindre l'équipe core si approprié

## Checklist pour les Pull Requests

Avant de soumettre votre PR, vérifiez :

- [ ] Les tests passent (`pytest`)
- [ ] Le code suit les standards de style (`black`, `flake8`)
- [ ] Les types sont correctement annotés (`mypy`)
- [ ] La documentation est mise à jour
- [ ] Les exemples fonctionnent
- [ ] Le changelog est mis à jour (si applicable)
- [ ] Les tests couvrent les nouvelles fonctionnalités

---

Merci encore pour votre contribution à DataLexir ! 🚀

Pour toute question, n'hésitez pas à ouvrir une discussion GitHub ou à contacter l'équipe de maintenance.
