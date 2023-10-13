Lecture 2: Quantum many body dynamics              
====================================================              
#### Date: 2023-10-12              
              
Intro/ Recap:              
-------------              
[M] Go to [course website](https://www.pks.mpg.de/condensed-matter/teaching) for extra details on the course. Today we will be learning some of Marin's [quspin](https://github.com/QuSpin/QuSpin) package for ED with spin chains. (Remeber our minimal model from last lecture will be TFI with n.n.n.)


## Spin chains 
We will start with a single spin and then build a spin chain.

### 2 level system:
- Hilbert space $\mathbb{C}^2$
- basis of operators in terms of Pauli matrices, $ \sigma^x, \sigma^y, \sigma^z$ and $\mathbb{I}$
- States parameterised by $\theta$ and $\phi$ gives notion of the Bloch sphere.
- most general Hamiltonain (after subtracting energy offset) $ H = \vec{h}\cdot \vec{\sigma}$

In **quspin**:

```python
from quspin.basis import spin_basis_1d

basis_1 = spin_basis_1d(L=1) # single spin-1/2 
```

### 2 spins:
- $ j \in \{0, 1\} $ labels particle
- Hilbert space $\mathbb{C}^4 = \mathbb{C}^2 \times \mathbb{C}^2   $
- label states according to a bitstring

Now we implement the XXZ model for a 2 site spin chain:

$$ H = \sum_{\langle i, j \rangle}
J_z \sigma_i^z \sigma_j^z + \frac{J_{xy}}{2}\left( \sigma_i ^+ \sigma_j^- + \sigma_i^- \sigma_j ^+
\right)$$

### Entanglement

Can calculate von Neumann entropy by tracing out subsystem from density matrix, $\rho$ to get the reduced density matrix, $\rho_1$ and then calculate $ S = -Tr\{\rho_1 \ln \rho_1 \}$. 

But we can also calculate Renyi-$\alpha$ entropy, $S^\alpha = \frac{1}{1-\alpha} \log Tr \{ \rho_1 ^\alpha\}$

$$ \lim_{\alpha \rightarrow 1} S^{\alpha} = S $$

Von Neumann cannot be calculated exerimentally but attempts have been made with Renyi entropy.

[Q] What is the physical meaning of Renyi entropy and its relation to the V.N entropy.

[A] $\rho^2$ is related to the purity which is why this could be measured in experiment. All Renyi entropies contain same information.

### Symmetries

System has a symmetry if there is an operator $S$ where $[S, H] = 0$.

Can have simulataneous eigenbasis. By choosing a basis, in which S is diagonal, block diagonalises H and can now work in blocks labled by the eigenvalues/ quantum numbers of S.

#### Example spin exhange symmetry

$$ S: \vec{\sigma}_1  \leftrightarrow \vec{\sigma}_2 $$

Symmetry described by $\mathbb{Z}_2$ group. (Repeating the symmetry operation takes us back to inital state).

List of symmetries:
- invesrsion
- translation
- on site inversion

#### Ball park of system sizes:

- laptop: 18 sites
- cluster: ~30 sites
- super computer: 50 sites

See notebook on the website for implementation of XXZ in quspin.

### Density of states DOS

$$ \rho(E) = \sum_i \delta(E - E_i) $$

For ergodic spin chains, this resembles a Guassian.

### Time evolution

Two types of time evolution:
- **quench**: Turn on hamiltonian and track the time evolution
- **drives**: psi evolves according to a time dependent hamiltonian.

#### quench:
we want to compute:
1. the time-evolved state
2. expectation value as a function of time
3. time evolution of the entanglement entropy


[previous](/lecture-notes/lecture_notes.1.md)