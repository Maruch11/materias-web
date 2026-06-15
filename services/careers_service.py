import csv


def get_careers():
    careers = []

    with open("data/careers.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            careers.append(row)

    return careers