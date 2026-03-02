from __future__ import annotations #Per lavorare su classi ancora non definite
import re #Sarebbe Regex
from dataclasses import dataclass #Ci permette di utilizzare le classì come entità
from typing import Any, Dict, List, Optional, Tuple #Permette di tipizzare

import numpy as np
from numpy import dtype

@dataclass #Dice come deve essere tipizzato il mio record, e mi genera in automatico la classe.
class CleanRecord:
    age: int
    income: float
    debts: int
    credit_score: int
    approved: int

class FieldParser: #Classe parsing sanificazione dati, convertendo i dati in numeri e gestendo i formati.

    #Chiede in ingresso dei float, e chiedo di restituire, possibilmente int. Funge anche da documentazione.
    def parse_int(self, value: Any) ->Optional[int]:
        if value is None:
            return None

        if isinstance(value, str):
            txt = value.strip() #Tolgo spazi superflui.
            if txt == "" or txt.lower() in {"n/a", "na", "??"}:
                return None
            #Ora faccio la Regex, per tenermi le stringhe di numeri interi e con i segni meno
            #E sostituire il resto con stringa vuota.
            txt = re.sub(r"[^\d\-]", "", txt)
            if txt == "" or txt == "-":
                return None

            try:
                return int(txt)
            except ValueError:
                return None

        if isinstance(value, (int, np.integer)):
            return int(value)

        return None

    #Ora cerco di convertire i valori tipo monetizzazione, valuta, virgola mobile, eccetera
    def parse_income(self, value: Any) -> Optional[float]:
        if value is None:
            return None

        if isinstance(value, (int, float, np.integer, np.floating)):
            income = float(value)
            return income

        if not isinstance(value, str):
            return None

        #Passati gli if precedenti, deve essere PER FORZA una stringa.
        txt = value.strip().lower()

        if txt in {"", "n/a", "na", "??"}:
            return None

        #Se la Regex qui sotto mi fa il match con k finale tutto corretto, e mi restituisce True.
        k_match = re.fullmatch(r"([-+]?\d+)\s*k", txt)
        if k_match:
            return float(k_match.group(1)) * 1000.0 #group 1 è la parentesi tonda della Regex

        txt = txt.replace("€", "").replace(" ", "").replace(".","")
        try:
            return float(txt)
        except ValueError:
            return None

    #Ora devo controllare e convertire gli yes, no, true, false in 1 e 0
    def parse_approved(self, value: Any) -> Optional[int]:
        if value is None:
            return None

        if isinstance(value, (int, np.integer)):
            if int(value) in (0, 1):
                return int(value)
            return None

        if not isinstance(value, str):
            return None

        txt = value.strip().lower()

        if txt in {"1", "yes", "y", "si", "sì", "t", "true"}:
            return 1

        if txt in {"0", "no", "n", "f", "false"}:
            return 0

        return None

#Questo mi valida i dati
class RecordValidator:
    def is_valid(self, rec: CleanRecord) -> bool:
        if rec.age < 18 or rec.age > 99:
            return False

        if rec.income < 0:
            return False

        if rec.debts < 0 or rec.debts > 50:
            return False

        if rec.credit_score < 300 or rec.credit_score > 850:
            return False

        if rec.approved not in (0,1):
            return False

        return True

#Ora tocca trasformare i dati in matrice.
class PreprocessPipeline:
    def __init__(self, parser: FieldParser, validator: RecordValidator):
        self.parser = parser
        self.validator = validator
        self.dropped_records: int = 0
        self.kept_records: int = 0

    def clean_records(self, raw_records: List[Dict[str, Any]]) -> List[CleanRecord]:
        cleaned: List[CleanRecord] = []
        for row in raw_records:
            age = self.parser.parse_int(row.get("age"))
            income = self.parser.parse_income(row.get("income"))
            debts = self.parser.parse_int(row.get("debts"))
            credit_score = self.parser.parse_int(row.get("credit_score"))
            approved = self.parser.parse_approved(row.get("approved"))

            if None in (age, income, debts, credit_score, approved):
                self.dropped_records += 1
                continue

            rec = CleanRecord(
                age = int(age),
                income = float(income),
                debts = int(debts),
                credit_score = int(credit_score),
                approved = int(approved)
            )

            if not self.validator.is_valid(rec):
                self.dropped_records += 1
                continue

            cleaned.append(rec)
            self.kept_records += 1

        return cleaned

    #Ora mi creo le due matrici
    def build_xy(self, cleaned: List[CleanRecord]) -> Tuple[np.ndarray, np.ndarray]:
        X = np.array(
                [[r.age, r.income, r.debts, r.credit_score] for r in cleaned], dtype = float
        )

        y = np.array(
            [r.approved for r in cleaned], dtype = int
        )
        return X, y

    def add_feature_engineering(self, X: np.ndarray) -> np.ndarray:
        income = X[:, 1]
        debts = X[:, 2]
        debt_to_income = debts / income
        debt_to_income = debt_to_income.reshape(-1, 1)
        X_enhanced = np.hstack((X, debt_to_income))
        return X_enhanced

    def minmax_normalize(self, X: np.ndarray) -> np.ndarray:
        min_col = np.min(X, axis = 0)
        max_col = np.max(X, axis = 0)
        denom = max_col - min_col
        denom[denom == 0] = 1.0
        X_norm = (X - min_col) / denom
        return X_norm

    def train_test_split(
            self,
            X: np.ndarray,
            y: np.ndarray,
            train_ratio: float = 0.8,
            seed: int = 42
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: #2 di train e 2 di test.
        idx = np.arange(len(X))
        rng = np.random.default_rng(seed)
        rng.shuffle(idx)
        train_size = int(len(idx) * train_ratio)
        train_idx = idx[:train_size]
        test_idx = idx[train_size:]

        X_train = X[train_idx]
        X_test = X[test_idx]
        y_train = y[train_idx]
        y_test = y[test_idx]

        return X_train, X_test, y_train, y_test