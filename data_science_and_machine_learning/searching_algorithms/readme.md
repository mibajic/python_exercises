# Pac-Man  
The Pac-Man projects were developed for UC Berkeley's introductory artificial intelligence course. Detailed project overview from its developers can be found [here](http://ai.berkeley.edu/project_overview.html).

![image](https://user-images.githubusercontent.com/38294198/102825825-ded1ee00-43df-11eb-8200-03123ff7f1ff.png)

## Introduction 
Pac-Man is a game, where the main character Pac-Man is trying to navigate through an enclosed maze with the aim of eating all dots placed in the maze while avoiding four coloured ghosts. As a part of my semester work on the Artificial Intelligence 1 course, I've implemented the following navigation algorithms:
* Depth First Search Algorithm
* Breadth First Search Algorithm
* Unified Cost Search Algorithm
* A* Search Algorithm

## Setup
In order to run the code, please use the following commands.


Depth First Search:
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

Breadth First Search: 
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

Unified Cost Search:
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

A* Search:
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## Screenshots
![image](https://user-images.githubusercontent.com/38294198/103171000-f0d0e800-4848-11eb-93e4-9e208615a51b.png)
![Pac-Mac navigating through the maze in search of food](https://user-images.githubusercontent.com/38294198/102821744-e55c6780-43d7-11eb-8d3c-d7c8e6b30ac8.png)
![image](https://user-images.githubusercontent.com/38294198/103170956-a3547b00-4848-11eb-840c-d3eb9655da45.png)



