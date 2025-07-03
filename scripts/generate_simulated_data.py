import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------
# ACTIVITY POOL 
# -----------------------------
activities = [
    ("Take medicine", "Bedroom", "Health", 1),
    ("Brush teeth", "Bathroom", "Hygiene", 0),
    ("Eat breakfast", "Kitchen", "Meal", 1),
    ("Watch TV", "Living Room", "Leisure", 0),
    ("Call daughter", "Living Room", "Social", 1),
    ("Take a walk", "Garden", "Physical", 0),
    ("Eat lunch", "Kitchen", "Meal", 1),
    ("Nap", "Bedroom", "Rest", 0),
    ("Read book", "Living Room", "Mental", 0),
    ("Eat dinner", "Dining Room", "Meal", 1),
    ("Prepare for bed", "Bedroom", "Routine", 0)
]

def generate_routines(user_id, start_date, days=7):
    rows = []
    for day in range(days):
        base_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=day)
        time_cursor = base_date.replace(hour=7, minute=0)

        # Randomly decide number of activities (simulate variation)
        num_activities = random.randint(5, 8)
        sampled_activities = random.sample(activities, num_activities)

        for act in sampled_activities:
            # Simulate time drift: ± 15 minutes
            time_drift = timedelta(minutes=random.randint(-15, 15))
            activity_time = time_cursor + time_drift
            time_str = activity_time.strftime("%H:%M")

            # 10–20% chance the person skips or forgets an activity
            if random.random() < 0.15:
                continue  # skip this activity

            # 5% chance to repeat an activity
            repeat = 1 if random.random() < 0.05 else 0

            for _ in range(1 + repeat):
                rows.append([
                    user_id,
                    activity_time.strftime("%Y-%m-%d"),
                    time_str,
                    act[0],  # activity name
                    act[1],  # location
                    act[2],  # reminder type
                    act[3]   # reminder_needed (label)
                ])

            # Move time cursor
            time_cursor = activity_time + timedelta(minutes=random.randint(45, 90))

    return rows

# -----------------------------
# Main: Generate for Multiple Users
# -----------------------------
all_data = []
for user_id in range(1, 6):  # simulate 5 users
    user_data = generate_routines(user_id=user_id, start_date="2025-07-01", days=10)
    all_data.extend(user_data)

# -----------------------------
# Save to CSV
# -----------------------------
df = pd.DataFrame(all_data, columns=[
    "user_id", "date", "time", "activity", "location", "reminder_type", "reminder_needed"
])
df.to_csv("C:/Users/pc/AndroidStudioProjects/ARAPP/data/simulated_routines.csv", index=False)

print("Simulated routine dataset saved to /data/simulated_routines.csv")
