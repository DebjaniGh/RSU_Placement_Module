# RSU_Placement_Module
This module utilizes Memetic Algorithm (AI) to optimally place Roadside Units in a given area map.

# Steps to run the module
1. First, install the SUMO application in your system. The steps to do so according to your system's OS are present 
in the official documentation here --> https://sumo.dlr.de/docs/Installing/index.html

2. Next, download the files from this repository. There are 4 python files in this repository. Their descriptions are as follows:
  a) "genetic_modular.py" contains the code for genetic algorithm (GA).
  b) "memetic_modular.py" contains the code for memetic algorithm (MFRD).
  c) "mem2.py" contains the code for GARHC algorithm.
  d) "graphs.py" helps generate different graphs for visualization purpose.

3. You need to have a software installed in your system to run python files.

4. Now, run graphs.py to obtain graphs pertaining to GA, MFRD, and GARHC algorithms. You can vary the number of RSUs and the initial population size by changing 
the values of the variables RSU_COUNT and POPULATION_SIZE at the very start of each of the 3 python files containing the algorithms.
