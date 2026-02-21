"""
Welcome to the depreciator app
We will calculate the depreciation of an asset over a
number of years using straight line depreciation method
and other methods like double declining balance method 
and sum of years digits method
"""
import storage, calculator, display

# User welcome and input
def main():
    hello()
    item = input("Enter the name of the asset: ")
    cost = float(input("Enter the cost of the asset: "))
    salvage = float(input("Enter the salvage value of the asset: "))
    life = int(input("Enter the useful life of the asset in years: "))
    method = input("Enter the depreciation method (straight line, \
                   double declining balance, sum of years digits): ")
    # Store the data
    storage.store_data(item, cost, salvage, life, method)
    # Calculate the depreciation; returns a dict 
    depreciation = calculator.calculate_depreciation(cost, salvage, life, method)
    # Display the results
    display.display_depreciation(item, depreciation)


def hello():
    print("Welcome to the depreciator app")
    print("We will calculate the depreciation of an asset over a")
    print("number of years using straight line depreciation method")
    print("and other methods like double declining balance method ")
    print("and sum of years digits method")

    
if __name__ == "__main__":
    main()
