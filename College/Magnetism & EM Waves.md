# Magnetism & EM Waves

## 1. Fundamentals of Magnetism

### Magnetic Fields and Field Lines

**Magnetic Field Properties:**

- Magnetic fields are vector quantities with both magnitude and direction
- Unit: **Tesla (T)** where $1\text{ T} = \frac{\text{N·s}}{\text{C·m}} = \frac{\text{N}}{\text{A·m}}$
- Magnetic field lines help visualize the magnetic field around magnets
- **Important**: Magnetic field lines are **NOT** lines of force since the force on a charged particle is not along the direction of a field line

**Field Line Characteristics:**

- At each point, the field line is tangent to the magnetic field vector $\vec{B}$
- The more densely packed the field lines, the stronger the field at that point
- Field lines point **away** from N poles and **toward** S poles
- Magnetic field lines form closed loops (unlike electric field lines)
- Field lines never cross each other

**Magnetic Poles:**

- Forces between magnetic poles are similar to forces between electric charges
- **Like poles repel, unlike poles attract**
- Magnetic poles always come in pairs (no magnetic monopoles)

---

## 2. Magnetic Force on Moving Charges

### Force Magnitude

**Primary Formula:** $$F = |q|vB\sin\phi$$

Where:

- $q$ = electric charge (C)
- $v$ = velocity of the charge (m/s)
- $B$ = magnetic field strength (T)
- $\phi$ = angle between $\vec{v}$ and $\vec{B}$

**Key Points:**

- Maximum force occurs when $\phi = 90°$ (velocity perpendicular to field)
- No force when $\phi = 0°$ or $180°$ (velocity parallel/antiparallel to field)
- Force is always perpendicular to both $\vec{v}$ and $\vec{B}$

### Force Direction - Right-Hand Rules

**Right-Hand Rule #1 (For moving charges):**

1. Extend the right hand
2. Point fingers in direction of magnetic field $\vec{B}$
3. Point thumb in direction of velocity $\vec{v}$ (for positive charge)
4. Palm faces in direction of magnetic force $\vec{F}$
5. **For negative charges**: Force direction is opposite to palm

**Vector Form:** $$\vec{F} = q\vec{v} \times \vec{B}$$

### Circular Motion in Uniform Magnetic Fields

**Key Concepts:**

- A charged particle in a magnetic field always moves with **constant speed**
- Magnetic force is always perpendicular to velocity → does no work
- Since $W = \vec{F} \cdot \vec{d} = 0$, kinetic energy remains constant
- For perpendicular entry: particle follows circular path

**Radius of Circular Path:** $$R = \frac{mv}{|q|B}$$

**Derivation:**

- Centripetal force equals magnetic force: $F_c = F_B$
- $\frac{mv^2}{R} = |q|vB$
- Solving for R: $R = \frac{mv}{|q|B}$

**Period of Circular Motion:** $$T = \frac{2\pi R}{v} = \frac{2\pi m}{|q|B}$$

**Frequency:** $$f = \frac{1}{T} = \frac{|q|B}{2\pi m}$$

**Applications:**

- **Cyclotron**: Particle accelerator using circular motion
- **Mass spectrometer**: Separates particles by mass-to-charge ratio
- **Cosmic ray deflection**: Earth's magnetic field deflects charged particles

---

## 3. Magnetic Force on Current-Carrying Wires

### Force on a Straight Wire

**Formula:** $$F = ILB\sin\theta$$

Where:

- $I$ = current through the wire (A)
- $L$ = length of the wire in the magnetic field (m)
- $B$ = magnetic field strength (T)
- $\theta$ = angle between current direction and $\vec{B}$

**Derivation from Particle Force:**

- Current $I = \frac{\Delta q}{\Delta t}$
- For moving charges in wire: $F = qvB\sin\theta$
- For wire: $F = \left(\frac{\Delta q}{\Delta t}\right)(v\Delta t)B\sin\theta = ILB\sin\theta$

**Direction:** Use Right-Hand Rule #1 with current direction as “velocity”

### Torque on Current-Carrying Loops

**Torque on a Coil:** $$\tau = NIAB\sin\phi$$

Where:

- $N$ = number of turns/loops in the coil
- $I$ = current (A)
- $A$ = area of the loop (m²)
- $B$ = magnetic field strength (T)
- $\phi$ = angle between magnetic field and normal to the loop

**Magnetic Moment:** $$\mu = NIA$$

**Alternative Torque Expression:** $$\tau = \mu B\sin\phi$$

**Equilibrium Positions:**

- **Stable equilibrium**: $\phi = 0°$ (magnetic moment aligned with field)
- **Unstable equilibrium**: $\phi = 180°$ (magnetic moment opposite to field)

**Applications:**

- Electric motors
- Galvanometers
- Compass needles

---

## 4. Magnetic Fields Produced by Currents

### Straight Wire

**Formula:** $$B = \frac{\mu_0 I}{2\pi r}$$

Where:

- $\mu_0 = 4\pi \times 10^{-7}\text{ T·m/A}$ (permeability of free space)
- $I$ = current (A)
- $r$ = distance from wire (m)

**Right-Hand Rule #2 (For field direction):**

1. Curl fingers of right hand into half-circle shape
2. Point thumb in direction of conventional current
3. Fingertips point in direction of magnetic field

### Circular Loop at Center

**Formula:** $$B = \frac{N\mu_0 I}{2R}$$

Where:

- $N$ = number of turns
- $R$ = radius of the loop (m)

**Field Direction:** Right-hand rule with thumb pointing through center of loop

### Solenoid (Long Coil)

**Inside a Solenoid:** $$B = \mu_0 nI$$

Where:

- $n = \frac{N}{l}$ = turns per unit length (turns/m)
- $N$ = total number of turns
- $l$ = length of solenoid (m)

**Alternative Form:** $$B = \frac{\mu_0 IN}{l}$$

**Key Properties:**

- Field inside is uniform and parallel to axis
- Field outside is negligible for long solenoids
- Field strength independent of solenoid diameter
- Direction determined by right-hand rule

### Force Between Parallel Wires

**Force per unit length:** $$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

Where:

- $I_1, I_2$ = currents in the two wires
- $d$ = separation distance between wires

**Force Direction:**

- **Parallel currents**: Attractive force
- **Antiparallel currents**: Repulsive force

**Applications:**

- Definition of the Ampere
- Power transmission line interactions

---

## 5. Electromagnetic Induction

### Magnetic Flux

**Definition:** $$\Phi_B = BA\cos\phi$$

Where:

- $\phi$ = angle between $\vec{B}$ and normal to surface
- **Unit**: Weber (Wb) where $1\text{ Wb} = 1\text{ T·m}^2$

**Maximum flux**: $\phi = 0°$ (field perpendicular to surface) 
**Zero flux**: $\phi = 90°$ (field parallel to surface)

### Faraday's Law

**Mathematical Statement:** $$\mathcal{E} = -N\frac{\Delta\Phi_B}{\Delta t}$$

Where:

- $\mathcal{E}$ = induced EMF (V)
- $N$ = number of turns
- **Negative sign**: Indicates direction per Lenz's Law

**Ways to Change Flux:**

1. Change magnetic field strength $B$
2. Change area $A$ of the loop
3. Change orientation $\phi$ between field and loop
4. Move the loop in/out of the field

### Lenz's Law

**Statement:** “The induced current flows in such a direction that its magnetic field opposes the change that produced it.”

**Physical Meaning:**

- Nature opposes changes in magnetic flux
- Induced effects always work to maintain the status quo
- Conservation of energy principle in electromagnetic form

**Application Steps:**

1. Identify the change in magnetic flux
2. Determine what magnetic field would oppose this change
3. Use right-hand rule to find current direction that produces opposing field

### Mutual Inductance

**Primary-Secondary Coil System:** $$\mathcal{E}_s = -M\frac{\Delta I_p}{\Delta t}$$

Where:

- $M$ = mutual inductance (Henry, H)
- $\Delta I_p$ = change in primary coil current

**Unit**: $1\text{ H} = 1\text{ V·s/A}$

### Self-Inductance

**Self-Induced EMF:** $$\mathcal{E} = -L\frac{\Delta I}{\Delta t}$$

Where $L$ = self-inductance (H)

**Inductance Calculation:** $$L = \frac{N\Phi_B}{I}$$

**For a Solenoid:** $$L = \frac{\mu_0 N^2 A}{l}$$

### Energy Stored in Inductors

**Energy Formula:** $$U = \frac{1}{2}LI^2$$

**Units**: Joules (J)

### Transformers

**Voltage Relationship:** $$\frac{V_s}{V_p} = \frac{N_s}{N_p}$$

**Current Relationship (for ideal transformer):** $$\frac{I_s}{I_p} = \frac{N_p}{N_s} = \frac{V_p}{V_s}$$

**Power Conservation:** $$P_p = P_s \quad \text{(ideal transformer)}$$

**Types:**

- **Step-up**: $V_s > V_p$ (more secondary turns)
- **Step-down**: $V_s < V_p$ (fewer secondary turns)

---

## 6. Electromagnetic Waves

### Wave Nature and Properties

**Key Characteristics:**

- EM waves are oscillating electric and magnetic fields
- Fields are perpendicular to each other and to direction of propagation
- No medium required - can travel through vacuum
- All EM waves travel at speed of light in vacuum

**Fundamental Relationship:** $$c = f\lambda$$

Where:

- $c = 3.00 \times 10^8\text{ m/s}$ (speed of light in vacuum)
- $f$ = frequency (Hz)
- $\lambda$ = wavelength (m)

### Generation of EM Waves

**Source**: Any accelerating electric charge emits electromagnetic waves

**Examples:**

- Oscillating charges in radio antennas
- Electron transitions in atoms (visible light)
- Nuclear transitions (gamma rays)
- Thermal motion of charges (infrared)

### The Electromagnetic Spectrum

**From Low to High Frequency:**

1. **Radio Waves**
    
    - Frequency: $< 10^9$ Hz
    - Wavelength: $> 0.3$ m
    - Applications: AM/FM radio, TV, cell phones
2. **Microwaves**
    
    - Frequency: $10^9 - 10^{12}$ Hz
    - Wavelength: $0.3$ m - $0.3$ mm
    - Applications: Microwave ovens, radar, satellite communication
3. **Infrared (IR)**
    
    - Frequency: $10^{12} - 4 \times 10^{14}$ Hz
    - Wavelength: $0.3$ mm - $750$ nm
    - Applications: Heat lamps, night vision, remote controls
4. **Visible Light**
    
    - Frequency: $4 \times 10^{14} - 7.9 \times 10^{14}$ Hz
    - Wavelength: $750$ nm - $380$ nm
    - Colors: Red → Orange → Yellow → Green → Blue → Indigo → Violet
5. **Ultraviolet (UV)**
    
    - Frequency: $7.9 \times 10^{14} - 10^{17}$ Hz
    - Wavelength: $380$ nm - $3$ nm
    - Applications: Sterilization, fluorescent lighting, astronomy
6. **X-rays**
    
    - Frequency: $10^{17} - 10^{20}$ Hz
    - Wavelength: $3$ nm - $3$ pm
    - Applications: Medical imaging, crystallography
7. **Gamma Rays**
    
    - Frequency: $> 10^{20}$ Hz
    - Wavelength: $< 3$ pm
    - Applications: Cancer treatment, nuclear physics, astronomy

### Maxwell's Equations (Conceptual)

**Key Insight**: Maxwell's equations show that:

- A time-varying magnetic field creates an electric field
- A time-varying electric field creates a magnetic field
- This mutual creation propagates as electromagnetic waves

**Wave Speed in Vacuum:** $$c = \frac{1}{\sqrt{\mu_0\epsilon_0}}$$

Where $\epsilon_0$ is the permittivity of free space.

### Wave Properties

**Amplitude**: Determines intensity of the wave **Frequency**: Determines energy and color (for visible light) **Wavelength**: Inversely related to frequency **Polarization**: Orientation of electric field vector

### Energy and Intensity

**Energy of EM Wave**: Carried equally by electric and magnetic fields **Intensity**: Power per unit area (W/m²) **Poynting Vector**: Describes energy flow direction

---

## 7. Applications and Problem-Solving Strategies

### Common Applications

**Magnetic Force Applications:**

- Particle accelerators (cyclotrons, synchrotrons)
- Mass spectrometers
- MRI machines
- Electric motors and generators
- Magnetic levitation trains

**Electromagnetic Induction Applications:**

- Power generators
- Transformers
- Induction cooking
- Wireless charging
- Magnetic brakes

**EM Wave Applications:**

- Communication systems
- Medical imaging and treatment
- Astronomy and space exploration
- Remote sensing
- Optical fiber communication

### Problem-Solving Protocol

**For Magnetic Force Problems:**

1. Identify the charge, velocity, and magnetic field
2. Determine the angle between velocity and field
3. Calculate magnitude using $F = |q|vB\sin\phi$
4. Find direction using appropriate right-hand rule
5. For circular motion, use $R = \frac{mv}{|q|B}$

**For Electromagnetic Induction Problems:**

1. Identify what causes the flux change
2. Calculate initial and final flux values
3. Apply Faraday's law: $\mathcal{E} = -N\frac{\Delta\Phi_B}{\Delta t}$
4. Use Lenz's law to determine current direction
5. Apply Ohm's law if resistance is given

**For EM Wave Problems:**

1. Identify known quantities (frequency, wavelength, or speed)
2. Apply $c = f\lambda$ relationship
3. Use appropriate values for different media if needed
4. Consider energy relationships for intensity problems

### Key Constants to Remember

- Speed of light: $c = 3.00 \times 10^8\text{ m/s}$
- Permeability of free space: $\mu_0 = 4\pi \times 10^{-7}\text{ T·m/A}$
- Electron charge: $e = 1.60 \times 10^{-19}\text{ C}$
- Electron mass: $m_e = 9.11 \times 10^{-31}\text{ kg}$
- Proton mass: $m_p = 1.67 \times 10^{-27}\text{ kg}$

### Common Mistakes to Avoid

1. **Sign errors** in Lenz's law applications
2. **Angle confusion** in force calculations
3. **Unit inconsistencies** (always use SI units)
4. **Right-hand rule misapplication**
5. **Forgetting perpendicular motion requirement** for circular paths
6. **Confusing mutual vs. self-inductance**
7. **Speed of light variations** in different media
