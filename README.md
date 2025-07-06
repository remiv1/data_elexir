# Data Elexir

## Description
- Une API expressive et intuitive pour le nettoyage de texte/données
- Une intégration fluide avec Pandas
- Une chaînabilité élégante façon `.strip().lower().remove_accents()`
- Des outils pour concaténer, tracer, auditer les transformations
- Une philosophie modulaire : tu ajoutes tes propres briques facilement
On serait donc clairement en terrain innovant, avec un vrai positionnement entre ergonomie, lisibilité et puissance.


## Installation
```bash
# Clone le dépôt
git clone <url-du-repo>
cd data_elexir
# Installe les dépendances
pip install -r requirements.txt
```

## Utilisation
Le pojet est de faciliter la vie de la datascience en chaînant les commandes.
Le projet devra aboutir à une distribution pypi.

## Structure du projet à compléter
```
datalexir/
    elexbook/
        exploration/
            visualisation           # Visualisation de la donnée
            interactif              # Gestion interactive sur notebook 
        nettoyage/
            texte
            float_int
            time_date
        conversion/
            texte
            float_int
            time_date
        batch/
            objets
            dataframe
        echantillons/
            nb
            %
        pipelinisation/
            recupération/dict_retour      
    elexdas/
        nettoyage/
        conversion/
        batch/
    elexpark/
        nettoyage/
        conversion/
        batch/
notebooks/
test/
```

## Documentation
Voir le dossier `documentation/` pour plus de détails.

## Contribuer
Je souhaite monter une équipe pour un projet opensource.

## Auteurs
- Rémi Verschuur (remiv1/data-fan)

## Licence
A venir
