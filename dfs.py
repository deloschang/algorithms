#!/usr/bin/env python

# This python program solves the following problems:
# CLRS 22.3-10:
    # Modify the pseudocode for depth-first search so that it prints out every edge in the directed graph 
    # G, together with its type. Show what modifications, if any, you need to make if G is undirected.

# CLRS 22.4-2:
    # Give a linear-time algorithm that takes as input a directed acyclic graph G = (V,E)
    # and two vertices s and t, and returns the number of simple paths from s to t in G.


graph = {'A': ['G', 'E', 'B'],
             'B': ['E', 'H'],
             'G': ['F', 'E'],
             'E': [],
             'F': ['A'],
             'C': ['B', 'H', 'D'],
             'H': ['E'],
             'D': ['E']}

color = {}
pi = {}

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

        if color[v] == "white":
            pi[v] = u

            DFSVisit(v)

    color[u] = "black"

    glob_time += 1
    f[u] = glob_time


def DFS(graph):
    global glob_time
    for u in graph:
        color[u] = "white"
        pi[u] = "nil"
    
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

DFS(graph)
print "=========== Done ============"
create_edges(graph)
print_edges(graph)

print pi
print d


