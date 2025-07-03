**Voici une structure typique pour une bibliothèque comme Datalexir :

- Classes : pour les objets avec état ou logiques complexes (ex : TextCleaner, DataAuditPipeline).
- Fonctions : pour les opérations simples et pures (ex : remove_accents(text), plot_char_distribution(df)).
- Méthodes : dans les classes, bien sûr — ex. .clean(), .summarize(), .plot().

** exemples de fonctions :
- rename_columns(df, mapping) pour renommer proprement,
- resolve_duplicates(df) pour éviter les doublons embêtants,
- visualize (voir les modifications proposées)
- apply (appliquer les modifications)
- normalize_column(df, col) pour scaler élégamment tes données,
- validate_schema(df, schema) pour s’assurer que tout est conforme à tes attentes

** prévoir deux méthodes exploratoires :
- interactive dans la console (méthode input() pour le type colonne par colonne)
- interface riche avec ipywidget (ipython) avec des options cliquables de typage de colonne.