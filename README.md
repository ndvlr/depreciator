Depreciator

A simple Python depreciation calculator, currently for single assets in 
straight line depreciation, later for baskets of assets with varied depreciation
methods (double declining balance, sum of years' digits)

Inputs are Initial cost, salvage value, useful life, and depreciation method 
Output is a formatted depreciation schedule
Years are 1-indexed in accordance with financial and accounting convention

Req: 
Python 3.14
No external dependencies

Usage:
Run from the project directory
python depreciator.py
Follow prompts

Design notes:
Internal schedule uses dictionaries, later we will use lists of dictionaries for
multiple assets. 
Division of scope: 

    calculator.py: business logic (we will later switch depreciation methods halfway if advantageous as practice dictates)

    display_depreciation.py: display output (later this will be gui)

    storage.py: storage of information

    data/storage/depreciation_data.csv: actual data (for now we clear, later we will use this to store many items and call them up by name when user asks for them after storing them)




