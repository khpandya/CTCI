import unittest
from collections import deque
# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R
def hasRouteBFS(graph, s, t):
    # write your code here
    if s==t:
        return True
    visited={}
    que=deque()
    que.append(s)
    while len(que)!=0:
        leftNode=que.popleft()
        if leftNode==t:
            return True
        for neighbor in graph[leftNode]:
            if neighbor not in visited:
                que.append(neighbor)
        visited[leftNode]=True
    return False

def hasRouteDFSrecursive(graph,s,t, visited=None):
    if s==t:
        return True
    if visited==None:
        visited={s:True}
    for node in graph[s]:
        if node not in visited:
            visited[node]=True
            if node==t:
                return True
            if hasRouteDFSrecursive(graph,node,t,visited):
                return True       
    return False

    

def is_route(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(graph, node, end, visited):
                return True
    return False


class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]
    print(tests)
    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = hasRouteDFSrecursive(self.graph, start, end)
            print([]==None)
            assert actual == expected



if __name__ == "__main__":
    # levelOrder(root)
    unittest.main()


