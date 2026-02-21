"""
Storage functions.
"""
import csv

def store_data(item, cost, salvage, life, method):
    # In a real application, this would store data in a database or file
    print("\nStoring the following data:")
    print(f"Asset: {item}")
    print(f"Cost: {cost}")
    print(f"Salvage Value: {salvage}")
    print(f"Useful Life: {life} years")
    print(f"Depreciation Method: {method}\n")
    with open("data/depreciation_data.csv", "a", newline='') as file:
        depreciation_writer = csv.writer(file, delimiter=",", quotechar="\"")
        depreciation_writer.writerow([item, cost, salvage, life, method])


def check_item(item):
    try:
        with open("data/depreciation_data.csv", "r") as file:
            depreciation_reader = csv.reader(file, delimiter=",", quotechar="\"")
            for row in depreciation_reader:
                if row[0] == item:
                    return True
    except FileNotFoundError:
        return False
    return False


def retrieve_data(x):
    with open("data/depreciation_data.csv", "r") as file:
        depreciation_reader = csv.reader(file, delimiter=",", quotechar="\"")
        for row in depreciation_reader:
            if row[0] == x:
                return row[0], float(row[1]), float(row[2]), int(row[3]), row[4]

