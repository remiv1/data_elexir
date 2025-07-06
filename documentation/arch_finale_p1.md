**************************************
# Arborescence fonctionnelle du projet
**************************************
Cette arborescence décrit la structure du projet, facilitant la navigation et la compréhension de l'usage

```
datalexir (bibliothèque)
│
├── Elexbook (class)                                # Exploration des données (notebook Jupyter)
│   ├── opération 1
│   ├── opération 2
│   ├── opération 3
│   ├── opération ...
│   └── elexbook.concatbook()                       # Concaténation du notebook d'exploration
│       └── génération d'une fonction pipeline complète (cf ci-après)
│
├── Elexdas                                         # Gestion de données pandas (elexir_pandas)
│   └── elexdas.pipeline({op1: {[fonct1, fonct2, ...]: [param1, param2, ...]}})
│
└── Elexpark                                        # Gestion de données Spark (elexir_spark)
    └── elexpark.pipeline({op1: {[fonct1, fonct2, ...]: [param1, param2, ...]}})
```
**************************************
# Structure du dictionnaire de la pipeline
**************************************
Le dictionnaire de la pipeline est structuré de manière à organiser les opérations et les fonctions associées. Chaque opération est une clé du dictionnaire, et les valeurs sont des sous-dictionnaires contenant les fonctions et leurs paramètres. le pipeline est généré par la concaténation des notebooks d'exploration des données. Chaque opération peut contenir plusieurs fonctions, chacune avec ses propres paramètres. Voici un exemple de structure de pipeline :

```python
pipeline = {
    "op1": {
        "fonct1": [param1, param2, ...],
        "fonct2": [param1, param2, ...],
        ...
    },
    "op2": {
        "fonct1": [param1, param2, ...],
        "fonct2": [param1, param2, ...],
        ...
    },
    ...
}
```