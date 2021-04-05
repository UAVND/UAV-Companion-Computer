# Patrick Harkins 3/25/21
# A_star.py
# Simple A* pathfinding algorithm
#
# Translation of the psuedocode from the article below
# Based on the github of the python code from the article, it seems like his was broken so I built it from his psuedocode
# I haven't tested it at all so feel free to do that
# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

import math

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent # Node that before this node
        self.position = position # Location tuple (x,y) of this Nodes location

        self.G = 0 # Heuristic (estimated distance to destination)
        self.H = 0 # Distance between current and start
        self.F = 0 # Total cost of node

    def __eq__(self, other): # Overloaded == operator
        return self.position == other.position


# maze is 2D array of the map
    # 1 if there is an obstacle in that node, else 0
# start, end are tuples (x, y) of nodes in the graph
def a_star(maze, start, end):
    startNode = Node(None, start)
    endNode = Node(None, end)

    openList = [startNode]
    closedList = []

    while openList:
        currentNode = min_f(openList) # currentNode is the node in openList with the lowest F.  It is popped from the openList
        closedList.append(currentNode)

        if currentNode == endNode: # Found the destination
            return build_path(currentNode)

        for adjacentNode in get_adjacent(maze, currentNode):
            if adjacentNode in closedList:
                continue

            adjacentNode.G = currentNode.G + node_distance(currentNode, adjacentNode)
            adjacentNode.H = node_distance(adjacentNode, endNode)
            adjacentNode.F = adjacentNode.G + adjacentNode.H

            cont = False
            for node in openList:
                # made it compare the G values, initially had node.position in both comparisons
                if adjacentNode.position == node.position and adjacentNode.G > node.G:
                    cont = True # Continue the for loop on line 34
            if cont: continue

            openList.append(adjacentNode)


def min_f(openList): # returns the node in openList with lowest F and pops the node from the list
    fmin = min([node.F for node in openList])
    for i, node in enumerate(openList):
        if node.F == fmin:
            return openList.pop(i)

def build_path(currentNode):
    # I'm not sure long term if it makes sense but instead of appending node, I just appended the tuple positions
    # makes it easier to read and digest at the moment, but if ROS and the drone needs the full node then easy switch back
    path = [currentNode.position]
    while currentNode.parent:
        path.append(currentNode.parent.position)
        currentNode = currentNode.parent
    # need to reverse path
    resPath = []
    for pos in reversed(path):
        resPath.append(pos)
    return resPath

# added quick helper function to make sure the optimal path isn't cheating and going out of the competition boundaries
def in_maze(node, maze):
    if not 0 <= node.position[0] < len(maze):
        return False
    if not 0 <= node.position[1] < len(maze[node.position[0]]):
        return False
    return True

def get_adjacent(maze, currentNode): # Returns all the nodes we can travel to from currentNode
    x, y = currentNode.position
    neighbors = [ Node(currentNode, (x-1,y-1)), Node(currentNode, (x,y-1)), Node(currentNode, (x+1,y-1)),
                  Node(currentNode, (x-1,y))  ,                             Node(currentNode, (x+1,y)),
                  Node(currentNode, (x-1,y+1)), Node(currentNode, (x,y+1)), Node(currentNode, (x+1,y))]
    return [n for n in neighbors if (not maze[n.position[0]][n.position[1]] and in_maze(n, maze))] # return the neighbors that are not obstacles and within boundaries of the maze

def node_distance(node1, node2):
    return (node1.position[0] - node2.position[0])**2 + (node1.position[1] - node2.position[1])**2 # distance between node1 and node2
    # From testing, it seems like we do not need square root and it also significantly helps our time out
