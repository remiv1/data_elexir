import ipywidgets as widgets
from IPython.display import display

def assign_column_types_with_error_handling(df):
    type_widgets = {}
    for col in df.columns:
        type_widgets[col] = widgets.Dropdown(
            options=["int", "float", "str", "bool", "datetime"],
            description=col,
            value=str(df[col].dtype)
        )
    apply_button = widgets.Button(description="Appliquer")

    def apply_types(change):
        new_types = {}
        for col, widget in type_widgets.items():
            while True:
                try:
                    new_type = widget.value
                    new_types[col] = new_type
                    break
                except Exception as e:
                    print(f"Erreur lors de l'attribution du type pour la colonne '{col}': {e}")
        print("Nouveaux types attribués :", new_types)
        return df.astype(new_types)

    apply_button.on_click(apply_types)

    display(widgets.VBox(list(type_widgets.values()) + [apply_button]))