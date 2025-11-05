# test_loader.py
from utilis.data_loader import load_medical_data, create_patients

if __name__ == "__main__":
    df = load_medical_data("data/medical_data.csv")
    patients = create_patients(df)

    # afficher les 3 premiers patients pour vérification
    for p in patients[:3]:
        print(p)