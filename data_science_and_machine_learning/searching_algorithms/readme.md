# Pac-Man
> The Pac-Man projects were developed for UC Berkeley's introductory artificial intelligence course. Detailed project overview from its developers can be found [here](http://ai.berkeley.edu/project_overview.html).
 
Pac-Man is a game, where the main character Pac-Man is trying to navigate through an enclosed maze with the aim of eating all dots placed in the maze while avoiding four coloured ghosts. As a part of my semester work on the Artificial Intelligence I course, I've implemented the following navigation algorithms:
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
![Pac-Mac navigating through the maze in search of food](https://user-images.githubusercontent.com/38294198/102821744-e55c6780-43d7-11eb-8d3c-d7c8e6b30ac8.png)
