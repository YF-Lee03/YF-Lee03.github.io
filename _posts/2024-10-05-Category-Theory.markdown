---
layout: post
title:  "Category Theory"
date:   2024-07-12 15:55:29 +0800
categories: Category Theory
---



> 尝试提高一下可读性。参考书籍为Tom Leinster的*Basic Category Theory*，添加了一些个人想法。

## 1.1 Categories

在一切开始之前，我们首先要知道，category到底是什么。数学结构一般都可以通过“data”和“property”来定义，对于category而言，“data”是一些“**object**”（**对象**）以及他们之间的“**morphism**”（**态射**）。

### Def. 1  Category
A category $\mathcal{A}$ consists of:

- A class $\text{Ob}(\mathcal{A})$ of objects.

- For each pair of objects $A,B\in \text{Ob}(\mathcal{A})$, a set $\text{Hom}(A,B)$ of morphisms from $A$ to $B$.

- For each object $A\in \text{Ob}(\mathcal{A})$, a morphism $\text{id}_A\in \text{Hom}(A,A)$ called the identity morphism of $A$ satisfying the identity law:

$$
	f\circ \text{id}_A = f = \text{id}_B\circ f
$$

- For each triple of objects $A,B,C\in \text{Ob}(\mathcal{A})$, a composition function

$$
	\circ:\text{Hom}(B,C)\times \text{Hom}(A,B)\to \text{Hom}(A,C).
$$
satisfying the associativity law:

$$
	(f\circ g)\circ h = f\circ (g\circ h).
$$

#### Remark

以上对于范畴的定义，看似肯简单，实则非常抽象。出现了很多奇怪的概念：

- 我们称$\text{Ob}(\mathcal{A})$为“class”，而不是常见的“set”。因为有时我们讨论的对象过于庞大，如果用“set”，可能会产生一些悖论（比如the set of all set）。~~（当然，实际上我们并不太关心这一点）~~

- 我们给出了一个新的名词：“morphism”，注意虽然它们常常是一些Function，但它并不总是，因为有时候我们研究的并不是函数，任何满足composition law和associativity law的数学对象都能被称为态射。一般把它视为对象之间的箭头。

- 在范畴中，我们一般对对象内部的样子并不感兴趣。我们站在外面，关注对象之间的“关系”（箭头）。

- 于是，我们常常用diagram来表示范畴：对象是节点，态射是节点之间的箭头，单位态射是节点到其自身、没有什么“作用”的箭头，而态射的复合就是图表中的路径（path）。于是，你可能常常看见有人通过画diagram来证明定理（Ha, interesting, right?）

### 交换图
现在思考一个新的问题：怎么表示两个态射是相同的（比如说，$g\circ f=h$）？对于这个例子而言，我们有三个态射，画出来就是：

<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsMyxbMCwwLCJBIl0sWzEsMCwiQiJdLFsxLDEsIkMiXSxbMCwxLCJmIl0sWzEsMiwiZyJdLFswLDIsImgiLDJdXQ==&embed" width="304" height="304" style="border-radius: 8px; border: none;"></iframe>

如果我们要说$g\circ f=h$，也就是说从A通过两种路径（$h$和$g \circ f$）到达C没有区别，我们称这个图是**交换的**。于是，对于**交换**图而言，任意两条路径对应的态射的复合，得到的结果都是一样的。


> Do not be seduced by the lotus-eaters into infatuation with untethered abstraction.

### Eg. 3  一些范畴的例子

- $\textbf{Gp}$：群范畴，包含所有的群和它们之间的群同态。

- $\textbf{Ring}$：环范畴，包含所有的环和它们之间的环同态。

- $\textbf{Vect}_k$： 域$k$上的向量空间范畴，包含所有$k$上的向量空间以及它们之间的线性映射。

- $\textbf{Top}$：拓扑空间范畴，包含所有的拓扑空间和它们之间的连续映射。

#### Remark

虽然现在我们举的例子都是对象为集合、态射是映射的范畴，但实际上，它们不必如此。再次强调：只要满足了Def 1.1的数学结构，都可以被称为范畴。

### Defn. 2 Isomorphism （同构）
在上述例子中，我们都有“同构”的概念，但是它们的定义看到了对象内部，现在我们尝试从对象外面看~~（把它变得抽象）~~。

A map $f:A\to B$ in a category $\mathcal{A}$ is an isomorphism if there exists a map $g: B\to A$ in $\mathcal{A}$ such that $gf=1_A$ and $fg=1_B$.

用人话讲就是我们可以把这个态射复原成单位态射（从两个方向）


### Eg. 4  更多范畴的例子

以下这些图都是范畴（$\text{id}$并没有被画出来）

<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsMixbMCwwLCJcXGJ1bGxldCJdLFsxLDAsIlxcYnVsbGV0Il0sWzAsMSwiIiwwLHsib2Zmc2V0IjotMX1dLFswLDEsIiIsMix7Im9mZnNldCI6MX1dXQ==&embed" width="304" height="176" style="border-radius: 8px; border: none;"></iframe>

<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNSxbMSwwLCJcXGJ1bGxldCJdLFswLDEsIlxcYnVsbGV0Il0sWzEsMSwiXFxidWxsZXQiXSxbMiwwLCJcXGJ1bGxldCJdLFsyLDEsIlxcYnVsbGV0Il0sWzAsMSwia2oiLDJdLFswLDIsImoiLDJdLFsyLDEsImsiXSxbMCwzLCJmIl0sWzMsNCwiZyJdLFsyLDQsImgiLDJdLFswLDQsImhqPWdmIiwxXV0=&embed" width="432" height="304" style="border-radius: 8px; border: none;"></iframe>

#### Remark
有时候，我们并不会把态射的复合全部画在图里（那样太冗杂了！）。

### 从范畴的角度看群

从范畴来看，一个群就是只有一个对象的范畴，并且每个态射都是同构。而群的元素对应的是这个范畴中的态射，群运算是态射的复合。于是，一个群看起来像这样：

<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsMSxbMCwwLCJcXGJ1bGxldCJdLFswLDAsIiIsMCx7Im9mZnNldCI6MSwicmFkaXVzIjoxfV0sWzAsMCwiIiwwLHsib2Zmc2V0IjoxLCJyYWRpdXMiOjEsImFuZ2xlIjotOTB9XSxbMCwwLCIiLDAseyJvZmZzZXQiOjEsInJhZGl1cyI6MSwiYW5nbGUiOjkwfV0sWzAsMCwiIiwwLHsib2Zmc2V0IjoxLCJyYWRpdXMiOjEsImFuZ2xlIjoxODB9XV0=&embed" width="176" height="176" style="border-radius: 8px; border: none;"></iframe>

#### Remark
类似地，我们也可以用范畴来定义monoid（幺半群）、preorder（预序）等，这里就不一一展开了。

### Dual （对偶）

对于一个范畴$\mathcal{A}$，我们可以把它里面的态射“箭头”全部调转方向（reversing），这样我们可以得到一个新的范畴：**对偶范畴** $\mathcal{A}^{op}$。

