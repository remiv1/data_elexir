from datalexir import Elexdas

# Initialisation
df = ...  # Votre DataFrame
elexdas = Elexdas(df)

# Construction du pipeline
elexdas.add_operation("dropna").add_operation("rename_columns", mapping={...})

# Exécution du pipeline
elexdas.execute_pipeline()

# Historique des opérations
print(elexdas.history)

elex = Elexdas(df)
elex.dropna().rename(columns={"Nom": "name"}).fillna(value=0)

print(elex.sample.head())       # Données nettoyées (échantillon)
print(elex.history)             # Log de toutes les opérations