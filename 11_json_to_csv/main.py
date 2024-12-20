import json
import csv

"""
    This script reads a JSON file and writes its content to a CSV file.
    The JSON file contains a list of dictionaries, each dictionary represents a person.
    The CSV file will have the following columns: name, age, email, street, city, state, zip.
"""

if __name__ == "__main__":
    with open("data.json", "r") as f:
        data = json.load(f)

    with open("data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "email", "street", "city", "state", "zip"])
        for item in data:
            writer.writerow(
                [
                    item["name"],
                    item["age"],
                    item["email"],
                    item["address"]["street"],
                    item["address"]["city"],
                    item["address"]["state"],
                    item["address"]["zip"],
                ]
            )

    with open("data.csv", "r") as f:
        print(f.read())