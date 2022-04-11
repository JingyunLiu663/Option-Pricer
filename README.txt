Group 5 - Option Pricer

Please refer to the group5.pdf file for the report.

To use the option pricer:
1. install the requirements first:
   pip install -r requirements.txt

2. run the GUI.py script.
   To select an option pricing method:
   a. The top menu is ONLY available for Windows OS;
   b. The homepage is available for both MacOS and Windows OS.

   Attention:
   a. For MacOS users, some input boxes may not have a solid outline, but this will not affect the use of the input boxes.
   b. For all the method based on Monte Carlo Simulation, the user has to explicitly specify the "MC Path No." (normally fill in 100000),
      otherwise there will be an "input format" error message.

The classes and functions for option pricing:
1. EuropeanOption.py
2. geometric_asian_basket.py
3. arithmetic_asian_mc.py
4. arithmetic_basket_mc.py
5. binomial_tree_american.py

The other python scripts is used for testing purpose either for the GUI or for the analysis for option pricer functions

The 2 csv files are the price results of the test cases given in the assignment's instructions.