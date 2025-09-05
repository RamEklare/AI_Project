from core.data_handler import load_doctors
from core.appointment_logic import generate_slots

class SchedulingAgent:
    def get_doctor_availability(self, doctor_name, duration_mins=30):
        # For simplicity, assume all doctors are available 09:00-17:00
        slots = generate_slots(duration_mins=duration_mins)
        return slots

    def book_appointment(self, patient, doctor_name, slot):
        # Here you can save to Excel or DB
        print(f"Booking for {patient['first_name']} with Dr. {doctor_name} at {slot}")
        return True
