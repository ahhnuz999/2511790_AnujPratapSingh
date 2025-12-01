import matplotlib.pyplot as plt
 # Task 1


time_data = [
    (3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
    (4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
    (5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
    (3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
    (4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]

low = []        
moderate = []   
high = []       


for study, ent, sleep in time_data:
    if study < 3:
        low.append(study)
    elif 3 <= study <= 5:
        moderate.append(study)
    else:
        high.append(study)

print("Low study time:", low)
print("Moderate study time:", moderate)
print("High study time:", high)


# Task 2:

print("Days with LOW study time:", len(low))
print("Days with MODERATE study time:", len(moderate))
print("Days with HIGH study time:", len(high))


# Task 3:

study_minutes =[]

for study, ent, sleep in time_data:
    study_minutes.append(study*60)

print("Study minutes:", study_minutes)

# Task 4:

study_hours =[]
entertainment_hours = []
sleep_hours = []

for study, ent, sleep in time_data:
    study_hours.append(study)
    entertainment_hours.append(ent)
    sleep_hours.append(sleep)

avg_study = sum(study_hours)/len(study_hours)
avg_ent = sum(entertainment_hours) / len(entertainment_hours)
avg_sleep = sum(sleep_hours) / len(sleep_hours)

# Task 5:

plt.scatter(study_hours, sleep_hours)
plt.xlabel("Study Hours")
plt.ylabel("Sleep Hours")
plt.title("Study vs Sleep Pattern")
plt.show()

