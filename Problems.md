# LeetCode Problems

## Sumário
1. [#881. Boats to Save People](#881-boats-to-save-people-) 

2. [#630. Course Schedule III](#630-course-schedule-iii-)

3. [#1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](#1489-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree-)

## #881. Boats to Save People 🔶


## Como resolvemos?
...

## #630. Course Schedule III 🔴



## Como resolvemos?
...

## #1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree 🔴

Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Exemple 1:

![ex1](img/ex1_1.png)

Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

![ex1](img/ex1_2.png)

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

Example 2:

![ex2](img/ex_2.png)

Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.


## Como resolvemos?

Nesse problema, vimos que era necessário apenas comparar os pesos das MSTs, e para cada aresta do grafo, ver se ela aumentava o peso da MST ou não, assim seria crítica, tendo que estar em todas as MSTs; se não, pseudo-crítica, normalmente quando empatava os pesos de duas arestas.

A ideia era bem simples, então apenas precisávamos de um algoritmo que "gerasse" uma MST, entre aspas porque estávamos interessados apenas nos pesos mesmo, e o Prim conseguiria fazer isso. Porém o tema do módulo era Greedy, e ficamos muito curiosos com a estrutura de dados Union-Find, então decidimos usar Kruskal.

Foi um desafio implementar essa estrutura, mas depois de ver uns vídeos na internet, entendemos como ela funcionava, e era relativamente simples. Depois de ter feito, bastou fazer umas modificações no algoritmo do Kruskal, para retornar apenas o peso da MST, e fazer uma forma de tirar uma aresta, sempre que fosse calcular esse peso.