# Pacman AI Project

## Introduction

This project is part of a CS AI course at [Your University], where I implemented various search algorithms for Pacman scenarios. The goal was to create a Pacman agent capable of finding paths through mazes efficiently and collecting food optimally.

## Project Overview

The project consists of several search algorithms implemented in Python, including Depth First Search (DFS), Breadth First Search (BFS), Uniform-Cost Search (UCS), and A* search. Additionally, the project involves solving more complex problems, such as finding paths that touch all four corners in a maze and optimizing the collection of Pacman food.

## Files

- **search.py**: Contains the implementation of search algorithms.
- **searchAgents.py**: Includes search-based agents, such as CornersProblem and FoodSearchProblem.
- **pacman.py**: The main file for running Pacman games.
- **util.py**: Provides useful data structures for implementing search algorithms.

## Running the Project

To run the project, navigate to the project directory and execute the following command:

```bash
python pacman.py -l [layout] -p [Agent] -a [options]
```

For example, to run the A* search algorithm with the Manhattan distance heuristic on the bigMaze layout, use the following command:

```bash
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## Project Structure

- **Q1-Q8**: These represent different stages of the project, each focusing on a specific aspect of search algorithms or problem-solving.

## Grading

Grading information for each question is provided in the project description. You can check your implementation against the autograder test cases using the following commands:

```bash
python autograder.py -q [question_number]
```

## How to Contribute

If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Feedback and suggestions are also welcome!

---
