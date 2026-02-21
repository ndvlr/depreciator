""" 
This file handles the display of the app,
and later including user input and output.
That will be a refactoring test
"""
# NEEDS a display function to display all available assets in the stored database


def display_depreciation(item, depreciation):
    print(f"\nDepreciation schedule for {item}:")
    for year, amount in depreciation.items():
        print(f"Year {year}: ${amount:.2f}")