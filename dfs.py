#!/usr/bin/env python

# Author: Delos Chang

# This python program solves the following CLRS algorithm problems:

# CLRS 22.3-10:
    # Modify the pseudocode for depth-first search so that it prints out every edge in the directed graph 
    # G, together with its type. Show what modifications, if any, you need to make if G is undirected.

# CLRS 22.4-2:
    # Give a linear-time algorithm that takes as input a directed acyclic graph G = (V,E)
    # and two vertices s and t, and returns the number of simple paths from s to t in G.


graph = {'S': ['G', 'T', 'B'],
             'B': ['T', 'H'],
             'G': ['F', 'T'],
             'T': [],
             'F': ['S'],
             'C': ['B', 'H', 'D'],
             'H': ['T'],
             'D': ['T']}

graph = {

             'P': ['O','S','Z'],
            'M': ['R', 'Q', 'T'],
             'N': ['Q', 'U', 'O'],
             'O': ['R', 'V', 'S'],
             'Q': ['T'],
             'R': ['U', 'Y'],
             'S': ['R'],
             'T': [],
             'U': ['T'],
             'V': ['X', 'W'],
             'X': [],
             'Z': [],
             'Y': ['V']}

color = {}
pi = {}

count = {} # container for CLRS 22.4-2

d = {}
f = {}
glob_time = 0 


edges = []

def DFSVisit(u):
    global glob_time
    color[u] = "gray"

    glob_time += 1
    d[u] = glob_time

    for v in graph[u]:
        print "Exploring vertices adjacent to " + str(v)

        # Discovery of vertex
        if color[v] == "white":
            pi[v] = u

            # Each time DFS discovers a new vertex, if it is T, set its count to 1. Otherwise, set it to 0.
            # If the vertex discovered is T, set it to "finished" and do not continue DFS from t
            if v == "V":
                count[v] = 1
                color[v] = "black"
            else:
                DFSVisit(v)

        # Each time u finishes with a vertex v, add the count to vertex u
        count[u] += count[v]

    color[u] = "black"


    glob_time += 1
    f[u] = glob_time


def DFS(graph):
    global glob_time
    for u in graph:
        color[u] = "white"
        pi[u] = "nil"
        count[u] = 0 ## 22.4-2 solution
    
    for u in graph:
        print "Starting DFS from " + str(u)
        if color[u] == "white":
            DFSVisit(u)


def create_edges(graph):
    for u in graph:
        for v in graph[u]:
            dict_m = {u:v}
            edges.append(dict_m)
    
    print edges

# Solution for 22.3-10
def print_edges(graph):
    for vert in edges:
        u = vert.keys()[0]
        v = vert.values()[0]

        if pi[v] == u:
            print "Tree Edge: (" + pi[v] + ", " + v + ")"
        else:
            # v is adj to u 
            # (u, v)
            if d[u] < d[v] and d[v] < f[v] and f[v] < f[u]:
                # v is a desc of u 
                print "Forward Edge: (" + u + ", " + v + ")"
            elif d[v] < d[u] and d[u] < f[u] and f[u] < f[v]:
                # u is a desc of v 
                print "Back Edge: (" + u + ", " + v + ")"
            else:
                print "Cross Edge: (" + u + ", " + v + ")"

# Solution for 22.4-2
# returns the count from s to t
def calc_count():
    print count['P']


DFS(graph2)
create_edges(graph2)
print "=========== Done ============"
#print_edges(graph)

print "=========== 22.4-2 ============"
calc_count()




