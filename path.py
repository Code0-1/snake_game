import sys


"""
This function should be temporary
/**
* in[0] : current (start)
* in[1] : neighbor (next node)
* return : value of the link between current and neighbor
*/
"""
def get_cost(current, neighbor):
    pass
    return 1


def reconstruct_path(cameFrom, current):
    total_path = {current}
    while current in cameFrom.Keys:
        current = cameFrom[current]
        total_path.prepend(current)
    return total_path

# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def A_Star(start, goal, grid): # h -> grid
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = {start}

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = sys.maxsize
    gScore[start] = 0

    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    fScore = sys.maxsize
    fScore[start] = grid(start)

    while (not openSet.empty()):
        # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        current = min(fScore) # the node in openSet having the lowest fScore[] value
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.Remove(current)
        for neighbor in current:
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + get_cost(current, neighbor)
            if tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + grid(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)

        # Open set is empty but goal was never reached
        return False
