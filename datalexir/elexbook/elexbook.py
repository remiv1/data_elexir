from .interactivity import assign_column_types_with_error_handling
import pandas as pd
from typing import List, Dict, Any
class Elexbook:
    def __init__(self, df: pd.DataFrame, sample: float=0.3):
        self.df = df
        self.sample: pd.DataFrame = df.sample(frac=sample)
        self.history: List[Dict[str, Any | None]] = []

    def _log(self, name: str, args: tuple[Any | None, ...], kwargs: Dict[str, Any | None]):
        self.history.append({"operation": name, "args": args, "kwargs": kwargs})

    def __getattr__(self, attr_name: str):
        attr = getattr(self.sample, attr_name)
        if callable(attr):
            def wrapper(*args: tuple[Any | None, ...], **kwargs: tuple[Any | None, ...]):
                result = attr(*args, **kwargs)
                self._log(attr_name, args, kwargs)
                if isinstance(result, type(self.sample)):
                    self.sample = result
                    return self
                return result
            return wrapper
        return attr
    
    def typage_interactif(self):
        return assign_column_types_with_error_handling(self.sample)
