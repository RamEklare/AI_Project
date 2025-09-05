from core.data_handler import find_patient, load_patients

class PatientAgent:
    def lookup_patient(self, first_name, last_name, dob):
        patient = find_patient(first_name, last_name, dob)
        if patient:
            return {"status": "returning", "patient": patient}
        else:
            return {"status": "new", "patient": None}
