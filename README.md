# RSU_Placement_Module
This module utilizes Memetic Algorithm (AI) to optimally place Roadside Units in a given area map.

<img src="https://user-images.githubusercontent.com/13494311/184808759-f3e0db08-2ea3-44a2-8bc1-106a34f2fa44.png" width=45% height=45%>
<p align = "left">
Fig.1 - Framework of the Roadside Unit Placement Module
</p>

It was observed that an increase in the number of RSUs helps improve the fitness scores as is visible from the below graphs.
<img src="https://user-images.githubusercontent.com/13494311/184811823-e957f7ae-ec01-480b-861e-65f24f40a6a8.png" width=35% height=35%>
<p align = "left">
Fig.2 - Fitness scores vs. No. of RSUs in Area 1
</p>
<img src="https://user-images.githubusercontent.com/13494311/184811924-b696b9d9-9cd0-47e1-b548-b8993288c77f.png" width=35% height=35%>
<p align = "left">
Fig.3 - Fitness scores vs. No. of RSUs in Area 2
</p>

It was also observed that when compared to GA and GARHC algorithms (as explained in the above paper), MFRD performed the best w.r.t high fitness scores.
It was also observed that as the number of generations (iterations) are increased, fitness score also increases. Both these results can be inferred from the following graphs. 

<img src="https://user-images.githubusercontent.com/13494311/184901503-561f1502-7b2b-45af-93a1-b1bfc8008b99.png" width=50% height=50%>
<p align = "left">
Fig.4 - Comparison of Fitness scores of RSU placement algorithms for 9 RSUs in Area 1
</p>

<img src="https://user-images.githubusercontent.com/13494311/184901567-81f70f1e-61a7-412a-be8a-361f46b91ab7.png" width=50% height=50%>
<p align = "left">
Fig.5 - Comparison of Fitness scores of RSU placement algorithms for 9 RSUs in Area 1
</p>

<div class="row">
  <div class="column">
    <img src="https://user-images.githubusercontent.com/13494311/184903728-385c1a52-0e4b-4215-9c7c-97f4e92191f8.PNG" alt="gen0_12R_map2" style="width:100%">
  </div>
  <div class="column">
    <img src="https://user-images.githubusercontent.com/13494311/184904140-c7e9232d-0b43-4432-993a-803d4d21c8be.PNG" alt="gen0_12R_map2" style="width:100%">
  </div>
  <div class="column">
    <img src="https://user-images.githubusercontent.com/13494311/184904382-70478565-1e4d-4d65-b8cf-cb509ef87241.PNG" alt="gen30_12R_map2" style="width:100%">
  </div>
</div>

# Steps to run the module
1. First, install the SUMO application in your system. The steps to do so according to your system's OS are present 
in the official documentation here --> https://sumo.dlr.de/docs/Installing/index.html

2. Create a folder where you will keep all the files in this repository.

3. Next, download the files from this repository. There are 4 python files in this repository. Their descriptions are as follows:
  a) "genetic_modular.py" contains the code for genetic algorithm (GA).
  b) "memetic_modular.py" contains the code for memetic algorithm (MFRD).
  c) "mem2.py" contains the code for GARHC algorithm.
  d) "graphs.py" helps generate different graphs for visualization purpose.

4. You need to have a software installed in your system to run python files.

5. Create a folder "Map" inside the previous folder. Inside "Map", place the map.net.xml file. This file contains the area layout of Area 1 (Murlipura, Jaipur).

4. Now, run graphs.py to obtain graphs pertaining to GA, MFRD, and GARHC algorithms. You can vary the number of RSUs and the initial population size by changing 
the values of the variables RSU_COUNT and POPULATION_SIZE at the very start of each of the 3 python files containing the algorithms.
