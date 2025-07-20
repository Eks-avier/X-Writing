# Magnetism

## Fundamental Constants and Units

### Key Constants

- **Permeability of free space**: $\mu_0 = 4\pi \times 10^{-7} \, \frac{\text{T·m}}{\text{A}}$
- **Speed of light**: $c = 3.00 \times 10^8 \, \text{m/s}$

### Units

- **Magnetic field (B)**: Tesla (T)
  - $1 \, \text{T} = \frac{\text{N·s}}{\text{C·m}} = \frac{\text{N}}{\text{A·m}}$
- **Magnetic flux (Φ)**: Weber (Wb) = T·m²
- **Inductance (L, M)**: Henry (H) = V·s/A
- **EMF**: Volt (V)

---

## Magnetic Forces

### 1. Force on a Moving Charge

**Basic Formula:**
$$F = |q|vB\sin\phi$$

Where:
- $q$ = charge (C)
- $v$ = velocity (m/s)
- $B$ = magnetic field (T)
- $\phi$ = angle between $\vec{v}$ and $\vec{B}$

**Vector Form:**
$$\vec{F} = q\vec{v} \times \vec{B}$$

**Key Points:**
- Maximum force when $\phi = 90°$ (perpendicular motion)
- Zero force when $\phi = 0°$ or $180°$ (parallel motion)
- Direction determined by right-hand rule

### 2. Circular Motion in Magnetic Fields

**Radius of Circular Path:**
$$R = \frac{mv}{|q|B}$$

**Derivation:** Set magnetic force equal to centripetal force
- $F_{\text{magnetic}} = F_{\text{centripetal}}$
- $qvB = \frac{mv^2}{R}$
- Solving for R: $R = \frac{mv}{qB}$

**Applications:**
- Particle accelerators
- Mass spectrometers
- Cyclotron motion

### 3. Force on Current-Carrying Wire

**Force on Straight Wire:**
$$F = ILB\sin\theta$$

Where:
- $I$ = current (A)
- $L$ = length of wire (m)
- $B$ = magnetic field (T)
- $\theta$ = angle between current direction and $\vec{B}$

**Derivation from charge motion:**
- $F = qvB$ for moving charge
- Current: $I = \frac{\Delta q}{\Delta t}$
- Distance: $L = v \Delta t$
- Therefore: $F = \frac{\Delta q}{\Delta t} \cdot v \Delta t \cdot B = ILB$

---

## Torque on Current Loops

### Single Loop

$$\tau = IAB\sin\phi$$

Where:
- $I$ = current (A)
- $A$ = area of loop (m²)
- $B$ = magnetic field (T)
- $\phi$ = angle between $\vec{B}$ and normal to loop

### Multiple Turns (Coil)

$$\tau = NIAB\sin\phi$$

Where $N$ = number of turns

### Magnetic Moment

$$\mu = NIA$$

**Units**: A·m²

**Torque in terms of magnetic moment:**
$$\tau = \mu B \sin\phi$$

---

## Magnetic Fields from Currents

### 1. Long Straight Wire

**Field at distance r:**
$$B = \frac{\mu_0 I}{2\pi r}$$

**Key Features:**
- Field forms circular patterns around wire
- Direction given by right-hand rule
- Field strength decreases as $\frac{1}{r}$

### 2. Circular Loop (at center)

**Single Loop:**
$$B = \frac{\mu_0 I}{2R}$$

**Multiple Turns:**
$$B = \frac{N\mu_0 I}{2R}$$

Where:
- $R$ = radius of loop (m)
- $N$ = number of turns

### 3. Solenoid (Inside, Near Center)

**Field inside solenoid:**
$$B = \mu_0 nI$$

Where $n$ = turns per unit length

**Alternative form:**
$$B = \frac{\mu_0 NI}{l}$$

Where:
- $N$ = total number of turns
- $l$ = length of solenoid (m)
- $n = \frac{N}{l}$

**Key Features:**
- Uniform field inside (for long solenoid)
- Field approximately zero outside
- Field lines are parallel inside

---

## Electromagnetic Induction

### 1. Magnetic Flux

**Definition:**
$$\Phi_B = BA\cos\phi$$

Where:
- $B$ = magnetic field (T)
- $A$ = area of surface (m²)
- $\phi$ = angle between $\vec{B}$ and normal to surface

**Key Angles:**
- $\phi = 0°$: Maximum flux ($\Phi = BA$)
- $\phi = 90°$: Zero flux (field parallel to surface)

### 2. Faraday's Law

**Induced EMF:**
$$\mathcal{E} = -N\frac{\Delta\Phi}{\Delta t}$$

**Expanded form:**
$$\mathcal{E} = -N\frac{\Phi_f - \Phi_i}{t_f - t_i}$$

**Key Points:**
- Negative sign indicates Lenz's law (opposes change)
- EMF induced only when flux changes
- Change can occur through:
  - Changing $B$
  - Changing $A$
  - Changing $\phi$ (orientation)

### 3. Lenz's Law

**Statement:** The induced current flows in a direction to oppose the change causing it.

**Application Steps:**
1. Determine direction of flux change
2. Find direction of induced field to oppose change
3. Use right-hand rule to find induced current direction

### 4. Motional EMF

**Rod moving through magnetic field:**
$$\mathcal{E} = BLv$$

Where:
- $B$ = magnetic field (T)
- $L$ = length of rod (m)
- $v$ = velocity perpendicular to B (m/s)

---

## Inductance

### 1. Self-Inductance

**Induced EMF:**
$$\mathcal{E} = -L\frac{\Delta I}{\Delta t}$$

**Inductance definition:**
$$L = \frac{N\Phi}{I}$$

**Units:** Henry (H) = V·s/A

### 2. Mutual Inductance

**Induced EMF in secondary:**
$$\mathcal{E}_s = -M\frac{\Delta I_p}{\Delta t}$$

Where:
- $M$ = mutual inductance (H)
- $I_p$ = current in primary coil (A)

### 3. Energy Stored in Inductor

$$U = \frac{1}{2}LI^2$$

**Units:** Joules (J)

---

## Transformers

### 1. Basic Relationships

**Voltage relation:**
$$\frac{V_s}{V_p} = \frac{N_s}{N_p}$$

**Current relation (ideal transformer):**
$$\frac{I_s}{I_p} = \frac{N_p}{N_s} = \frac{V_p}{V_s}$$

**Power conservation:**
$$P_p = P_s \quad \text{(ideal)}$$
$$V_p I_p = V_s I_s$$

### 2. Transformer Types

**Step-up transformer:**
- $N_s > N_p$
- $V_s > V_p$
- $I_s < I_p$

**Step-down transformer:**
- $N_s < N_p$
- $V_s < V_p$
- $I_s > I_p$

---

## Problem-Solving Strategies

### 1. Magnetic Force Problems

1. **Identify the system:** moving charge, current-carrying wire, or current loop
2. **Determine geometry:** angles between vectors
3. **Apply appropriate formula:** $F = qvB\sin\phi$ or $F = ILB\sin\theta$
4. **Use right-hand rule:** for direction (if needed)
5. **Check units:** force should be in Newtons

### 2. Magnetic Field Problems

1. **Identify source:** straight wire, loop, or solenoid
2. **Determine distance/position:** where field is calculated
3. **Apply appropriate formula:**
   - Wire: $B = \frac{\mu_0 I}{2\pi r}$
   - Loop center: $B = \frac{\mu_0 I}{2R}$
   - Solenoid: $B = \mu_0 nI$
4. **Check units:** field should be in Tesla

### 3. Induction Problems

1. **Calculate initial and final flux:** $\Phi = BA\cos\phi$
2. **Find change in flux:** $\Delta\Phi = \Phi_f - \Phi_i$
3. **Apply Faraday's law:** $\mathcal{E} = -N\frac{\Delta\Phi}{\Delta t}$
4. **Apply Lenz's law:** for current direction
5. **Check units:** EMF should be in Volts

### 4. Transformer Problems

1. **Identify given quantities:** voltages, currents, or turns
2. **Apply voltage relation:** $\frac{V_s}{V_p} = \frac{N_s}{N_p}$
3. **Apply current relation:** $\frac{I_s}{I_p} = \frac{N_p}{N_s}$
4. **Check power conservation:** $P_p = P_s$ (ideal)
5. **Verify units:** consistent voltage and current units

---

## Common Applications

### Magnetic Forces

- **Particle accelerators:** cyclotrons, synchrotrons
- **Mass spectrometers:** isotope separation
- **Electric motors:** torque on current loops
- **Magnetic levitation:** maglev trains

### Electromagnetic Induction

- **Electric generators:** rotating coils in magnetic fields
- **Transformers:** voltage conversion
- **Induction cooktops:** changing magnetic fields
- **Eddy current brakes:** induced current damping

### Solenoids and Electromagnets

- **MRI machines:** strong uniform fields
- **Relays and switches:** electromagnetic actuation
- **Speakers:** voice coils in magnetic fields
- **Magnetic door locks:** electromagnetic holding force