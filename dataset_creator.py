import csv
import random

# Setup
RECORDS_PER_DISEASE = 500
FILENAME = "new_dset.csv"

# Expanded medical baselines with a larger pool of symptoms
diseases_config = {
    "Fever": {
        "temp_range": (99.0, 102.0),
        "sbp_range": (110, 130), "dbp_range": (70, 85),
        "symptoms": ["Chills", "Headache", "Sweating", "Muscle Ache", "Fatigue", "Loss of Appetite", "Shivering", "Dehydration", "Weakness"]
    },
    "Typhoid": {
        "temp_range": (101.0, 104.5),
        "sbp_range": (100, 120), "dbp_range": (60, 80),
        "symptoms": ["High Fever", "Abdominal Pain", "Weakness", "Rose Spots", "Constipation", "Dry Cough", "Bloating", "Lethargy", "Diarrhea"]
    },
    "Malaria": {
        "temp_range": (101.0, 105.0),
        "sbp_range": (100, 120), "dbp_range": (60, 80),
        "symptoms": ["Chills", "High Fever", "Sweating", "Nausea", "Vomiting", "Headache", "Muscle Pain", "Fatigue", "Mild Cough"]
    },
    "Appendicitis": {
        "temp_range": (99.0, 101.5),
        "sbp_range": (110, 140), "dbp_range": (70, 90),
        "symptoms": ["Right Lower Abdominal Pain", "Nausea", "Vomiting", "Loss of Appetite", "Low Grade Fever", "Constipation", "Inability to Pass Gas", "Abdominal Swelling"]
    },
    "Dengue": {
        "temp_range": (102.0, 105.0),
        "sbp_range": (90, 115), "dbp_range": (60, 75),
        "symptoms": ["Sudden High Fever", "Severe Joint Pain", "Rash", "Eye Pain", "Easy Bruising", "Nausea", "Vomiting", "Fatigue", "Mild Bleeding"]
    },
    "Chicken Pox": {
        "temp_range": (99.0, 102.5),
        "sbp_range": (110, 125), "dbp_range": (70, 80),
        "symptoms": ["Itchy Blisters", "Fever", "Fatigue", "Loss of Appetite", "Headache", "Red Spots", "Scabs", "Malaise", "Sore Throat"]
    },
    "Diarrhea": {
        "temp_range": (98.0, 100.5),
        "sbp_range": (90, 115), "dbp_range": (60, 75),
        "symptoms": ["Loose Stools", "Abdominal Cramps", "Nausea", "Dehydration", "Bloating", "Urgency to Defecate", "Mild Fever", "Dizziness"]
    }
}

# Generate the CSV
with open(FILENAME, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write Headers
    writer.writerow([
        "Age", "Sex", "Temperature", "Systolic_BP", "Diastolic_BP", 
        "Symptom_1", "Symptom_2", "Symptom_3", "Symptom_4", "Diagnosis"
    ])
    
    # Write Data
    for diagnosis, details in diseases_config.items():
        for _ in range(RECORDS_PER_DISEASE):
            age = random.randint(5, 75)
            sex = random.choice(["M", "F"])
            temp = round(random.uniform(*details["temp_range"]), 1)
            sbp = random.randint(*details["sbp_range"])
            dbp = random.randint(*details["dbp_range"])
            
            # Use random.sample() to pick EXACTLY 4 unique symptoms from the pool
            selected_symptoms = random.sample(details["symptoms"], 4)
            
            # Write the row
            writer.writerow([age, sex, temp, sbp, dbp] + selected_symptoms + [diagnosis])

print(f"Success! Saved dataset to '{FILENAME}' with {RECORDS_PER_DISEASE * len(diseases_config)} total records.")