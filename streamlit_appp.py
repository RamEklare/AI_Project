import streamlit as st
from agents.patient_agent import PatientAgent
from agents.scheduling_agent import SchedulingAgent
from agents.reminder_agent import ReminderAgent
from core.data_handler import load_doctors

st.title("Medical Appointment Scheduling AI Agent")

patient_agent = PatientAgent()
scheduling_agent = SchedulingAgent()
reminder_agent = ReminderAgent()

# Step 1: Collect patient info
st.header("Patient Information")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
dob = st.text_input("DOB (YYYY-MM-DD)")

if st.button("Check Patient"):
    result = patient_agent.lookup_patient(first_name, last_name, dob)
    st.write(result)

# Step 2: Doctor selection
st.header("Doctor Selection")
doctors = load_doctors()
doctor_name = st.selectbox("Select Doctor", doctors['doctor_name'].tolist())

# Step 3: Appointment slot selection
duration = 60 if result.get("status") == "new" else 30
slots = scheduling_agent.get_doctor_availability(doctor_name, duration_mins=duration)
slot = st.selectbox("Select Slot", [f"{s[0]} - {s[1]}" for s in slots])

# Step 4: Confirm Appointment
if st.button("Book Appointment"):
    patient_data = result.get("patient", {"first_name": first_name, "email": "test@test.com", "phone": "1234567890"})
    success = scheduling_agent.book_appointment(patient_data, doctor_name, slot)
    if success:
        st.success(f"Appointment booked for {first_name} with Dr. {doctor_name} at {slot}")
        reminder_agent.send_reminder(patient_data, slot, reminder_number=1)
