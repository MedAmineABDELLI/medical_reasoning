# knowledge/base_classes.py

class Patient:
    """
    Représente un patient et ses informations médicales.
    """
    def __init__(self, pid: int, age: int, sex: str, lab_results: dict, disease: str = None):
        self.id = pid
        self.age = age
        self.sex = sex
        self.lab_results = lab_results      # ex: {"blood_pressure": 140, "creatinine": 1.2, "protein": 3.4}
        self.disease = disease              # étiquette connue, ex: "yes" ou "no"

    def __repr__(self):
        return f"Patient(id={self.id}, age={self.age}, sex='{self.sex}', lab_results={self.lab_results}, disease={self.disease})"


class Symptom:
    """
    Optionnelle : représente un symptôme et éventuellement son intensité.
    """
    def __init__(self, name: str, severity: float = None):
        self.name = name
        self.severity = severity

    def __repr__(self):
        return f"Symptom(name='{self.name}', severity={self.severity})"


class Disease:
    """
    Représente une maladie et un niveau de risque (utile pour la logique floue).
    """
    def __init__(self, name: str, risk_level: float = 0.0):
        self.name = name
        self.risk_level = risk_level

    def __repr__(self):
        return f"Disease(name='{self.name}', risk_level={self.risk_level})"
