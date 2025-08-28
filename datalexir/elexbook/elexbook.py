import pandas as pd
from .interactivity import assign_column_types_with_error_handling
from typing import Any, Dict, List, Tuple, Union, Self

class Elexbook:
    '''
    Class for interactive data exploration and visualization.
    This class is created to explore data in pandas DataFrames interactively.
    To use this class, you need to pass a pandas DataFrame and a sample fraction
    in a jupyter notebook environment.
    After initialization, you can use the methods of the pandas DataFrame
    on the sampled DataFrame, and the operations will be logged in the history.
    At the end, the methode `.concatbook()` will return the dictionary with the pipeline
    of operations performed on the DataFrame.
    This dictionary will be used with the Elexir class Elexdas (ELEXir panDAS) or with
    the class Elexpark (ELEXir sPARK).
    ---
    Structure of the Elexbook's operations:
    datalexir (bibliothèque)
    │
    ├── Elexbook (class)
    │   ├── opération 1
    │   ├── opération ...
    │   └── elexbook.concatbook()
    │       └── génération d'une fonction pipeline complète
    │
    ├── Elexdas
    │   └── elexdas.pipeline({op1: {[fonct1, fonct2, ...]: [param1, param2, ...]}})
    │
    └── Elexpark
        └── elexpark.pipeline({op1: {[fonct1, fonct2, ...]: [param1, param2, ...]}})
    ---
    :param df: DataFrame to be sampled and manipulated.
    :param sample: Fraction of the DataFrame to sample.
    ---
    :type df: pd.DataFrame
    :type sample: float
    ---
    :return: None
    :rtype: None
    ---
    Example:
    ```python
    import pandas as pd
    from datalexir.elexbook import Elexbook
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    elexbook = Elexbook(df, sample=0.3)
    ```
    '''
    # Initialization of the Elexbook class with a DataFrame and a sample fraction
    def __init__(self, df: pd.DataFrame, sample: float = 0.3) -> None:
        '''
        Initialization of the Elexbook class with a DataFrame and a sample fraction.
        ---
        :param df: DataFrame to be sampled and manipulated (except uniques values).
        :type df: pd.DataFrame
        :param sample: Fraction of the DataFrame to sample (default is 0.3).
        :type sample: float
        :param self: Instance of Elexbook containing the sample DataFrame.
        :type self: Elexbook
        ---
        :return: None
        :rtype: None
        ---
        Example:
        ```python
        import pandas as pd
        from datalexir.elexbook import Elexbook
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        elexbook = Elexbook(df, sample=0.3)
        ```
        '''
        self.df = df
        self.sample = df.sample(frac=sample)
        self.history: List[Dict[str, Any]] = []

    # Function to log operations performed on the DataFrame
    def _log(self, name: str, args: Tuple[str, Any | None], kwargs: Dict[str, Any]) -> None:
        '''
        Function to log operations performed on the DataFrame.
        ---
        :param name: Name of the operation performed.
        :type name: str
        :param args: Arguments passed to the operation.
        :type args: Tuple[str, Any | None]
        :param kwargs: Keyword arguments passed to the operation.
        :type kwargs: Dict[str, Any]
        :param self: Instance of Elexbook containing the sample DataFrame.
        :type self: Elexbook
        ---
        :return: None
        :rtype: None
        ---
        Example:
        ```python
        elexbook = Elexbook(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))
        elexbook._log('sample', ('frac', 0.3), {})
        ```
        '''
        self.history.append({"operation": name, "arguments": {"args": args, "kwargs": kwargs}})

    # Function to dynamically get attributes of the sample DataFrame
    def __getattr__(self, attr_name: str) -> Any:
        '''
        Function to dynamically get attributes of the sample DataFrame.
        ---
        :param attr_name: Name of the attribute to get.
        :type attr_name: str
        :param self: Instance of Elexbook containing the sample DataFrame.
        :type self: Elexbook
        ---
        :return: The attribute or a callable wrapper if the attribute is a method.
        :rtype: Any
        ---
        Example:
        ```python
        elexbook = Elexbook(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))
        elexbook.sample.head()  # Returns the first few rows of the sample DataFrame
        ```
        '''
        attr = getattr(self.sample, attr_name)
        if callable(attr):
            def wrapper(*args: Any, **kwargs: Any) -> Union[Self, Any]:
                result = attr(*args, **kwargs)
                self._log(attr_name, args, kwargs)
                if isinstance(result, type(self.sample)):
                    self.sample = result
                    return self
                return result
            return wrapper
        return attr
    
    # Assign column types dynamically with error handling
    def dynamic_type_assignment(self) -> None:
        '''
        Function for datascience to assign column types dynamically with error handling.
        ---
        :param self: Instance of Elexbook containing the sample DataFrame.
        :type self: Elexbook
        ---
        :return: None
        :rtype: None
        ---
        exemple:
        ```python
        elexbook.dynamic_type_assignment()
        ```
        '''
        return assign_column_types_with_error_handling(self.sample)

    # Concatenate the history of operations into a dictionary
    def concatbook(self) -> List[Dict[str, Dict[str, Any]]]:
        '''
        Concatenate the history of operations into a dictionary.
        ---
        :param self: Instance of Elexbook containing the sample DataFrame.
        :type self: Elexbook
        ---
        :return: Dictionary with the history of operations performed on the DataFrame.
        :rtype: Dict[str, Dict[str, Any]]
        ---
        Example:
        ```python
        # Exemple d'utilisation
        import pandas as pd
        from datalexir.elexbook import Elexbook

        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        elexbook = Elexbook(df, sample=1.0)

        # Effectuer des opérations
        elexbook.dropna()
        elexbook.fillna(0)
        elexbook.astype({'A': 'int'})

        # Générer la pipeline
        pipeline = elexbook.concatbook()
        print(pipeline)
        # Sortie attendue:
        # {
        #     'op1': {'dropna': []},
        #     'op2': {'fillna': [0]},
        #     'op3': {'astype': [{'A': 'int'}]}
        # }
        ```
        '''
        for op in self.history:
            if "arguments" not in op:
                op["arguments"] = {"args": (), "kwargs": {}}
        return [{"operation": op.get("operation", ""), 
                 "arguments": op.get("arguments", {"args": (), "kwargs": {}})}
                 for op in self.history]
    
    