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
            

def view_assets():
    assets = []
    try:
        with open("data/depreciation_data.csv", "r") as file:
            depreciation_reader = csv.reader(file, delimiter=",", quotechar="\"")
            for row in depreciation_reader:
                assets.append(row[0])
    except FileNotFoundError:
        return []
    return assets


def remove_asset(x):
    lines = []
    with open("data/depreciation_data.csv", "r") as file:
        depreciation_reader = csv.reader(file, delimiter=",", quotechar="\"")
        for row in depreciation_reader:
            if row[0] != x:
                lines.append(row)
    with open("data/depreciation_data.csv", "w", newline='') as file:
        depreciation_writer = csv.writer(file, delimiter=",", quotechar="\"")
        depreciation_writer.writerows(lines)


def remove_all_assets():
    with open("data/depreciation_data.csv", "w", newline='') as file:
        pass  # This will effectively clear the file
