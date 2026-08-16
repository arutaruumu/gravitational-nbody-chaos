# Mathematical Model

## 1. State representation

Each body $\(i\)$ has mass $\(m_i\)$, position $\(\mathbf r_i\)$, and velocity $\(\mathbf v_i\)$.

The complete state is

$$
\[
X(t)=\{\mathbf r_i(t),\mathbf v_i(t)\}_{i=1}^{N}.
\]
$$

The default implementation is two-dimensional.

## 2. Newtonian gravity

For $\(i\ne j\)$,

$$
\[
\mathbf F_{ij}
=
Gm_im_j
\frac{\mathbf r_j-\mathbf r_i}
{|\mathbf r_j-\mathbf r_i|^3}.
\]
$$

The corresponding acceleration is

\[
\mathbf a_i
=
G\sum_{j\ne i}
m_j
\frac{\mathbf r_j-\mathbf r_i}
{|\mathbf r_j-\mathbf r_i|^3}.
\]

The implementation uses Plummer-like softening:

\[
|\mathbf r_j-\mathbf r_i|^3
\rightarrow
\left(
|\mathbf r_j-\mathbf r_i|^2+\epsilon^2
\right)^{3/2}.
\]

## 3. Conservation laws

Kinetic energy:

\[
K=\frac12\sum_i m_iv_i^2.
\]

Potential energy:

\[
U=-G\sum_{i<j}
\frac{m_im_j}
{\sqrt{r_{ij}^2+\epsilon^2}}.
\]

Total energy:

\[
E=K+U.
\]

For planar motion:

\[
L_z=\sum_i m_i(x_iv_{y,i}-y_iv_{x,i}).
\]

## 4. Numerical integration

Leapfrog / Velocity Verlet is used as the default long-term integrator.

\[
v_{n+1/2}=v_n+\frac{\Delta t}{2}a_n
\]

\[
r_{n+1}=r_n+\Delta t\,v_{n+1/2}
\]

\[
v_{n+1}=v_{n+1/2}+\frac{\Delta t}{2}a_{n+1}.
\]

## 5. Chaos metric

For two nearby simulations A and B,

\[
D(t)=
\sqrt{\sum_i
|\mathbf r_i^A(t)-\mathbf r_i^B(t)|^2}.
\]

The finite-time Lyapunov-like estimate is

\[
\lambda(t)=
\frac{\ln(D(t)/D_0)}{t}.
\]

A rigorous maximal Lyapunov exponent requires a renormalization-based algorithm and is planned as future work.

## 6. Computational complexity

Direct pairwise evaluation requires

\[
\frac{N(N-1)}{2}
\]

unique interactions, giving approximately

\[
O(N^2)
\]

work per force evaluation.
