Some Interesting Properties in System of Linear

First-order ODE

Yifan Li

November 2023

> **1 Linear Independence of Solutions**

***Remark***: We say that a set of vector functions *{X*1*, . . . , Xn}*
to be **linearly dependent** on an interval *I* if

*∃c*1*, . . . , ck* not all zero*, ∀t ∈I* (*c*1*X*1(*t*) + *. . .* +
*ckXk*(*t*) = 0)*.*

> If a set of vector functions is not linearly dependent on *I*, then it
> is said to be **linearly independent**.
>
> **Theorem 1.1.** *If a set of solution vectors X*1*, . . . , Xn of a
> homogeneous system of order n is linearly dependent at some t*0 *∈I,
> then it is linearly dependent at any point t ∈I. Also, if it is
> linearly independent at some t*0 *∈I then it is linearly independent
> at any t ∈I*\
> *Proof.* We know that any solution vector can be written as *Xi* =
> *etAXi*(0). In fact, *etA*is just an invertible matrix, which can be
> regarded as a bijective linear transformation, which conserves the
> linear independence.
>
> There is another way to think about it. If *X*1*, . . . , Xn* are
> linearly dependent at *t*0 *∈I*, then

*∃c*1*, . . . , cn* (*c*1*X*1(*t*0) + *c*2*X*2(*t*0) + *. . .* +
*cnXn*(*t*0) = 0)

> Let *X*(*t*) = *c*1*X*1(*t*) + *. . .* + *cnXn*(*t*), both *X*(*t*)
> and 0 are solutions to *X′*= *AX* satisfying the initial value
> condition *X*(*t*0) = 0. Thus they are equal by the

+-----------------------+-----------------------+-----------------------+
| > uniqueness of the   |                       |   ------------------  |
| > solution, i.e. *∀t  |                       |                       |
| > ∈I*                 |                       |   ------------------  |
| > (*c*1*X*1(*t*) + *. |                       |                       |
| > . .* + *cnXn*(*t*)  |                       |                       |
| > = 0).               |                       |                       |
+=======================+=======================+=======================+
| **2**                 | > **Laplace Transform |                       |
|                       | > of** *etA*          |                       |
+-----------------------+-----------------------+-----------------------+

> Before we introduce the Laplace transform of *etA*, we need to know
> what is *etA*. We may define it by a Taylor series.
>
> **Definition 2.1.**

+-----------+-----------+-----------+-----------+-----------+-----------+
| > *etA*:= | *∞*       | > *tk*\   | *n*       | > *tk*\   | > \(1\)   |
| > *I* +   |           | >         |           | >         |           |
| > *At*    |           |  *k*!*Ak* |           |  *k*!*Ak* |           |
| > +*A*2   |           | > = lim   |           |           |           |
| >         |           | > *n→∞*   |           |           |           |
|  2!*t*2 + |           |           |           |           |           |
| > *A*3    |           |           |           |           |           |
| >         |           |           |           |           |           |
|  3!*t*3 + |           |           |           |           |           |
| > *. . .* |           |           |           |           |           |
| > :=      |           |           |           |           |           |
+===========+===========+===========+===========+===========+===========+
|           | *k*=0     |           | *k*=0     |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+

1

> From the definition of the exponential of a matrix, we may find

+-----------------+-----------------+-----------------+-----------------+
| **Theorem       | *detA*          | > =*etAetAA*    | 2               |
| 2.1.**          |                 |                 |                 |
+=================+=================+=================+=================+
| **Theorem       | *dt*            | > =*eeA*        | 2               |
| 2.2.**          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 | > *L{etA}* =    |                 | \(3\)           |
|                 | > (*sI −A*)*−*1 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

> *Proof.*
>
> *L{etA}*(*sI −A*) = *sL{etA} −A}*\
> = *sL{etA} −L{AetA}*\
> = *sL{etA} −L{*(*etA*)*′}*\
> = *sL{etA} −*(*sL{etA} −e*0*·A*)\
> = *I*

+-----------------------+-----------------------+-----------------------+
| > Thus *L{etA}* =     |                       |   ------------------  |
| > (*sI −A*)*−*1       |                       |                       |
|                       |                       |   ------------------  |
+=======================+=======================+=======================+
| **3**                 | > **Fundamental       |                       |
|                       | > Matrices**          |                       |
+-----------------------+-----------------------+-----------------------+

> For the homogeneous system *X′*= *AX*, we can find its general
> solutions, which can be determined by a fundamental set of solutions
> for the system.
>
> **Definition 3.1.** *Fundamental Matrix*\
> *Let X*1(*t*)*, . . . , Xn*(*t*) *be fundamental set of solutions of
> X′*= *AX. Then the matrix*

+-----------+-----------+-----------+-----------+-----------+-----------+
| Φ(*t*) =  | *X*1(*t*) | *X*2(*t*) | *. . .*   | >         | \(4\)     |
|           |           |           |           | *Xn*(*t*) |           |
+===========+===========+===========+===========+===========+===========+
+-----------+-----------+-----------+-----------+-----------+-----------+

> *is said to be a **fundamental matrix** for the system X′*= *AX. In
> addition, the general solution can be determined by* Φ(*t*) *C where C
> is a constant vector.*
>
> **Theorem 3.1.** *If* Φ(*t*)*,* Ψ(*t*) *are both fundamental matrices
> for the same system, then there exists a constant matrix C such that*
> Φ(*t*) = Ψ(*t*) *C. In particular,*Φ(*t*) = *etA*Ψ(0)*.*

+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| *Pr   | *X*1  | *. .  | *Xn*  | and   | *Y*1  | *. .  | >     | > ,   |
| oof.* | (*t*) | .*    | (*t*) | Ψ     | (*t*) | .*    |  *Yn* | >     |
| Let   |       |       |       | (*t*) |       |       | (*t*) | since |
| Φ     |       |       |       | =     |       |       |       |       |
| (*t*) |       |       |       |       |       |       |       |       |
| =     |       |       |       |       |       |       |       |       |
+=======+=======+=======+=======+=======+=======+=======+=======+=======+
+-------+-------+-------+-------+-------+-------+-------+-------+-------+

Ψ(*t*) is a fundamental matrix, any solution to the system can be
written as a

+-----------------------------------------------------------------------+
| > linear combination of *{Xi*(*t*)*}*, then we have                   |
| >                                                                     |
| > *xn,j*(*t*) *x*1*,j*(*t*)                                      |
| >                                                                     |
| > *x*2*,j*(*t*)                                                       |
| >                                                                     |
| > . . . = *Xj*(*t*) =                                             |
| >                                                                     |
| > *k*=1\                                                              |
| > *n*                                                                 |
| >                                                                     |
| > *ck,jYk*(*t*) = *n*                                            |
| >                                                                     |
| > *k*=1*ck,jyn,k*(*t*)\                                               |
| > *k*=1*ck,jy*1*,k*(*t*)                                              |
|                                                                       |
| *n*                                                                   |
|                                                                       |
| *k*=1*ck,jy*2*,k*(*t*)                                                |
|                                                                       |
| > . . . \                                                        |
| > *n*                                                                 |
| >                                                                     |
| > The *i −th* component of *Xj*(*t*) is*n k*=1*ck,jyi,k*(*t*) Thus we |
| > may find that                                                       |
|                                                                       |
| *n*                                                                   |
|                                                                       |
| > Φ(*t*) = *k*=1*yi,k*(*t*) *ck,j* = Ψ(*t*) *C*                       |
+=======================================================================+
+-----------------------------------------------------------------------+

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

2

> **4 Some Interesting Exercises**
>
> **Application of Laplace Transform of** *etA*

+-----------------+-----------------+-----------------+-----------------+
| > **Example     | 0               | 1               | > *. Compute    |
| > 4.1.** *Let   |                 |                 | > etA*          |
| > A* =          |                 |                 |                 |
+=================+=================+=================+=================+
|                 | *−*1            | 0               |                 |
+-----------------+-----------------+-----------------+-----------------+

> **Solution 4.1.** *We first consider the Laplace transform of etA.*

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"></th>
<th colspan="6" rowspan="2"><em>L{etA}</em> = (<em>sI
−A</em>)<em>−</em>1=</th>
<th><em>s</em></th>
<th rowspan="2"><em>−</em>1 <em>S</em></th>
<th rowspan="3"><blockquote>
<p><em>−</em>1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>1</th>
</tr>
<tr class="header">
<th rowspan="3">=</th>
<th colspan="2">1</th>
<th colspan="2"><em>s</em></th>
<th colspan="3"><blockquote>
<p>1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th rowspan="2"></th>
<th colspan="2"><em>s</em>2+ 1</th>
<th colspan="2" rowspan="2"><blockquote>
<p><em>−</em>1 1</p>
</blockquote></th>
<th colspan="3" rowspan="2"><blockquote>
<p><em>s</em></p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th colspan="2"><em>s</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td rowspan="2">=</td>
<td colspan="3" rowspan="2"><em>s</em>2+1 <em>s</em>2+1<em>−</em>1</td>
<td colspan="4"><em>s</em>2+1<br />
<em>s</em></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4"><em>Thus</em></td>
<td colspan="4"><blockquote>
<p><em>s</em>2+1</p>
</blockquote></td>
<td rowspan="4"></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>= <em>L{</em>cos <em>t}</em></p>
</blockquote>
<p><em>L{−</em>sin <em>t}</em></p>
<p>cos <em>t</em></p>
<blockquote>
<p>= <em>L{</em> <em>−</em>sin <em>t</em></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><em>L{</em>sin <em>t} L{</em>cos <em>t}</em></p>
<p>sin <em>t</em></p>
<p>cos <em>t</em> <em>}.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2" rowspan="2"><em>etA</em>=</td>
<td colspan="3">cos <em>t</em></td>
<td colspan="3"><blockquote>
<p>sin <em>t</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><em>−</em>sin <em>t</em></td>
<td colspan="3"><blockquote>
<p>cos <em>t</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> **Example 4.2.** *Find the general solution for the system*
>
> *x′*\
> *x′*
>
> 2= *x*1*−x*2\
> 1= *−x*1
>
> **Solution 4.2.** *The system above can be written as X′*= *AX where*

+-----------------------+-----------------------+-----------------------+
| *A* =                 | *−*1 1                | > 0                   |
+=======================+=======================+=======================+
|                       |                       | > *−*1                |
+-----------------------+-----------------------+-----------------------+

> *Then*

+---------+---------+---------+---------+---------+---------+---------+
| *       |         |         | *s* + 1 | 0       | *−*1    |         |
| L{etA}* |         |         |         |         |         |         |
| = (*sI  |         |         |         |         |         |         |
| −A      |         |         |         |         |         |         |
| *)*−*1= |         |         |         |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
|         |         |         | > *−*1\ | *s* + 1 |         |         |
|         |         |         | > 0     |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| =       | 1       | *s* + 1 |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | (*s* +  | 1       | > *s* + |         |         |         |
|         | 1)2     |         | > 1     |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| =       | 1       | 0       |         | *e−t*\  |         |         |
|         |         |         |         | *te−t*  |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         | >       |         | = *L{*  |         | 0       | > *}*   |
|         |  *s*+1\ |         |         |         |         |         |
|         | > 1     |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         | 1       |         |         | *−t*    |         |
+---------+---------+---------+---------+---------+---------+---------+
| (       |         | *s*+1   |         |         | > *e*   |         |
| *s*+1)2 |         |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+

> *Thus the fundamental matrix can be written as*

+---------+---------+---------+---------+---------+---------+---------+
| Φ(*t*)  | *e−t*   | 0       |         | \+ *c*2 | 0       | > *.*   |
| =       |         |         |         |         |         |         |
+=========+=========+=========+=========+=========+=========+=========+
|         | *te−t*  | >       |         |         |         |         |
|         |         |  *e−t,* |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
| > *and  |         |         | *e−t*\  |         |         |         |
| > the   |         |         | *te−t*  |         |         |         |
| >       |         |         |         |         |         |         |
| general |         |         |         |         |         |         |
| > s     |         |         |         |         |         |         |
| olution |         |         |         |         |         |         |
| > is    |         |         |         |         |         |         |
| >       |         |         |         |         |         |         |
| X*(*t*) |         |         |         |         |         |         |
| > =     |         |         |         |         |         |         |
| >       |         |         |         |         |         |         |
|  Φ(*t*) |         |         |         |         |         |         |
| > *C* = |         |         |         |         |         |         |
| > *c*1  |         |         |         |         |         |         |
+---------+---------+---------+---------+---------+---------+---------+
|         |         |         |         |         | *e−t*   |         |
+---------+---------+---------+---------+---------+---------+---------+

3

> **Application of Fundamental Matrices**
>
> **Example 4.3.** *Prove that AB* = *BA implies that BetA*= *etAB.*
>
> *Proof.* Let Φ = *BetA*and Ψ = *etAB*, then we may find that Φ*′*=
> *BAetA*= *ABetA*= *A*Φ and Ψ*′*= *AetAB* = *A*Ψ. Thus Φ and Ψ are
> fundamental matrices of *X′*= *Ax*. When *t* = 0 one could find that
> Φ(0) = Ψ(0) = *B*, thus Φ(*t*) =

+-----------------------------------+-----------------------------------+
| > Ψ(*t*).                         |   ------------------------------  |
|                                   |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

> **Example 4.4.** *Prove that etAetB*= *et*(*A*+*B*)*if AB* = *BA.*

*Proof.* Let Φ(*t*) = *etAetB*and Ψ(*t*) = *et*(*A*+*B*). Notice that
the Ψ(*t*) is just a

> fundamental matrix for the system

*X′*= (*A* + *B*)*X.*

> For the Φ(*t*), we have

(*etAetB*)*′*= *AetAetB*+ *etABetB*

= (*A* + *B*)*etAetB*

Thus it is also a fundamental matrix for *X′*= (*A* + *B*)*X*. Let *t* =
0, we may

+-----------------------------------+-----------------------------------+
| > find that the Φ(0) = Ψ(0) =     |   ------------------------------  |
| > *I*, thus they are the same.    |                                   |
|                                   |   ------------------------------  |
+===================================+===================================+
+-----------------------------------+-----------------------------------+

4
