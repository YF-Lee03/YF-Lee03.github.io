\maketitle1\begin{center}\begin{minipage}[c]{0.9\textwidth}\centering\footnotesize These is my personal proof to the conjecture that the subcubic outerplanar graph is $(1,1,2,2,2)$ -edge colorable. They are only one of the ways to look at the problems, and in particular, all errors are almost surely mine.\end{minipage}\end{center}1\tableofcontents1\section{Introduction}1\begin{defi} A graph is \textbf{outerplanar} if it can be embedded in the plane so that all vertices lie on the boundary of a single face. \end{defi}1\begin{defi} A graph is \textbf{subcubic} if all vertices have degree at most 3. \end{defi}1\begin{defi}
A graph is \textbf{$(1,1,2,2,2)$ -edge colorable} if its edges can be colored with 5 colors such that each vertex is incident with exactly one edge of each color. In addition, the edges with colors being one of 3, 4, 5 could not seen by one edge.
\end{defi}1\begin{defi}
    A cut vertex is a vertex whose removal disconnects the graph.
\end{defi}1\begin{defi}
A graph is \textbf{2-connected} if it is connected and has no cut vertex.
\end{defi}1\begin{defi}
    The face of a graph is a maximal connected subgraph that is homeomorphic to an open disk. In addition, a 2-connected face is a face that has no cut vertex.
\end{defi}1\begin{defi}
    The face graph of a graph is a graph whose vertices are the faces of the graph and vertices are adjacent if they share an edge. Note that in this paper we do not consider the outer face without particular mention.
\end{defi}1\begin{conjecture}
The subcubic outerplanar graph is $(1,1,2,2,2)$ -edge colorable.
\end{conjecture}1\section{Proof}1\begin{lemma}
    The 2-connected subcubic outerplanar graph is $(1,1,2,2,2)$ -edge colorable.
\end{lemma}1\begin{proof}
    Suppose not, there would be a counterexample. Let $G$ be a counterexample with the smallest number of vertices. Since the graph is outerplanar, the face graph is a tree. Consider the face $F_0$ corresponding to the leaf of the longest path of the face graph. Removing $F_0$, the left graph is still outerplanar, denoted by $G'$. By the minimality of $G$, $G'$ is $(1,1,2,2,2)$ -edge colorable. Now we consider the situation of $F_0$. Since $F_0$ is a leaf, it would be as the following:
    % \begin{figure}[H]
    %     \centering
    %     \includegraphics[width=0.5\textwidth]{fig1.png}
    %     \caption{The face $F_0$}
    % \end{figure}
\end{proof}