*************
Instructions:
*************

1.) Open Mastermind_CPU.xlsx

2.) Enter desired simulation runs in cell "B2"

3.) Press 'Run Simulation' 

4.) Wait for python script to execute (You can monitor its progress in the command prompt that appears)

5.) Press 'Refresh Data' to update the tables and graphs

6.) Press 'Fix Columns' to re-adjust column formatting (a bit of a hack fix)

	i.) Number of attempts to solve is plotted along with various statistics

	ii.) A game viewer is located below the plot. Select a game by clicking
	the drop-down menu at cell "B33", labelled 'Game'



*******
NOTES:
*******
	* 	The VBA macro 'RunSim' that launches the python script has a variable 'python_path' which must 
	be set to the directory containing 'python.exe'. If the directory is in your Windows Path Variable, set to be
	equal to "python ".

	*	If changing this does not work, the python script can be launched manually like so:

	python <location of Mastermind.py> 100

	The argument 100 can be any integer and determines the number of simulations. Once the script 
	completes, press 'Refresh Data' in 'Mastermind_CPU.xlsx'.

