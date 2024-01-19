
# Multi-Agent Pacman Project
## Introduction
Welcome to the second project of the CS383 Artificial Intelligence course at UMass Amherst. In this project, we extend our exploration into the field of multi-agent scenarios, focusing on enhancing the capabilities of the classic Pacman agent to navigate through mazes populated by ghosts. The key components include the implementation of minimax and expectimax search algorithms and the refinement of the evaluation function for Pacman.

## Project Overview
This project builds upon the foundations laid in the previous assignment, introducing new challenges associated with the presence of ghosts in the Pacman world. The primary objectives include designing agents that can make strategic decisions in the face of adversarial entities, demonstrating the ability to explore different search algorithms and improve the evaluation function to enhance Pacman's decision-making.

## Files
multiAgents.py: Contains the implementation of multi-agent search agents.
pacman.py: The main file for running Pacman games.
game.py: Logic for the functioning of the Pacman world.
util.py: Provides useful data structures for implementing search algorithms.

## Running the Project
To run the project, follow these steps:

Download the project files.

Open a terminal or command prompt and navigate to the project directory.

Execute the following command to run Pacman with specific settings:

```bash
python pacman.py -l [layout] -p [Agent] -a [options]
```
For example, to run the A* search algorithm with the Manhattan distance heuristic on the bigMaze layout:

bash
Copy code
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

## Project Structure
## Q1 (4 pts): Reflex Agent
Improve the ReflexAgent to play respectably. The provided reflex agent code gives examples of methods querying the GameState for information. A capable reflex agent should consider both food locations and ghost locations to perform well.

bash
Copy code
python pacman.py -p ReflexAgent -l testClassic
## Q2 (5 pts): Minimax
Implement an adversarial search agent in the MinimaxAgent class. Your minimax agent should work with any number of ghosts and expand the game tree to an arbitrary depth.

bash
Copy code
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
## Q3 (5 pts): Alpha-Beta Pruning
Create a new agent, AlphaBetaAgent, using alpha-beta pruning for more efficient exploration of the minimax tree.

bash
Copy code
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
## Q4 (5 pts): Expectimax
Implement the ExpectimaxAgent to model probabilistic behavior of agents who may make suboptimal choices.

bash
Copy code
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
## Q5 (6 pts): Evaluation Function
Write a better evaluation function for Pacman in the provided betterEvaluationFunction.

## How to Contribute
If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Feedback and suggestions are also welcome.

## Acknowledgment
The programming projects and autograders were developed at UC Berkeley for CS 188. We thank them for their permission to use it as a part of this course.
