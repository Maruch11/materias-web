import csv

def get_subjects_by_career(career_id):
    subject = []

    with open("data/subjects.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            
            career_id_csv = int(row["career_id"])
            if career_id == career_id_csv:
                subject.append(row)

    return subject