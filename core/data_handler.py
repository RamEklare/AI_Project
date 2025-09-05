import pandas as pd

PATIENT_FILE = "./data/patients_sample_50.csv"
DOCTOR_FILE = "./data/doctor_schedules_sample.xlsx"

def load_patients():
    df = pd.read_csv(PATIENT_FILE)
    return df

def load_doctors():
    df = pd.read_excel(DOCTOR_FILE)
    return df

def find_patient(first_name, last_name, dob):
    df = load_patients()
    match = df[
        (df['first_name'].str.lower() == first_name.lower()) &
        (df['last_name'].str.lower() == last_name.lower()) &
        (df['dob'] == dob)
    ]
    if not match.empty:
        return match.iloc[0].to_dict()
    return None
