#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:35:24 2021

@author: kanikshasharma
"""


import random

def randomSolution(pdp):
    dlocation = list(range(len(pdp)))
    solution = []

    for i in range(len(pdp)):
        randomlocation = dlocation[random.randint(0, len(dlocation) - 1)]
        solution.append(randomlocation)
        dlocation.remove(randomlocation)

    return solution

def routeLength(pdp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += pdp[solution[i - 1]][solution[i]]
    return routeLength

def getNextnodes(solution):
    nextnodes = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            nextnode = solution.copy()
            nextnode[i] = solution[j]
            nextnode[j] = solution[i]
            nextnodes.append(nextnode)
    return nextnodes

def getBestNextnode(pdp,nextnodes):
    bestRouteLength = routeLength(pdp, nextnodes[0])
    bestNextnode = nextnodes[0]
    for nextnode in nextnodes:
        currentRouteLength = routeLength(pdp, nextnode)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNextnode = nextnode
    return bestNextnode, bestRouteLength

def hillClimbing(pdp):
    currentSolution = randomSolution(pdp)
    currentRouteLength = routeLength(pdp, currentSolution)
    nextnodes = getNextnodes(currentSolution)
    bestNextnode, bestNextnodeRouteLength = getBestNextnode(pdp, nextnodes)

    while bestNextnodeRouteLength < currentRouteLength:
        currentSolution = bestNextnode
        currentRouteLength = bestNextnodeRouteLength
        nextnodes = getNextnodes(currentSolution)
        bestNextnode, bestNextnodeRouteLength = getBestNextnode(pdp, nextnodes)

    return currentSolution, currentRouteLength

def main():
    pdp = [
        [0, 200, 300, 100],
        [200, 0, 100, 300],
        [300, 100, 0, 200],
        [100, 300, 200, 0]
    ]

    print(hillClimbing(pdp))

if __name__ == "__main__":
    main()