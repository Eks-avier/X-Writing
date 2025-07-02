# Formulas for Electromagnetism

## Magnetic Force

### Units

- Tesla is the unit of magnetic fields; it is denoted by $B$.

$$
T = \frac{\text{Newton-second}}{\text{Coloumb-meter}}
$$
$$
T = \frac{\text{Newton}}{\text{Amp-meter}}
$$

### Formulas

#### 1. Magnetic Force on a **moving charge**: $F = |q|vB\sin \phi$

Where:
- $q$ is the *charge*
- $v$ is the *velocity*
- $B$ is the *magnetic field*
- $\phi$ is the angle *between the direction of $v$ and $B$*

#### 2. Magnetic Force as a **vector product**: $\vec{F} =q \vec{v} \times \vec{B}$

#### 3. Motion of Charged Particles in a (uniform) Magnetic Field: $R = \frac{mv}{|q|B}$

Where: $F_{c} = F_{B}$
- Derived from:
	- $F_{c} = m \frac{v^{2}}{R}$
	- $F_{b}=qvB\sin \theta$

## Mag. Force on a **Wire** and **Torque**

### Units

- Torque, which is $\tau = F\times l$
	- Where: $\text{force}\times\text{lever arm}$
	- **Unit**: $Nm$

### Formulas

#### 1. Force on a **current in a Mag. field**: $F=qvB\sin \theta$

Derived from: $F=\left( \frac{\Delta q}{\Delta t} \right)(v\Delta tB\sin\theta)$
- Then: $F=ILB\sin \theta$
	- Where:
		- $I$ is *current*
		- $L$ is the *length of the wire*
		- $B$ is the *magnetic field*
		- $\theta$ is the angle *between* the *direction* of $I$ and $B$

#### 2. Net Torque: $IAB\sin \phi$

Derived from: $ILB\left( \frac{1}{2}w\sin \phi \right)+ILB\left( \frac{1}{2}w\sin \phi \right)$

#### 3. Torque on a **current-carrying coil**: $\tau=NIAB\sin \phi$

Where:
- $N$ is the is the number of *turns* or *loops* in the coil.
- $I$ is the *current*
- $A$ is the *area of the loop*, depending on the shape of the loop
- $B$ is the *magnetic field*
- $\phi$ is the angle *between* the *magnetic field* and the *normal to the loop*

#### 4. Magnetic Moment: $\mu = NIA$

Where:
- $N$ is the number of *turns* or *loops* in the coil
- $I$ is the *current*
- $A$ is the *area* of the loop

## Electromagnets

### Formulas

#### 1. Mag. Fields Produced by a **long, Straight wire**: $B=\frac{\mu_{o}I}{2\pi r}$

Derived from: $F = qvB\sin \theta = qv (\frac{\mu_{o}I}{2\pi r})\sin \theta$
- Where: $B = \frac{\mu_{o}I}{2\pi r}$

Where:
- $\mu_{o}=4\pi \times 10^{-7} \frac{\text{Tm}}{A}$; this is called the **permeability of free space**.
- $r$ is the *distance* from the wire to where the mag. field is determined.
- $I$ is *current*.

#### 2. Mag. Fields Produced by a **loop of wire**: $B = \frac{N\mu_{o}I}{2R}$

Where:
- $R$ is the radius of the loop
- $\mu$ is the permeability of free space
- $N$ is the number of turns or loops
- $I$ is the current

#### 3. Mag. Fields Produced by a **solenoid**: $B = \mu_{o}nI$

Where:
- $n$ is the number of *turns per unit length*.

## Electromagnetic Induction

### Unit

- Weber (**Wb**)
- Henry (**H**)
	- The unit of self-inductance

### Formulas

#### 1. Magnetic flux: $\Phi_{B} = BA\cos \phi$

Where:
- $\phi$ is the angle between the direction of $B$ and the *normal* to the surface.

Note:
- When $\phi$ is $0\degree$, the flux $1$, hence it is maximized.
- When $\phi$ is $90\degree$, the magnetic field lines are parallel to the surface, and no flux passes through.
#### 2. Faraday's Law: $EMF = -N \frac{\Delta \Phi}{\Delta t}$

Derived from: $EMF = -N\left( \frac{\Phi-\Phi_{o}}{t-t_{o}} \right)$

Where:
- $\Phi - BA\cos \phi$
- $N$ is the number of turns or loops
- $t$ is time

#### 3. Mutual Inductance: $\varepsilon=-N \frac{\Delta \Phi}{\Delta t}$

#### 4. Self Inductance: $\varepsilon=-L \frac{\Delta I}{\Delta t}$

Where:
- $L$ is the *length*

To get $L$: $L=\frac{N\Phi}{I}$

#### 5. Energy stored in an inductor: $\frac{1}{2}LI^{2}$



---

$n = \frac{N}{l}$
$N=nl$