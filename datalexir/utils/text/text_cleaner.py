# datalexir/cleaners/text_cleaner.py

import pandas as pd
import unicodedata
import re

class TextCleaner:
    '''
    Classe d'objet pour le nettoyage de données textuelles dans une série Pandas.
    Permet de nettoyer les chaînes de caractères en supprimant les espaces, en mettant en minuscules,
    en supprimant les accents et les chiffres, et en appliquant d'autres transformations.
    '''
    def __init__(self, series: pd.Series):
        self.series = series.copy()

    def strip(self, columns: str | list[str] | None = None):
        if columns:
            if isinstance(columns, list):
                for column in columns:
                    self.series[column] = self.series[column].str.strip()   # type: ignore
            else:
                self.series[columns] = self.series[columns].str.strip()     # type: ignore
        else:
            self.series = self.series.str.strip()
        return self

    def lower(self, columns: str | list[str] | None = None):
        if columns:
            if isinstance(columns, list):
                for column in columns:
                    self.series[column] = self.series[column].str.lower()   # type: ignore
            else:
                self.series[columns] = self.series[columns].str.lower()     # type: ignore
        else:
            self.series = self.series.str.lower()
        return self

    def remove_accents(self, columns: str | list[str] | None = None):
        if columns:
            if isinstance(columns, list):
                for column in columns:
                    self.series[column] = self.series[column].apply(        # type: ignore
                        lambda text: ''.join(
                            c for c in unicodedata.normalize('NFD', text)
                            if unicodedata.category(c) != 'Mn'
                        )
                    )
            else:
                self.series[columns] = self.series[columns].apply(          # type: ignore
                    lambda text: ''.join(
                        c for c in unicodedata.normalize('NFD', text)
                        if unicodedata.category(c) != 'Mn'
                    )
                )
        else:
            self.series = self.series.apply(
                lambda text: ''.join(
                    c for c in unicodedata.normalize('NFD', text)
                    if unicodedata.category(c) != 'Mn'
                )
            )
        return self

    def remove_digits(self, columns: str | list[str] | None = None):
        if columns:
            if isinstance(columns, list):
                for column in columns:
                    self.series[column] = self.series[column].apply(lambda x: re.sub(r'\d+', '', x))    # type: ignore
            else:
                self.series[columns] = self.series[columns].apply(lambda x: re.sub(r'\d+', '', x))    # type: ignore
        else:
            self.series = self.series.apply(lambda x: re.sub(r'\d+', '', x))
        return self

    def get(self):
        return self.series