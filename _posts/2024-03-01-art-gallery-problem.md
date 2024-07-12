---
layout: post
title:  "Art Gallery Problem"
date:   2024-03-01 15:55:29 +0800
categories: Crumbs
---



Imagine you're in an art gallery filled with amazing artwork. The gallery is not shaped as a rectangle or square as usual, but its floor plan has a fancy shape with lots of corners and twists. The shape is made up of straight lines that meet in corners (in mathematics it is called a polygon). Your mission is to strategically place cameras at specific spots in the gallery to make sure that every spot in the gallery can be seen and is under surveillance. But here's the catch: you have to use as few cameras as possible. And these cameras can only be placed at the corners of the gallery.

Your task is to place the fewest number of security cameras possible so that every single spot in the gallery is under surveillance. This is known as the "Art Gallery Problem."

Solution 1. Quick observation: one may notice that for any convex polygon, only one cameras is enough (by the definition of convex polygon). Another thing you may notice is that any triangle is convex, but for polygon with more edges, it might not be convex. Then it is nature to ask the following question: is it always possible to triangularte a simple polygon?

For polygon with 3 edges, it is triangle already. For polygons with edges more than 3, we consider two non-adjacent vertices u and v. Add an edge uv. Then the polygon is separated into two polygons with less edges. By induction one may find that the simple polygons can be triangulated.

In fact, the vertices of the resulting triangulation graph is 3-colourable. Select two adjacent vertices and colour them with two distinct colour. Then colour vertices adjacent to these two vertices. Now two triangle have been coloured and what left is one or two triangulated polygons with less edges and two coloured adjacent vertices. Also by induction, one may find that the whole graph is 3-colourable.

![](https://cdn.mathpix.com/cropped/2024_07_12_bf513df47380905fff67g-1.jpg?height=629&width=575&top_left_y=1450&top_left_x=772)

Since the polygon is triangulated and 3-colourable. Thus each triangle has exactly three colours at its vertices. Place the cameras on one colour, every triangle is under surveillance. The smallest number of a colour is at most $\left\lfloor\frac{n}{3}\right\rfloor$.