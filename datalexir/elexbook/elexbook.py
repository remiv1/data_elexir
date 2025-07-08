from .interactivity import assign_column_types_with_error_handling

class Elexbook:
    def __init__(self, df, sample=0.3):
        self.df = df
        self.sample = df.sample(frac=sample)
        self.history = []

    def _log(self, name, args, kwargs):
        self.history.append({"operation": name, "args": args, "kwargs": kwargs})

    def __getattr__(self, attr_name):
        attr = getattr(self.sample, attr_name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                self._log(attr_name, args, kwargs)
                if isinstance(result, type(self.sample)):
                    self.sample = result
                    return self
                return result
            return wrapper
        return attr
    
    def typage_interactif(self):
        from .interactivity import assign_column_types_with_error_handling
        return assign_column_types_with_error_handling(self.sample)
