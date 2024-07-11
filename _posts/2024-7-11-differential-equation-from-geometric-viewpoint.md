\documentclass[a4paper]{article}

# Differential Equation from Geometric Viewpoint

%\input{header_YL.tex}\usepackage{graphicx}%Requiredforinsertingimages\usepackage{hyperref}\usepackage{amssymb}\usepackage{amsmath}\usepackage{amsthm}\usepackage{geometry}\usepackage{enumerate}undefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefinedundefined

Yifan Li
\date{\today}

\begin{document}
\maketitle

$$
\begin{minipage}[c]{0.9\textwidth}\centering\footnotesize These is my personal thought to methods of solving differential equations. It is only one of the ways to look at the methods, and in particular, all errors are almost surely mine.\end{minipage}
$$

Consider a differential equation

$$
\begin{equation}\label{eq1}
    P(x,\,y)\,dx+Q(x,\,y)\,dy=0,
\end{equation}
$$

there are several ways to solve the equation. Here we only discuss two of them: separation variables and using integrating factor.

Note that the solution of Eq [1](#eq1) is of the form

$$
\begin{equation*}
    y=f(x).
\end{equation*}
$$

One may regard it as a curve in $\mathbb{R}^2$, we know that there are two ways to represent a curve: by parametrilize $\vec{r}(t)=(x(t),\,y(t))$ and regard it as a level curve of a scalar function $\Phi(x,\,y)$.

For separation variables, one may write Eq [1](#eq1) as

$$
\begin{equation}\label{eq2}
    A(x)\,dx=B(y)\,dy.
\end{equation}
$$

Then you can integrate by both side. It would be confused because you may think what is $dx$, why we can apply integration now and why we can not integrate Eq [1](#eq1) directly. In fact, you can regard Eq [2](#eq2) as
$$
\begin{eqnarray}
    A(x)\frac{dx(t)}{dt}=B(x(t))\frac{dy(t)}{dt},
\end{eqnarray}
$$
and then we integrate each side with respect to $t$

$$
\begin{equation*}
    \int_{x(t_0)}^x A(\xi )d\xi=\int_{t_0}^t A(x(t))\frac{dx(t)}{dt}dt=\int_{t_0}^t B(x(t))\frac{dy(t)}{dt}+C=\int_{y(t_0)}^y B(\eta)d\eta+C,
\end{equation*}
$$

where $C$ is an arbitrary constant. In this case, you may feel more comfortable.<br>

For method using integrating factor, you need to multiply an integrating factor $\mu$ and would finally get a total derivative

$$
\begin{equation*}
    d(\Phi(x,\,y))=0,
\end{equation*}
$$

for some function $\Phi$. Since its total derivative is $0$, we know that $\Psi$ remains constant. Thus it is exactly a level curve $\Psi=C$ for constant $C$.
\end{document}

