"""
Welcome to the depreciator app
We will calculate the depreciation of an asset over a
number of years using straight line depreciation method
and other methods like double declining balance method 
and sum of years digits method
"""
import storage, calculator, display


def hello():
    print("Welcome to the depreciator app")
    print("We will calculate the depreciation of an asset over a")
    print("number of years using straight line depreciation method")
    print("and other methods like double declining balance method ")
    print("and sum of years digits method")
    print("CTRL + C to exit the app")

# Gets user input for asset details and depreciation method, no normalization
def get_user_input():
    item = input("Enter the name of the asset: ")
    cost = input("Enter the cost of the asset: ")
    salvage = input("Enter the salvage value of the asset: ")
    life = input("Enter the useful life of the asset in years: ")
    methods = ["straight line", "double declining balance", "sum of years digits", "sl", "ddb", "syd"]
    print(f"Available depreciation methods: {methods}")
    method = input("Enter the depreciation method: ")
    print("\n")
    return item, cost, salvage, life, method

# Assess user intent for adding new asset or accessing existing asset or quitting the app
def intent():
    intent = input("Do you want to add a new asset or access depreciation schedule for an existing asset? (add/access/quit/view/remove): ")
    if intent.lower() not in ["add", "access", "quit", "view", "remove"]:
        raise ValueError("Please type 'add' to add a new asset, 'access' to access depreciation schedule for an existing asset, 'view' to view all assets, 'remove' to remove an asset, or 'quit' to exit the app.")
    return intent.lower()

# Normalizes for storage and calculation
def normalize(item, cost, salvage, life, method):
    # Normalize the input values
    item = item.strip().lower()
    cost = float(cost.replace("$", ""))
    salvage = float(salvage.replace("$", ""))
    life = int(life)
    method = method.lower()
    return item, cost, salvage, life, method


def validate_input(item, cost, salvage, life, method):
    methods = ["straight line", "double declining balance", "sum of years digits", "sl", "ddb", "syd"]
    if method.lower() not in methods or float(life) <= 0 or float(cost) <= 0 or float(salvage) < 0 or float(salvage) >= float(cost):
        raise ValueError()
    

# User welcome and input
# Annoying thing I can't figure out is how to limit the degree to which the user is sent back in the flow of the app 
# when they make an error, I want them to be able to correct just the error and not have to re-enter all the data again, 
# but I also don't want to have a million nested try except blocks, so I'm not sure how to handle that yet. For now, I'm 
# just going to have it so that if they make an error, they have to start over from the beginning, but I'll come back and refactor that later.

def main():
    hello()
    while True:
        try:
            intention = intent()
            if intention == "add":
                item, cost, salvage, life, method = get_user_input()
                item, cost, salvage, life, method = normalize(item, cost, salvage, life, method)
                validate_input(item, cost, salvage, life, method)
                # Store the data
                storage.store_data(item, cost, salvage, life, method)
            elif intention == "access":
                checking = input("Enter the name of the asset to access depreciation schedule: ").lower()
                if storage.check_item(checking):
                    item, cost, salvage ,life, method = storage.retrieve_data(checking)
                    depreciation = calculator.calculate_depreciation(cost, salvage, life, method)    
                    # Display the results
                    display.display_depreciation(item.title(), depreciation)
                    return
                print("Asset not found, please try again.")
                continue
            elif intention == "view":
                assets = storage.view_assets()
                if not assets:
                    print("No assets found.")
                    continue
                print("Assets:")
                for asset in assets:
                    print(f"- {asset.title()}")
            elif intention == "remove":
                checking = input("Enter the name of the asset to remove: ").lower()
                if checking.lower() == "all":
                    confirm = input("Are you sure you want to remove all assets? (yes/no): ")
                    if confirm.lower() == "yes" or confirm.lower() == "y":
                        storage.remove_all_assets()
                        print("All assets removed successfully.")
                    else:
                        print("Operation cancelled.")
                    continue
                if storage.check_item(checking):
                    # Remove the asset from the CSV file
                    storage.remove_asset(checking)
                    print(f"Asset '{checking.title()}' removed successfully.")
                else:
                    print("Asset not found, please try again.")
                    continue
            elif intention == "quit":
                print("Goodbye!")
                return
            else:
                print("Invalid input, please try again.")
                raise ValueError()
        except (ValueError) as e:
            print(f"Error: {e}")
            pass
    
if __name__ == "__main__":
    main()
