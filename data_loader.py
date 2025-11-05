import re
import pandas as pd
from knowledge.base_classes import Patient

def load_medical_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    
    # ✅ Nettoyer les noms de colonnes
    df.columns = (
        df.columns.str.strip()                # enlever les espaces
                 .str.lower()                 # tout en minuscules
                 .str.replace(' ', '_')       # remplacer espaces par _
                 .str.replace(r'\(.*?\)', '', regex=True)  # enlever tout ce qu'il y a entre parenthèses
                 .str.replace('-', '_')       # remplacer tirets par _
    )
    
    print(f"[INFO] {len(df)} lignes chargées depuis {filepath}")
    print("[DEBUG] Colonnes nettoyées :", list(df.columns[:10]), "...")
    return df

def analyze_medical_data(df: pd.DataFrame):
    """
    Analyse rapide des données pour identifier les features importantes.
    Retourne une liste de colonnes pertinentes.
    """
    print("\n[INFO] Analyse des colonnes disponibles...")
    print(f"Nombre total de colonnes : {len(df.columns)}")
    
    # Exemple d'aperçu statistique
    print("\n[STATS] Aperçu des valeurs numériques :")
    print(df.describe().T[["mean", "std", "min", "max"]].head(10))
    
    # Features pertinentes selon notre analyse
    important_features = [
        "bun", "cr", "24_hour_urine_copper", "cp",
        "alt", "ast", "tbil", "dbil", "ggt", "alb",
        "cirrhosis", "ascites", "thalamus_damage",
        "brainstem_damage", "liver_capsule_smoothing",
        "psychiatric_symptom_score", "liver_symptom_score",
        "age", "gender", "label"
    ]
    
    # Filtrer celles qui existent vraiment
    important_features = [f for f in important_features if f in df.columns]
    print(f"\n[INFO] {len(important_features)} features pertinentes retenues : {important_features}")
    
    return important_features


def create_patients_from_features(df: pd.DataFrame, features: list[float]) -> list[Patient]:
    """
    Crée des patients en utilisant uniquement les colonnes sélectionnées.
    """
    patients = []
    for idx, row in df.iterrows():
        lab_results = {f: float(row[f]) if pd.notna(row[f]) else None for f in features if f not in ["age", "gender", "label"]}
        
        patient = Patient(
            pid=int(idx),
            age=int(row["age"]) if pd.notna(row["age"]) else None,
            sex=int(row["gender"]) if pd.notna(row["gender"]) else None,
            lab_results=lab_results,
            disease=int(row["label"]) if pd.notna(row["label"]) else None
        )
        patients.append(patient)
    
    print(f"[INFO] {len(patients)} patients créés avec les features pertinentes.")
    return patients





df = load_medical_data("data/medical_data.csv")
patients = create_patients_from_features(df, analyze_medical_data(df))
print(f"[INFO] Exemple de patient : {patients[0]}")