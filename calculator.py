"""
Calculator for depreciation methods.
"""

def calculate_depreciation(cost, salvage, life, method):
    depreciation_schedule = {}
    if method.lower() == "straight line" or method.lower() == "sl":
        annual_depreciation = (cost - salvage) / life
        for year in range(1, life + 1):
            depreciation_schedule[year] = annual_depreciation
    elif method.lower() == "double declining balance" or method.lower() == "ddb":
        book_value = cost
        for year in range(1, life + 1):
            depreciation = min(book_value * (2 / life), book_value - salvage)
            depreciation_schedule[year] = depreciation
            book_value -= depreciation
    elif method.lower() == "sum of years digits" or method.lower() == "syd":
        sum_of_years = sum(range(1, life + 1))
        for year in range(1, life + 1):
            depreciation = (life - (year - 1)) / sum_of_years * (cost - salvage)
            depreciation_schedule[year] = depreciation
    else:
        raise ValueError("Invalid depreciation method")
    
    return depreciation_schedule