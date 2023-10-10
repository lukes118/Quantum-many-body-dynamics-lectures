---
layout: page
title: About
permalink: /lecture_1/
---

Lecture 1: Quantum many body dynamics
========================================
> key: [R]=Rodderich; [P]=Peter; [M]=Marin
> [Q]=question [A]=answer

Intro:
------
[R] Not everything covered by this despite very broad title.
There has been a convergence on ideas from different communities.
First we  will need to establish a common vocabulary.
The course will focus on developments in last ten years.
The course is fairly self contained with some pre req knowledge of basic qm and stat mech.

We will start with some discussion on equilibrium physics, then beyond equilibrium - a vast field.
We will be interested in:

- Quenches 
- localised/ glassy sytems ([R]'s favourite accoring to Panos)
- (less so open systems)

Thermodynamics:
---------------

**Thermodynamics** was essentially completed at the end of the nineteenth century.
It's formulation was before microscopics, and makes/needs no reference to microscopics in its formulation.
The first two central concepts are:
- **Equilibration**: a sytem eventually reaches a steady state if you sit and wait for long enough
- **Thermalisation**: where very little information is required to describe this steady state e.g.
- N - $\mu$, E - T, V - P

**Instructions**:
1) find the constraints e.g energy, of particle number etc.
2) maximise the entropy subject to these constraints

Nice result:
Knowing an electronic system has a compressiblity you can derive quantised response to a magnetic field
without reference to Landau levels ie. microscopics.

Maxwell's relations enforce certain consitencies.

> What about alternatives?

Thermodyamics predicted its own demise. Physicists even at max planck found predictions made e.g
black body radiation weren't obeyed by classical equipartition.

Statistical Physics/ Mechanics:
-------------------------------
This is a very different formulation to that of thermodynamics. Essentially it's microscopic approach.
First find the partition function, $Z$ (way more info required to calc.)

> $$Z = \sum_{i} e^{- \beta E_i}  \qquad \beta = \frac{1}{k_B T} $$

Consider the thermodynamic relation,   

> $F = U - TS$ 

We can get this from statistical physics. Replace discrete sum by an integral

> $$Z = \int_{E_{min}}^{E_{max}} dE \: \rho(E) \: e^{-\beta E} =
\int_{E_{min}}^{E_{max}} dE \:  \exp \left(-\beta E + S\right) $$

This leads to saddle point approximation of integral i.e. dominant conribution by maximising the Free energy, $F$.

Quantum Mechanics:
------------------
Enter the Schrödinger equation: 

> $$i \frac{d}{dt} |\psi(t) \rangle  = \hat{H} |\psi(t) \rangle $$

How do we go from this formulation with time to stat. mech.? ([R] makes no mention of corresponding problem for classical mechanics)

We get the eigenstates and whack them into the parition function and we're good to go.

Many body sytems have a strong personal and community dependence.
e.g. what is: quanum? many-body? dynamics? 

The many body formulation can formulated in distinction to some other contexts. 
some other contexts:

- **Single particle**
- **Few body/ mesoscopic**: quantum dots, 
- **Integrable**: effectively single particle physics. An example being the slater determinant. Here there is a description in terms of occupancies.
A slighlty more "hardcore" integrable system example would be solution via beta ansatz. E.g. thought of in terms of non interacting domain walls.

Many body is what's left over once these special cases have been dealt with.

$N_a =  6*10^{23} \: $  but exact diagonilation $\implies$ 50 sites will suffice for all intensive purposes.


Spin $\frac{1}{2}$ chain:
----------------
We need a minimal model for generic many body sytems and
the simplest will be two degrees of freedom per site.
> *Unless you think in terms of Anyons?*

$S = 1/2 \implies 2S + 1 \; \textrm{states} = 2  = \{ \uparrow, \downarrow \}$

$N$ sites $\implies 2^N$ states

Discrete as much as possible:
- space (sites) are discrete
- local configuration space is discrete

Lieb-Robbinson bounds don't hold in continuous sytems (how fast information can travel)

$l_P = \sqrt{\frac{\hbar G}{c^2}}$ (planck length)

    There was some discussion here about the Planck length and the universe ...

There is some continuousness though ...

$ c_1 |\uparrow \rangle + c_2 |\downarrow \rangle \rightarrow 
\cos \left( \frac{\theta}{2} \right) \begin{bmatrix} 1 \\ 0 \end{bmatrix} + 
\sin \left( \frac{\theta}{2} \right) \begin{bmatrix} 0 \\ 1 \end{bmatrix} $ 


n.b. you can't dump arb. amount of energy into this system in contrast with a S.H.O where $e = \left( n + \frac{1}{2} \right) \; \omega$ and n can be arb. large.

Another example being hopping on a chain with one band:

> $e(k) = -2 t \cos(k)$ 

The kinetic enrgy is bounded by t as opposed to a free particle in the continuum.

[Q] What does generic mean?

[A] A notion of universality? Don't really know how many classes there are, but expect these classes to be measure zero. 
Typically give me a hamiltonian and if I add a couple of terms, it should be generic i.e. take us away from integrability.

### $J_1 - J_2$ Ising Model:

> $$ E({S_i}) = \sum_{k=1}^N J_1 \; S_k^z  S_{k+1}^z + 
J_2 \; S_k^z S_{k+2}^z  \tag{1} $$

$J_2 = 0$ classical configuration gives us the computational basis

Energies in $(1)$ indexed by number of domain walls and huge degeneracies as doesn't care where the domain walls are. 

<!--Centered Image Start-->
<div style="text-align: center;">
    <img src="https://www.inrim.it/sites/default/files/2022-05/spins_960x300.gif" alt="drawing" width="300"/>
</div>

### $H_{TFI}$ (Transverse field ising model):
We know add a term which takes the computational basis away from the eigenstates of the hamiltonian.

> $$ H_{TFI} = H_{exch} + \Gamma \sum_k S_k ^ x $$

Random matrix theory says:

> $ \begin{bmatrix} 0 & \epsilon \\ \epsilon & 0\end{bmatrix} $


lifts the degeneracy and we can see this in the level statistics. 

TFI is integrable, some statement about what is a generic hamiltonian
but adding $J_2$ lets us tune from an integrable model to a non integrable model!

Think of integrablility as follows:
- domain wall in ising model is a non interactinfg free paricle (TFI no $J_2$)
- given $J_2$ how strong are the effective interactions ($\gamma$ causes the spin flips that move the domain wall)
- can have scattering of domain walls e.g. two into four 
- people may be looking at observables that are not in generic systems even with non-integrable system

> n.b. $J_1 -J_2 - \textrm{TFI}$ simplest generic non-integrable hamiltonian

Prethermalisation
-----------------
Different convervation laws than final thermodynamic regime
More discussed on this in the coming course.

Eigenstates in the middle of the spectrum:
---------------------------
Spacing of eigenstates:

> $$ \delta_E = \frac{\epsilon N}{2^N} \sim 2^{-N} $$

where,

> $$ E_{max} - E_{min} = \epsilon N $$

Spacing is exponentially small in system size.
Fermi liquid/ Fermi gas distinction
Phonon description might ber relevant to arb. long times
Neither relevant for today (typical cond. matt setup)

Finite energy described by thermodynamics after some pre-thermal scale (staying close to middle of spec.)

> How relevant is an eigenstate in the middle of the spectrum?

Heisenbergy uncertainty 
$ \Delta_E  \cdot \delta_t \sim 1 $
so you cant prepare it in time as $\delta_t$ becomes exponentially large in system size.
You can't even write it down.

MPS makes writing it down relevant for ground state physics, but we are in the middle of the spectrum.

> Philosophy of does it exist? 

What's dynamical?
-----------------
> $$ \langle S_a(t) \cdot S_b(0) \rangle $$
> $$ = Tr\{e^{-\beta \hat{H}} S_a(t)S_b(0)\} $$
>
> $$ = \sum_{\{i\},\{j\}} \langle i | e^{-\beta H} 
e^{iHt} \; S_a(0) \; e^{-iHt} |j \rangle
\langle j|  \; S_b(0) \; |i \rangle $$
>
> $$ = \sum_{i, j} e^{-\beta E_i + it(E_i - Ej)}  
\langle i| S_a(0) |j \rangle \langle j|S_b(0)|i \rangle $$

Liemann representation of things

Chaos questions: In principle we can reverse time due to unitarity but in practice we cannot due to weak perturbation making very different trajectories.

Formulate chaos in terms of:
- scrambling: how does information in principle get lost?
- out of time ordered correlators: OTOCs, if i perturb here, propagate, perturbation and propagate back, how far apart am I from where I started? 

The Heisenberg picture: 
> $$ i \frac{dS(t)}{dt} = [H, S] + \frac{\partial S}{\partial t} \tag{2}

In some sense time evoultion of the matrix incorporates time evolution of all wave functions.
Whilst Shroedinger and HB. picture the same if solving for all eigenstates can be different in practice.
H.b picture and operator spreading will shed some light on things.

Non - equilibrium:
------------------
Most things are not equilibrium, so we need to start simpler i.e. closer to some of the
concepts we use from equilibrium.

No free energy out of equilibrium, are there phases? 
Are there phases which exist only beyond equilbrium - time crystals => a spatio-temporal form of order
Found in context of Floquet systems (periodically driven.)

#### Start driving things: 

$$ H = H_0 + H_{driven} $$
$$ H_{driven} = \cos(n \omega t) \; H_n \tag{3} $$  

(3) has frequencies that are harmonics of the fundamental drive.
{can also think of quasi peridic systems hongzheng zhoa}

Schroedinger must be noted as an effective theory and unlikely in our lifetime we will have any resolution
to unification problem in our lives.
Classical behaviour is an emergent behaviour of quatum problems which are very common.

Any computation can be mapped onto a turing machine?
Are there computations a turing machine can't do in a reasonable amount of time? 
NISQ = think of as many body systems far from a quantum computer
NAND gat universal for classical computations
quant computing is an extension of this with unitary gates
seq. of gates a universal way of describing ....

Summary:
--------
Intro to the course and a minimal model for what a generic quantum many body system should be,
namely the n.n.n TFI can tune in and out of integrability.
clean, conscise and clear idea of what to say and to show

Ref:
----

Todo:
-----
[ ] email peter claeys to inform attendance: claeys@pks.mpg.de

[ ] (check out website which will come after sending the email)

[ ] model TFI with J1 J2 and look at integrable vs generic behaviour

[ ] look at QSpin from Marin
