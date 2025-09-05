from datetime import datetime, timedelta

def generate_slots(start_time="09:00", end_time="17:00", duration_mins=30):
    slots = []
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    while start + timedelta(minutes=duration_mins) <= end:
        slot_start = start.strftime("%H:%M")
        slot_end = (start + timedelta(minutes=duration_mins)).strftime("%H:%M")
        slots.append((slot_start, slot_end))
        start += timedelta(minutes=duration_mins)
    return slots
