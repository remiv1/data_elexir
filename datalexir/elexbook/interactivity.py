import ipywidgets as widgets    # type: ignore
from IPython.display import display # type: ignore
import pandas as pd
from typing import Any

def assign_column_types_with_error_handling(df: pd.DataFrame):
    type_widgets = {}
    for col in df.columns:
        type_widgets[col] = widgets.Dropdown(
            options=["int", "float", "str", "bool", "datetime"],
            description=col,
            value=str(df[col].dtype)
        )
    apply_button = widgets.Button(description="Appliquer")

    def apply_types(change: Any):
        new_types = {}
        for col, widget in type_widgets.items():    # type: ignore
            while True:
                try:
                    new_type = widget.value # type: ignore
                    new_types[col] = new_type
                    break
                except Exception as e:
                    print(f"Erreur lors de l'attribution du type pour la colonne '{col}': {e}")
        print("Nouveaux types attribués :", new_types)      # type: ignore
        return df.astype(new_types) # type: ignore

    apply_button.on_click(apply_types)

    display(widgets.VBox(list(type_widgets.values()) + [apply_button])) # type: ignore