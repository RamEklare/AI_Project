from core.notifications import send_email, send_sms

class ReminderAgent:
    def send_reminder(self, patient, slot, reminder_number=1):
        message = f"Reminder {reminder_number}: Your appointment is at {slot}."
        send_email(patient['email'], "Appointment Reminder", message)
        send_sms(patient['phone'], message)
