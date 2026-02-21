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
    with open("depreciation_data.csv", "a", newline='') as file:
        depreciation_writer = csv.writer(file, delimiter=",", quotechar="\"")
        depreciation_writer.writerow([item, cost, salvage, life, method])
    

