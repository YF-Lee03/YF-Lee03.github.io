---
author:
- Yifan Li
date: 2024-07-11
title: The subcubic outerplanar graph is $(1,1,2,2,2)$ -edge colorable
---

::: center
These is my personal proof to the conjecture that the subcubic
outerplanar graph is $(1,1,2,2,2)$ -edge colorable. They are only one of
the ways to look at the problems, and in particular, all errors are
almost surely mine.
:::

# Introduction

::: defi
**Definition 1**. A graph is **outerplanar** if it can be embedded in
the plane so that all vertices lie on the boundary of a single face.
:::

::: defi
**Definition 2**. A graph is **subcubic** if all vertices have degree at
most 3.
:::

::: defi
**Definition 3**. A graph is **$(1,1,2,2,2)$ -edge colorable** if its
edges can be colored with 5 colors such that each vertex is incident
with exactly one edge of each color. In addition, the edges with colors
being one of 3, 4, 5 could not seen by one edge.
:::

::: defi
**Definition 4**. A cut vertex is a vertex whose removal disconnects the
graph.
:::

::: defi
**Definition 5**. A graph is **2-connected** if it is connected and has
no cut vertex.
:::

::: defi
**Definition 6**. The face of a graph is a maximal connected subgraph
that is homeomorphic to an open disk. In addition, a 2-connected face is
a face that has no cut vertex.
:::

::: defi
**Definition 7**. The face graph of a graph is a graph whose vertices
are the faces of the graph and vertices are adjacent if they share an
edge. Note that in this paper we do not consider the outer face without
particular mention.
:::

::: conjecture
**Conjecture 1**. The subcubic outerplanar graph is $(1,1,2,2,2)$ -edge
colorable.
:::

# Proof

::: lemma
**Lemma 1**. The 2-connected subcubic outerplanar graph is $(1,1,2,2,2)$
-edge colorable.
:::

::: proof
*Proof.* Suppose not, there would be a counterexample. Let $G$ be a
counterexample with the smallest number of vertices. Since the graph is
outerplanar, the face graph is a tree. Consider the face $F_0$
corresponding to the leaf of the longest path of the face graph.
Removing $F_0$, the left graph is still outerplanar, denoted by $G'$. By
the minimality of $G$, $G'$ is $(1,1,2,2,2)$ -edge colorable. Now we
consider the situation of $F_0$. Since $F_0$ is a leaf, it would be as
the following: ◻
:::
