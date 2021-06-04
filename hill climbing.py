#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 13:46:25 2021

@author: kanikshasharma
"""
import random

def randomsolution(pdp):
    dlocation=list(range(len(pdp)))
    solution=[]
    
    for i in range(len(pdp)):
        randomlocation=dlocation[random.randint(0,len(dlocation)-1)]
        solution.append(randomlocation)
        dlocation.remove(randomlocation)
    return solution

def routelength(pdp,solution):
    routelength=0
    for i in range(len(solution)):
        routelength +=pdp[solution[i-1]][solution[i]]
    return routelength

def getnextnodes(solution):
    nextnodes = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            nextnode = solution.copy()
            nextnode[i] = solution[j]
            nextnode[j] = solution[i]
            nextnode.append(nextnode)
    return nextnodes

def getBestNextnode(pdp, nextnodes):
    bestRouteLength = routelength(pdp, nextnodes[0])
    bestNextnode = nextnodes[0]
    for nextnode in nextnodes:
        currentRouteLength = routelength(pdp, nextnode)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNextnode = nextnode
    return bestNextnode, bestRouteLength

    
    
def hillclimbing(pdp):
    currentsolution = randomsolution(pdp)
    

def main():
    pdp=[ [0,100,300,200],
          [100,0,200,300],
          [300,200,0,100],
          [200,300,100,0]]
    print(hillclimbing(pdp))
if __name__ == "__main__":
    main()

    

    
    