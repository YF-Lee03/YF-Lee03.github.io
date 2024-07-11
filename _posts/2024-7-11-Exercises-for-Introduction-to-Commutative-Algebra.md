# Exercises for Introduction to Commutative Algebra 

Yifan Li

March 31, 2024


#### Abstract

These is my personal solution to the exercises from the book Introduction to Commutative Algebra by Atiyah and MacDonald. They are only one of the ways to look at the problems, and in particular, all errors are almost surely mine.


## 1 Chapter 1 Rings and Ideals

Exercise 1. Let $x$ be a nilpotent of a ring $A$. Show that $1+x$ is a unit of $A$. Dedecue that the sum of a nilpotent element and a unit is a unit.

Solution. Note that

$$
x \text { is a nilpotent } \Rightarrow \exists n \in \mathbb{N}\left(x^{n}=0\right)
$$

and thus

$$
(1+x)\left(1-x+x^{2}+\ldots+(-x)^{n-1}\right)=1+(-1)^{n} x^{n}=1
$$

Hence we know that $1+x$ is a unit.

In addition, for $a+x$ where $a$ is an arbitrary unit, it can be regarded as $a\left(1+a^{-1} x\right)$. Since $A$ commutes and $x$ is a nilpotent, we know that $a^{-1} x$ is also a nilpotent. Thus $1+a^{-1} x$ is unit, so does $a\left(1+a^{-1} x\right)=a+x$.

Definition (Primitive). $f \in A[x]$ is said to be primitive if $\left(a_{0}, a_{1}, \ldots, a_{n}\right)=(1)$ where $f=$ $a_{0}+a_{1} x+\ldots+a_{n} x^{n}$.

Exercise 2. Let $A$ be a ring and let $A[x]$ be the ring of polynomial in an indeterminate $x$, with coefficients in $A$. Let $f=a_{0}+a_{1} x+\ldots+a_{n} x^{n} \in A[x]$. Prove that
i) $f$ is unit in $A[x] \Leftrightarrow a_{0}$ is a unit in $A[x]$ and $a_{1}, a_{2}, \ldots, a_{n}$ are nilpotent.

ii) $f$ is nilpotent $\Leftrightarrow a_{0}, a_{1}, \ldots, a_{n}$ are nilpotent.

iii) $f$ is a zero-divisor $\Leftrightarrow$ there exists $a \neq 0$ in $A$ such that $a f=0$.

iv) $f g$ is primitive $\Leftrightarrow f$ and $g$ are primitives.

Solution. i) Suppose that $g=b_{0}+b_{1} x+\ldots+b_{m} x^{m}$ is the inverse of $f$, then we have

$$
\left(a_{0}+a_{1} x+\ldots+a_{n} x^{n}\right)\left(b_{0}+b_{1} x+\ldots+b_{m} x^{m}\right)=1
$$

and thus $a_{0} b_{0}=1$ and $a_{n} b_{m}=0$. Then we have proven that $a_{0}$ is unit. Now we try to prove $a_{i}$ is a nilpotent for $i \geq 0$. We start from the term of the largest order, $m+n$ (Since it has the simplest form). We have

$$
a_{n} b_{m}=0
$$

Also, for coefficient of $x^{m+n-1}$, we have

$$
a_{n} b_{m-1}+a_{n-1} b_{m}=0
$$

Here we try to use the previous conclusion, $a_{n} b_{m}=0$, so multiply by $a_{n}$ on both, we have

$$
a_{n}^{2} b_{m-1}+0=0
$$

In this case, we may guess that $a_{n}^{r+1} b_{m-r}=0$ (by induction). Suppose for $r \leq k$, we have the above assertion, then observe the coefficient of $x^{m+n-(k+1)}$, we have

$$
0=a_{n}^{k+1}\left(a_{n} b_{m-(k+1)}+a_{n-1} b_{m-k}+\ldots+a_{n-(k+1)} b_{m}\right)=a_{n}^{k+2} b_{m-(k+1)}
$$

By induction we know that $a_{n}^{r+1} b_{m-r}=0$ for all possible $r$, let $r=m$, we have

$$
a_{n}^{m+1} b_{0}=0
$$

Since $b_{0}$ is a unit, we know that $a_{n}^{m+1}=0$ and thus $a_{n}$ is a nilpotent. By Ex 11, we know that $\left(a_{0}+a_{1} x+\ldots+a_{n-1} x^{n-1}\right)=f-a_{n} x^{n}$ is still a unit. Then we may get $a_{n-1}$ is also a nilpotent. Using induction one may find that $a_{i}$ is nilpotent for any $0<i \leq n$.

ii) $\Rightarrow$ : Let $f=a_{0}+a_{1} x+a_{2} x^{2}+\ldots+a_{n} x^{n}$. Suppose that $f$ is a nilpotent, then there exists $m \in \mathbb{N}$ such that $f^{m}=0$. Then we have

$$
0=f^{n}=a_{0}^{m}+n a_{0}^{m-1} a_{1} x+\ldots+a_{n}^{m}
$$

and thus $a_{0}^{m}=0, a_{0}$ is a nilpotent. Suppose that $a_{i}$ is nilpotent for $i \leq k$. Then

$$
g:=f-\left(a_{0}+a_{1} x+\ldots+a_{k} x^{k}\right)
$$

is also a nilpotent. Then there exists $m^{\prime} \in \mathbb{N}$ such that $g^{m^{\prime}}=0$. Consider its coefficient of $x^{m^{\prime}(k+1)}$, we have $a_{k+1}^{m^{\prime}}=0$, which means that $a_{k+1}$ is also a nilpotent. By induction we know that $a_{i}$ is a nilpotent for $0 \leq i \leq n$.

$\Leftarrow$ : Suppose that $a_{0}, a_{1}, \ldots, a_{n}$ are nilpotent, then

$$
\exists m_{0}, m_{1}, \ldots, m_{n} \in \mathbb{N}\left(a_{0}^{m_{0}}=\ldots=a_{n}^{m_{n}}=0\right)
$$

Take

$$
M=\sum_{i=0}^{n} m_{i}
$$

by pigenhole principle, we know that for any term of $f^{n}$, there must be at least one of $a_{0}^{m_{0}}, \ldots, a_{n}^{m_{n}}$ and thus $f^{n}=0$.

iii) $\Rightarrow$ : Since $f$ is a zero-divisor, there exists $g=b_{0}+b_{1} x+\ldots+b_{n} x^{n} \neq 0$ with smallest degree such that $f g=0$. Consider its term of highest order, we have $a_{n} b_{m}=0$. However, note that

$$
0=a_{n}(f g)=f\left(a_{n} g\right)
$$

Here $a_{n} g$ has less degree than $g$ since $a_{n} b_{m}=0$. In this case the only possible case for $a_{n} g$ is 0 . Then consider the polynomial $f$ removed the term of highest order, we have

$$
0=f g=g\left(f-a_{n} x^{n}\right)+a_{n} g x^{n}=g\left(f-a_{n} x^{n}\right)
$$

Then we use the same procedure for $f-a_{n} x^{n}$ and $g$ to show that $a_{n-1} b_{m}=0$. By induction we know that $a_{i} b_{m}=0$ for all $i \leq n$. Then we know that $b_{m} f=0$.

$\Leftarrow$ : It is obvious since $a \in A \subseteq A[x]$
iv) $\Rightarrow$ : One may regard the coefficients of $f g$ as linear combinations of coefficients of $f$ or $g$.

$\Leftarrow$ : Suppose $f$ and $g$ are primitive but $f g$ does not. Then

$$
\mathfrak{c}:=\left(c_{0}, c_{1}, \ldots, c_{n}\right) \neq(1)
$$

where $f g=c_{0}+c_{1} x+\ldots+c_{m+n} x^{m+n}$. Then there is a maximal idael $\mathfrak{m}$ containing $\mathfrak{c}$, and thus

$$
f g \equiv 0(\bmod \mathfrak{m})
$$

In the field $A / \mathfrak{m}$, there is no zero divisor, and thus $f \equiv 0(\bmod \mathfrak{m})$ or $g \equiv 0(\bmod \mathfrak{m})$. Then we know that $f$ or $g$ is not primitive (their coefficients are all in $\mathfrak{m} \subsetneq A$ ), which is a contradiction.

Exercise 3. Generalize the result of $\operatorname{Ex} 2$ to $A\left[x_{1}, x_{2}, \ldots, x_{r}\right]$.

Exercise 4. In the ring $A[x]$, the Jacobson radical $\mathfrak{R}$ is equal to the nilradical $\mathfrak{N}$.

Solution. $\mathfrak{R} \subseteq \mathfrak{N}$ : For any element $f=a_{0}+a_{1} x+\ldots+a_{n} x^{n} \in \mathfrak{R}$, we know that $1-f g$ is a unit for any $g \in A[x]$. Now we just simply take $g=1$, then $1-f$ is a unit. By Ex $\sqrt{2\rangle}$, we know that $a_{k}$ is a nilpotent for $\forall 0<k \leq n$.

Then we need to show $a_{0}$ is also a nilpotent. Consider the coefficient of $x$ for $1-f g$, we have

$$
a_{0} b_{1}+a_{1} b_{0}=0
$$

Since $a_{1}$ is a nilpotent, then $a_{0} b_{1}=-a_{1} b_{0}$ is also a nilpotent. Since $b_{1}$ is arbitrary, we may simply take $b_{1}=1$. Thus $a_{0}$ is a nilpotent. Thus by Ex 2 , $f$ is nilpotent, i.e. $f \in \mathfrak{N}$.

$\mathfrak{N} \subseteq \mathfrak{R}$ : Note that $f \in \mathfrak{N}$ means that $f$ is a nilpotent, then by Ex $\sqrt{2}$, we have

$$
(f \in \mathfrak{N}) \Rightarrow \forall g \in A[x](f g \in \mathfrak{N}) \Rightarrow(1-f g \text { is a unit }) \Rightarrow(1-f g \in \mathfrak{R})
$$

To sum up, we have $\mathfrak{R}=\mathfrak{N}$.

Remark. There is a quicker way to see that the nilradical is contained in the Jacobson radical. Note that the nilradical is the intersection of all prime ideals and the Jacobson radical is the intersection of all maximal ideals. Since every maximal ideal is prime, the intersection of all maximal ideals contains the intersection of all prime ideals. Thus we know that the nilradical is contained in the Jacobson radical.

Exercise 5. Let $A$ be a ring and let $A[[x]]$ be the ring of formal power series $f=\sum_{n=0}^{\infty} a_{n} x^{n}$ with coefficients in $A$. Show that
i) $f$ is a unit in $A[[x]] \Leftrightarrow a_{0}$ is a unit in $A$.

ii) If $f$ is nilpotent, then $a_{n}$ is nilpotent for all $n \geq 0$.

iii) $f$ belongs to the Jacobson readical of $A[[x]] \Leftrightarrow a_{0}$ belongs to the Jacobson radical of $A$.

iv) The contraction of a maximal ideal $\mathfrak{m}$ of $A[[x]]$ is a maximal Ideal of $A$, and $\mathfrak{m}$ is generated by $\mathfrak{m}^{c}$ and $x$.

v) Every prime ideal of $A$ is the contraction of a prime ideal of $A[[x]]$.

Solution. i) $\Rightarrow$ : $f$ is a unit $\Rightarrow \exists g=\sum_{n=0}^{\infty} b_{n} x^{n}(f g=1)$. Then we may find that $a_{0} b_{0}=1$ and thus $a_{0}$ is a unit.

$\Leftarrow$ : Since $a_{0}$ is a unit, let $b_{0}=a_{0}^{-1}$. Note that

$$
f g=a_{0} b_{0}+\left(a_{1} b_{0}+a_{0} b_{1}\right) x+\ldots+\left(\sum_{i+j=k} a_{i} b_{j}\right) x^{k}+\ldots
$$

Take $b_{1}=-a_{1} b_{0} a_{0}^{-1}$, we can ensure that the coefficient of $x$ in $f g$ is zero. Suppose that $b_{0}, b_{1}, \ldots, b_{k}$ have been taken for some $k \in \mathbb{N}$ such that the first $k$ nonconstant terms of $f g$ are all zero, then the coefficient of the $k+1$-th term is

$$
a_{0} b_{k+1}+\ldots+a_{k+1} b_{0}
$$

where $b_{n+1}$ is the only unknown and $a_{0}$ is a unit. Take

$$
b_{k+1}=-a_{0}^{-1}\left(a_{1} b_{k}+\ldots+a_{k+1} b_{0}\right)
$$

In this case, the coefficient of $x^{k+1}$ becomes 0 . By induction, we could find $g$ such that $f g=1$.

ii) Let $f=a_{0}+a_{1} x+\ldots+a_{n} x^{n}+\ldots$, then $f$ being a nilpotent implies that $f^{m}=0$ for some $m \in \mathbb{N}$. Consider the constant term, we have $a_{0}^{m}=0$, which implies that $a_{0}$ is a nilpotent. Suppose that $a_{i}$ is nilpotent for any $i \leq k$, then $g:=f-\left(a_{0}+a_{1} x+\ldots+a_{k} x^{k}\right)$ is also a nilpotent. Note that

$$
g^{m^{\prime}}=a_{k+1}^{m^{\prime}} x^{m^{\prime}(k+1)}+\ldots
$$

Thus one may deduce that $a_{k+1}$ is also a nilpotent. By induction, we know that $a_{n}$ is nilpotent for all $n \geq 0$.

Remark: There is another viewpoint: you can $\bmod f$ by $\mathfrak{N}$ and use the similar procedure as above.

iii) $\Rightarrow$ : Suppose $f$ belongs to the Jacobson radical of $A[[x]]$, then $1-f g$ is a unit for any $g \in A[[x]]$. By Ex 5/i), we know that $1-a_{0} b_{0}$ is a unit and $b_{0}$ is arbitrary since $g$ is arbitrary. Then we may find that $a_{0}$ is in the Jacobson radical of $A$.

$\Leftarrow$ : Suppose that $a_{0}$ is in the Jacobson radical of $A$, then $1-a_{0} b_{0}$ is a unit. By Ex $5 \sqrt{\mathrm{i}}$, we know that $1-f g$ is a unit. Thus $f$ belongs to the Jacobson radical of $A[[x]]$.

iv) Let $\mathfrak{m}$ be a maximal ideal of $A[[x]]$, then $A[[x]] / \mathfrak{m}$ is a field. Now we want to show that $A / \mathfrak{m}$ is a field. Note that in $A[[x]], 1+x h$ is a unit for any $h$ since the constant term of $1+x h$ is 1 , which is a unit. Thus $x \in \mathfrak{R}$ which means that $x$ is in any maximal ideal of $A[[x]]$. Hence $x \in \mathfrak{m}$. For any $f \in A[[x]]$, we know that

$$
f \equiv b(\bmod \mathfrak{m})
$$

for some $b \in A$. Let $\bar{a}=\bar{b}^{-1}$. Since $x \in \mathfrak{m}$, we may find a representative $a \in A$ for $\bar{a}$. Then we have

$$
a f \equiv 1(\bmod \mathfrak{m})
$$

In this case, we have

$$
a f=1+g
$$

for some $g \in \mathfrak{m}$. Consider the constant term, we know that

$$
a a_{0}-1=g-\left(a f-a a_{0}\right)=g-a a_{1} x-a a_{2} x^{2}-\ldots \in \mathfrak{m}
$$

and thus $a_{0} a \equiv 1(\bmod \mathfrak{m})$. Since $a, a_{0} \in A$, they also belongs to $\mathfrak{m}^{c}$. Then we know that $a_{0}$ is a unit in $A / \mathfrak{m}^{c}$. Note that $f$ is arbitrarily chosen, thus $a_{0}$ is an arbitrary element in A. Hence $A / \mathfrak{m}$ is a field.

Now we try to show $\mathfrak{m}$ is generated by $\mathfrak{m}^{c}$ and $(x)$. Consider $\mathfrak{m} \backslash(x)$, we know that $\forall \bar{f} \in$ $\mathfrak{m} \backslash(x)$, we have $\bar{f}=a_{0}+(x)$ for some $a_{0} \in A$. Then we have $a_{0} \in \operatorname{id}_{A}^{-1}(\mathfrak{m})=\mathfrak{m}^{c}$. Thus $\mathfrak{m}$ is generated by $\mathfrak{m}^{c}$ and $(x)$.

Remark. Note that in $A[[x]]$, the degree is infinity and the coefficients of $f$ is not "bounded". Thus there is no restriction on the largest degree term (no such term).

Exercise 6. A ring $A$ is such that every ideal not contained in the nilradical contains a non-zero idempotent (i.e. an element $e$ such that $e^{2}=e \neq 0$ ). Prove that the nilradical and Jacobson radical of $A$ are equal.

Proof. $\mathfrak{N} \subseteq \mathfrak{R}$ is trivial (we have proved it in Ex 4) that $\mathfrak{N} \subseteq \mathfrak{R}$ always holds).

Suppose that $a \in \mathfrak{R} \backslash \mathfrak{N}$, then $(a) \nsubseteq \mathfrak{N}$. Then there exists $e=a x \in(a)$ for some $x \in A$ such that $e^{2}=e \neq 0$. Then $(1-e) e=0$. We know that $1-e=1-a x$ is a zero divisor, i.e. $1-a x$ is not unit. Thus $a \notin \mathfrak{R}$, which means that there is no such $a \in \mathfrak{R} \backslash \mathfrak{N}$ and thus $\mathfrak{R} \subseteq \mathfrak{N}$.

Thus $\mathfrak{R}=\mathfrak{N}$.

Exercise 7. Let $A$ be a ring in which every element $x$ satisties $x^{n}=x$ for some $n>1$ (depending on $x$ ). Show that every prime ideal in $A$ is maximal.

Proof. Let $\mathfrak{p}$ be a prime ideal of $A$. To show that it is maximal, we need to show that $A / \mathfrak{p}$ is a field. Let $x \in A \backslash \mathfrak{p}$, then $x^{n}=x$. Consider $\bar{x}=x+\mathfrak{p}$ and $\bar{x}^{n}=x^{n}+\mathfrak{p}$. Then we have

$$
\begin{aligned}
\bar{x}^{n}-\bar{x} & =0 \\
0=\left(x^{n}+\mathfrak{p}\right)-(x+\mathfrak{p}) & =(x+\mathfrak{p})\left(\left(x^{n-1}+\mathfrak{p}\right)-(1+\mathfrak{p})\right)
\end{aligned}
$$

Since $\mathfrak{p}$ is prime, we know that $A / \mathfrak{p}$ is an integral domain. Note that $x \notin \mathfrak{p} \Rightarrow x+\mathfrak{p} \neq 0$. Thus the only possibility is $x^{n-1} \equiv 1(\bmod \mathfrak{p})$. In this case,

$$
1=\bar{x}^{n-1}=\bar{x} \bar{x}^{n-2}
$$

Thus the inverse of $\bar{x}$ exists: $\bar{x}^{-1}=\bar{x}^{n-2}$, i.e. $A / \mathfrak{p}$ is a field. Thus $\mathfrak{p}$ is maximal.

Exercise 8. The set of prime ideals of $A$ has minimal elements with respect to inclusion.

Proof. Define an order: $\mathfrak{p} \leq \mathfrak{q} \Leftrightarrow \mathfrak{p} \subseteq \mathfrak{q}$. Then the minimal element with respect to inclusion is the minimal element with respect to this order. Then we try to use Zorn's lemma.

Let $\mathfrak{p}_{\alpha}$ be a chain of prime ideals. Then $\mathfrak{p}=\bigcup_{\alpha} \mathfrak{p}_{\alpha}$ is an ideal. Suppose that $a b \in \mathfrak{p}$, then $a \in \mathfrak{p}_{\alpha} \wedge b \in \mathfrak{p}_{\alpha}$ for all $\alpha$. Suppose $a \notin \mathfrak{p}$, then $a \notin \mathfrak{p}_{\beta}$ for some $\beta$. For $\alpha>\beta, b \in \mathfrak{p}_{\alpha}$ since $\mathfrak{p}_{\alpha} \subseteq \mathfrak{p}_{\beta}$ and $a \notin \mathfrak{p}_{\beta}$. For $\alpha \leq \beta, b \in \mathfrak{p}_{\beta} \subseteq \mathfrak{p}_{\alpha}$. Thus $b \in \mathfrak{p}$, i.e. $\mathfrak{p}$ is prime. Thus $\mathfrak{p}$ is an upper bound of the chain. By Zorn's lemma, we know that there exists a maximal element in the set of prime ideals of $A$.

Exercise 9. Let $\mathfrak{a} \neq(1)$ be an ideal in a ring $A$. Show that $\mathfrak{a}=r(\mathfrak{a})$ if and only if $\mathfrak{a}$ is an intersection of prime ideals.

Proof. $\Rightarrow$ : Suppose that $\mathfrak{a}=r(\mathfrak{a})$. Note that the radical of $\mathfrak{a}$ is the intersection of all prime ideals containing $\mathfrak{a}$. Thus $\mathfrak{a}$ is an intersection of prime ideals.

$\Leftarrow$ : Suppose that $\mathfrak{a}$ is an intersection of prime ideals. Then it is prime. Then $r(\mathfrak{a})=\mathfrak{a}$. (Note that the radical of a prime ideal is itself since the radical is the intersection of all prime ideals containing it.)

Exercise 10. Let $A$ be a ring and $\mathfrak{N}$ its nilradical. Show that the following are equivalent:
i) $A$ has exactly one prime ideal.

ii) Every element of $A$ is either a unit or nilpotent.

iii) $A / \mathfrak{N}$ is a field.

Proof. i) $\Rightarrow$ ii): Note that $\mathfrak{N}$ is the intersection of all prime ideals. If $A$ has exactly one prime ideal, then it is $\mathfrak{N}$. Then $A / \mathfrak{N}$ is a integral domain. Then every element of $A / \mathfrak{N}$ is either a unit or zero. Note that a unit plus a nilpotent is a unit, then every element of $A$ is either a unit or nilpotent.

ii) $\Rightarrow$ iii): It is easy to show that $\mathfrak{N}$ is a maximal ideal if elements in $A$ are either units or nilpotents. Then $A / \mathfrak{N}$ is a field.

iii) $\Rightarrow \mathrm{i})$ : Suppose that $A / \mathfrak{N}$ is a field, then $\mathfrak{N}$ is maximal. Note that $\mathfrak{N}$ is the intersection of all prime ideals, thus for any prime ideal $\mathfrak{p}$, we have $\mathfrak{N} \subseteq \mathfrak{p}$. Then $\mathfrak{N}$ maximal implies that $\mathfrak{p}=\mathfrak{N}$. Thus $A$ has exactly one prime ideal.

Exercise 11. A ring $A$ is Boolean if $x^{2}=x$ for all $x \in A$. In a Boolean ring $A$, show that
i) $2 x=0$ for all $x \in A$.

ii) Every prime ideal $\mathfrak{p}$ is maximal and $A / \mathfrak{p}$ is a field with two elements.

iii) Every finitely generated ideal is principal.

Proof. i): Note that

$$
x+1=(x+1)^{2}=x^{2}+2 x+1=x+2 x+1
$$

Then $2 x=0$.

ii): Suppose that $\mathfrak{p}$ is a prime ideal, then consider $x \in A \backslash \mathfrak{p}$. Let $\bar{x}=x+\mathfrak{p}$, then $\bar{x}^{2}=\bar{x}$. Then

$$
\bar{x}(\bar{x}-1)=0 \in \mathfrak{p}
$$

Since $x \notin \mathfrak{p}$, then $x-1 \in \mathfrak{p}$ since $\mathfrak{p}$ is prime. Thus

$$
x \equiv 1(\bmod \mathfrak{p})
$$

Then $\bar{x}$ is a unit in $A / \mathfrak{p}$. Then $A / \mathfrak{p}$ is a field. Note that for any $x \in A \backslash \mathfrak{p}$, we have $x \equiv 1(\bmod \mathfrak{p})$. Hence we know that $\bar{x}=1$. Then $A / \mathfrak{p}$ is a field with two elements.

iii): To show that every finitely generated ideal is principal, we only need to show that that every ideal generated by two elements is principal. By induction, we may show that every ideal generated by $n$ elements is principal. Suppose that

$$
\mathfrak{a}=\left(x_{1}, x_{2}\right)=\left(x_{1}\right)+\left(x_{2}\right)
$$

Then we may find that $\mathfrak{a}=\left(x_{1}\right)+\left(x_{2}-x_{1}\right)$. Since

$$
2\left(x_{2}-x_{1}\right)=\left(\left(x_{2}-x_{1}\right)+\left(x_{2}-x_{1}\right)\right)^{2}=4\left(x_{2}-x_{1}\right)
$$

we know that $2\left(x_{2}-x_{1}\right)=0$. Then

$$
\mathfrak{a}=\left(x_{1}\right)+\left(x_{2}-x_{1}\right)=\left(x_{1}\right)
$$

Thus by induction, every finitely generated ideal is principal.

## Exercise 12.

## Exercise 13.

## Exercise 14.

## The prime spectrum of a ring

Exercise 15. Let $A$ be a ring, $X$ the set of all prime ideals of $A$. Let $V(E)$ denote the set of all prime ideals of $A$ which contain $E$. Prove that

i) If $\mathfrak{a}$ is an ideal generated by $E$, then $V(E)=V(\mathfrak{a})=V(r(\mathfrak{a}))$.

ii) $V(0)=X, V(1)=\varnothing$.

iii) If $\left(E_{i}\right)_{i \in I}$ is a family of subsets of $A$, then $V\left(\bigcup_{i \in I} E_{i}\right)=\bigcap_{i \in I} V\left(E_{i}\right)$.

iv) If $\mathfrak{a}, \mathfrak{b}$ are ideals of $A$, then $V(\mathfrak{a} \cap \mathfrak{b})=V(\mathfrak{a} \mathfrak{b})=V(\mathfrak{a}) \cup V(\mathfrak{b})$.

Proof. i): $V(E) \supseteq V(\mathfrak{a}) \supseteq V(r(\mathfrak{a}))$ is obvious since $E \subseteq \mathfrak{a} \subseteq r(\mathfrak{a})$. Since $E$ generates $\mathfrak{a}, \mathfrak{a}$ is the smallest ideal containing $\mathfrak{a}$, i.e. for $\forall \mathfrak{p} \in V(E)$, we have $\mathfrak{a} \subseteq \mathfrak{p}$. Then $\mathfrak{p} \in V(\mathfrak{a})$. Then $V(E) \subseteq V(\mathfrak{a})$. Then we have $V(E)=V(\mathfrak{a})$.

For $\forall \mathfrak{p} \in V(\mathfrak{a})$, we have $\mathfrak{a} \subseteq \mathfrak{p}$. Then $r(\mathfrak{a}) \subseteq \mathfrak{p}$ since $r(\mathfrak{a})$ is the intersection of all prime ideals containing $\mathfrak{a}$. Then $\mathfrak{p} \in V(r(\mathfrak{a}))$. Then $V(\mathfrak{a}) \subseteq V(r(\mathfrak{a}))$, and thus we have $V(\mathfrak{a})=V(r(\mathfrak{a}))$.

Remark: The main idea is that one ideal is the smallest (prime) ideal containing another ideal. Thus the prime ideal containing one must contain the other.

ii): $V(0)=X$ is obvious since every prime ideal contains $0 . V(1)=\varnothing$ is obvious since no prime ideal contains 1 by definition.

iii): The left-hand side of the equation is the collection of all prime ideals containing $\bigcup_{i \in I} E_{i}$, and the right-hand side is the intersection of collection of all prime ideals containing $E_{i}$ for all $i \in I$, which means the collection of prime ideals containing all of the $E_{i}$. Then the two sides are equal.

iv): $\mathfrak{a} \cap \mathfrak{b} \supseteq \mathfrak{a} \mathfrak{b} \Rightarrow V(\mathfrak{a} \cap \mathfrak{b}) \subseteq V(\mathfrak{a} \mathfrak{b})$. For $\forall \mathfrak{p} \in V(\mathfrak{a} \mathfrak{b})$, we have $\mathfrak{a b} \subseteq \mathfrak{p}$. Suppose $\mathfrak{b} \nsubseteq \mathfrak{p}$, then $\exists b \in \mathfrak{b} \backslash \mathfrak{p}$. Note that $a b \in \mathfrak{a} \mathfrak{b} \subseteq \mathfrak{p}$ for $\forall a \in \mathfrak{a}$. Then $\mathfrak{a} \subseteq \mathfrak{p}$. Then $\mathfrak{p} \in V(\mathfrak{a}) \subseteq V(\mathfrak{a} \cap \mathfrak{b})$ since $\mathfrak{a} \cap \mathfrak{b} \subseteq \mathfrak{a}$. If $\mathfrak{b} \subseteq \mathfrak{p}$, we may know that $\mathfrak{p} \in V(\mathfrak{b}) \subseteq V(\mathfrak{a} \cap \mathfrak{b})$. Then we have $V(\mathfrak{a} \cap \mathfrak{b})=V(\mathfrak{a}) \cup V(\mathfrak{b})$.

In addition, $(\mathfrak{a} \supseteq \mathfrak{a b}) \wedge(\mathfrak{b} \supseteq \mathfrak{a b}) \Rightarrow(V(\mathfrak{a}) \subseteq V(\mathfrak{a} \mathfrak{b})) \wedge(V(\mathfrak{b}) \subseteq V(\mathfrak{a} \mathfrak{b}))$. Then we have $V(\mathfrak{a}) \cup$ $V(\mathfrak{b}) \subseteq V(\mathfrak{a} \mathfrak{b})$. Then we consider the other direction, $\forall \mathfrak{p} \in V(\mathfrak{a} \mathfrak{b})(\mathfrak{a} \subseteq \mathfrak{p} \vee \mathfrak{b} \subseteq \mathfrak{p}$ ) (we have proven it before). In this case, $\mathfrak{p} \in V(\mathfrak{a}) \cup V(\mathfrak{b})$. Then we have $V(\mathfrak{a} \mathfrak{b}) \subseteq V(\mathfrak{a}) \cup V(\mathfrak{b})$. Then we have $V(\mathfrak{a} \mathfrak{b})=V(\mathfrak{a}) \cup V(\mathfrak{b})$.

Exercise 16. Draw pictures of the prime spectrum of $\mathbb{Z}, \mathbb{R}, \mathbb{C}[x], \mathbb{R}[x]$ and $\mathbb{Z}[x]$.

## Solution.

Exercise 17. For each $f \in A$, let $X_{f}$ denote the complement of $V(f)$ in $X=\operatorname{Spec}(A)$. The sets $X_{f}$ are open in the Zariski topology. Show that they form a basis of open sets, and that
i) $X_{f} \cap X_{g}=X_{f g}$,
ii) $X_{f}=\varnothing \Leftrightarrow f$ is nilpotent,

iii) $X_{f}=X \Leftrightarrow f$ is a unit,

iv) $X_{f}=X_{g} \Leftrightarrow r((f))=r((g))$,
v) $X_{f}$ is quasi-compact (i.e. every open cover has a finite subcover),

vi) More generally, each $X_{f_{i}}$ is quasi-compact,

vii) An open subset of $X$ is quasi-compact if and only if it is a finite union of sets $X_{f_{i}}$.

The sets $X_{f}$ are called basic open sets of $X=\operatorname{Spec}(A)$.

Proof. i): $X_{f} \cap X_{g}$ is the set of all prime ideals not containing $f$ and $g$, which is the set of all prime ideals not containing $f g$, i.e. $X_{f g}$. (Note that $V(f) \cup V(g)=V(f g)$.)

ii): $X_{f}=\varnothing$ means that $V(f)=X$, then $f$ should be in every prime ideal, i.e. $f$ is nilpotent.

iii): $X_{f}=X$ means that $V(f)=\varnothing$, then $f$ is not contained in any prime ideal. Since for every non-unit element, it must lies in a maximal ideal, which is also a prime ideal, we know that $f$ is a unit.

iv): $X_{f}=X_{g} \Leftrightarrow r(f)=r(g)$ : We know that $(f)$ is the smallest ideal containing $f$, then

$$
\forall \mathfrak{p} \in V(f) \quad(\mathfrak{p} \supseteq(f))
$$

Thus $V(f)=V((f))$. Since $r((f))$ is the intersection of all prime ideals containing $(f)$, every prime ideal containing $(f)$ must contains $r((f))$, and vise verse. Then we have $V(f)=V(r((f)))$. In this case,

$$
\begin{gathered}
X_{f}=X_{g} \Leftrightarrow V(f)=V(g) \Leftrightarrow V(r(f))=V(r(g)) \\
r(f) \in V(r(g)) \Leftrightarrow r(f) \supseteq r(g) \\
r(g) \in V(r(f)) \Leftrightarrow r(g) \supseteq r(f)
\end{gathered}
$$

Thus $X_{f}=X_{g} \Leftrightarrow r(f)=r(g)$.

v):

vi):

vii):

Exercise 18. For psychological reasons it is sometimes convenient to denote a prime ideal of $A$ by a letter such as $x$ or $y$ when thinking of it as a point of $X=\operatorname{Spec}(A)$. When thinking of $x$ as a prime ideal of $A$, we denote it by $\mathfrak{p}_{x}$ (logically, of course, it is the same thing). Show that

i) The set $\{x\}$ is closed in $X$ if and only if $\mathfrak{p}_{x}$ is maximal;

ii) $\overline{\{x\}}=V\left(\mathfrak{p}_{x}\right)$;

iii) $y \in \overline{\{x\}} \Leftrightarrow \mathfrak{p}_{x} \subseteq \mathfrak{p}_{y}$;

iv) $X$ is a $T_{0}$-space (i.e. for every pair of distinct points, there is a neighborhood of one which does not contain the other).

Proof. i): $\Rightarrow$ : We have know that all closed set has the form $V(E)$ for some set $E$. Suppose $\mathfrak{p}_{x}$ is not maximal, then $\exists \mathfrak{m} \supsetneq \mathfrak{p}_{x}$ and for any $V(E)$ containing $x$, we have

$$
E \subseteq \mathfrak{p}_{x} \subsetneq \mathfrak{m} \Rightarrow \mathfrak{m} \in V(E)
$$

then $\mathfrak{m}$ is a closure point of $\{x\}$. Hence, $\{x\}$ is not closed, which is a contradiction.

$\Leftarrow$ : Suppose $\mathfrak{p}_{x}$ is maximal, then $V\left(\mathfrak{p}_{x}\right)=\{x\}$ (no other ideal containing it). Thus $\{x\}$ is closed.

ii): $\overline{\{x\}}$ is the intersection of all closed sets $V(E)$ containing $\mathfrak{p}_{x}$. Then $(E) \subseteq \mathfrak{p}_{x}$ for all $E$ since $V(E)=V((E))$. In this case, we have

$$
\overline{\{x\}}=\bigcap_{(E) \subseteq \mathfrak{p}_{x}} V(E)=V\left(\bigcup_{(E) \subseteq \mathfrak{p}_{x}} E\right)=V\left(\mathfrak{p}_{x}\right)
$$

iii): $y \in \overline{\{x\}}=V\left(\mathfrak{p}_{x}\right)$ means that $\mathfrak{p}_{x} \subseteq \mathfrak{p}_{y}$.

iv): For every pair of distinct points $x, y$, we have $\mathfrak{p}_{x} \neq \mathfrak{p}_{y}$. Then $\exists f \in \mathfrak{p}_{x} \backslash \mathfrak{p}_{y}$ or $\exists g \in \mathfrak{p}_{y} \backslash \mathfrak{p}_{x}$. Then $\mathfrak{p}_{x} \in V(f)$ but $\mathfrak{p}_{y} \notin V(f)$ or $\mathfrak{p}_{y} \in V(g)$ but $\mathfrak{p}_{x} \notin V(g)$. In this case, we know that $X$ is a $T_{0}$-space.

Remark: If every neighborhood of $x$ contains $y$, then $y \in \overline{(x)}$. If, in addition, every neighborhood of $y$ contains $x$, then $x \in \overline{(y)}$. Then we have $\mathfrak{p}_{x} \subseteq \mathfrak{p}_{y} \wedge \mathfrak{p}_{x} \subseteq \mathfrak{p}_{y} \Rightarrow x=y$.

![](https://cdn.mathpix.com/cropped/2024_07_11_5595162d419e08c2f239g-9.jpg?height=360&width=642&top_left_y=1268&top_left_x=701)

Exercise 19. A topological space $X$ is called irreducible if $X \neq \varnothing$ and if every pair of non-empty open sets in $X$ intersect, or equivalently if every non-empty open set is dense in $X$. Show that $\operatorname{Spec}(A)$ is irreducible if and only if the nilradical of $A$ is a prime ideal.

Proof.

