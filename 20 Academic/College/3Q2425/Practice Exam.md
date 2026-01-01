# COMPREHENSIVE PHYSICS PRACTICE EXAM

## PHYS102 - Electricity, Magnetism, and Optics

**Instructions:** Solve all problems completely, showing all work including equations used, substitutions made, and final answers with correct units. Round final answers to 2 decimal places unless otherwise specified.

**Total Points:** 100 points
**Time Limit:** 3 hours

---

## SECTION I: ELECTROSTATICS & CIRCUITS (40 points)

### Problem 1: Electrostatic Forces (12 points)

Four point charges are arranged at the corners of a rectangle. The rectangle has dimensions of 4.0 m by 3.0 m. Place charges as follows:
- $q_1 = +15.0 \, \mu\text{C}$ at the origin (0, 0)
- $q_2 = -8.0 \, \mu\text{C}$ at (4.0 m, 0)
- $q_3 = +12.0 \, \mu\text{C}$ at (4.0 m, 3.0 m)
- $q_4 = -6.0 \, \mu\text{C}$ at (0, 3.0 m)

**Find:** The magnitude and direction of the net electrostatic force on $q_3$.

**Equation:** Coulomb's Law: $F = k\frac{|q_1||q_2|}{r^2}$ where $k = 8.99 \times 10^9 \, \text{N·m}^2/\text{C}^2$

### Problem 2: Electric Potential and Capacitance (14 points)

A parallel-plate capacitor has circular plates with radius $R = 5.0 \, \text{cm}$ separated by a distance $d = 2.5 \, \text{mm}$. The capacitor is connected to a $12.0 \, \text{V}$ battery.

**Find:**
1. The capacitance of the capacitor
2. The charge stored on each plate
3. The electric field magnitude between the plates
4. The energy stored in the capacitor

**Equations:**
- $C = \epsilon_0 \frac{A}{d}$ where $\epsilon_0 = 8.85 \times 10^{-12} \, \text{C}^2/(\text{N·m}^2)$
- $Q = CV$, $E = \frac{V}{d}$, $U = \frac{1}{2}CV^2$

### Problem 3: Multi-Loop Circuit Analysis Using Kirchhoff's Laws (14 points)

In the circuit shown below, use Kirchhoff's Laws to analyze the following multi-loop circuit:

```
        R₁ = 6Ω     A     R₂ = 8Ω
    +---/\/\/\------+------/\/\/\---+
    |               |               |
    |               |               |
 V₁ = 20V       R₃ = 4Ω         V₂ = 12V
    |               |               |
    |               |               |
    +---------------+---------------+
                    B
```

**Find:**
1. Write the junction equation at point A using KCL
2. Write the loop equations for both loops using KVL (assume clockwise current directions)
3. Solve for the current through each resistor
4. Determine which end of $R_3$ is at higher potential

**Equations:**
- Kirchhoff's Current Law (KCL): $\sum I_{in} = \sum I_{out}$ at any junction
- Kirchhoff's Voltage Law (KVL): $\sum V = 0$ around any closed loop
- Ohm's Law: $V = IR$

---

## SECTION II: ELECTROMAGNETISM (30 points)

### Problem 4: Magnetic Field from Current Loops (10 points)

Two concentric circular loops carry currents in opposite directions. The inner loop has radius $R_1 = 0.15 \, \text{m}$ and carries current $I_1 = 2.5 \, \text{A}$ clockwise (when viewed from above). The outer loop has radius $R_2 = 0.30 \, \text{m}$ and carries current $I_2 = 4.0 \, \text{A}$ counterclockwise.

**Find:** The magnitude and direction of the net magnetic field at the center of the loops.

**Equation:** $B = \frac{\mu_0 I}{2R}$ where $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$

### Problem 5: Electromagnetic Induction (10 points)

A rectangular coil with dimensions $25 \, \text{cm} \times 40 \, \text{cm}$ consists of 180 turns of wire. The coil is placed in a magnetic field that is perpendicular to its plane. The magnetic field changes uniformly from $0.20 \, \text{T}$ to $1.60 \, \text{T}$ in a time interval of $0.75 \, \text{s}$.

**Find:**
1. The average induced EMF in the coil
2. If the coil has a total resistance of $8.5 \, \Omega$, what is the induced current?

**Equations:**
- Faraday's Law: $\mathcal{E} = -N\frac{\Delta\Phi_B}{\Delta t} = -N\frac{\Delta(BA)}{\Delta t}$
- Ohm's Law: $I = \frac{\mathcal{E}}{R}$

### Problem 6: Transformer and Magnetic Force (10 points)

**Part A:** A transformer has 80 turns in its primary coil and 320 turns in its secondary coil. If the primary voltage is $110 \, \text{V}$ and the primary current is $5.0 \, \text{A}$:
1. Find the secondary voltage and current
2. Determine if this is a step-up or step-down transformer

**Part B:** A charged particle with charge $q = +3.2 \times 10^{-19} \, \text{C}$ moves with velocity $\vec{v} = 2.5 \times 10^6 \, \text{m/s}$ eastward through a magnetic field $\vec{B} = 0.40 \, \text{T}$ pointing northward. Find the magnitude and direction of the magnetic force.

**Equations:**
- Transformer: $\frac{V_s}{V_p} = \frac{N_s}{N_p}$, $V_p I_p = V_s I_s$
- Magnetic Force: $\vec{F} = q\vec{v} \times \vec{B}$

---

## SECTION III: LIGHT AND OPTICS (30 points)

### Problem 7: Refraction and Snell's Law (10 points)

A beam of light traveling in air strikes the surface of a transparent material at an angle of incidence of $55.0°$. The angle of refraction is $35.0°$.

**Find:**
1. The index of refraction of the material
2. The speed of light in this material
3. The critical angle for total internal reflection when light travels from this material back to air

**Equations:**
- Snell's Law: $n_1 \sin\theta_1 = n_2 \sin\theta_2$
- $v = \frac{c}{n}$ where $c = 3.00 \times 10^8 \, \text{m/s}$
- Critical angle: $\sin\theta_c = \frac{n_2}{n_1}$

### Problem 8: Concave Mirror Optics (10 points)

A concave makeup mirror has a focal length of $35.0 \, \text{cm}$. An object (your face) is placed $25.0 \, \text{cm}$ in front of the mirror.

**Find:**
1. The image distance
2. The magnification
3. Describe the characteristics of the image (real/virtual, upright/inverted, enlarged/reduced)

**Equations:**
- Mirror equation: $\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$
- Magnification: $m = -\frac{d_i}{d_o} = \frac{h_i}{h_o}$

### Problem 9: Compound Microscope (10 points)

A compound microscope has an objective lens with focal length $f_o = 12.0 \, \text{mm}$ and an eyepiece with focal length $f_e = 20.0 \, \text{mm}$. The distance between the lenses is $L = 180.0 \, \text{mm}$. An object is placed $15.0 \, \text{mm}$ from the objective lens.

**Find:**
1. The image distance from the objective lens
2. The magnification of the objective lens
3. The image distance from the eyepiece
4. The total magnification of the microscope

**Equations:**
- Lens equation: $\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$
- Total magnification: $M_{total} = M_o \times M_e$

---

## SECTION IV: ADDITIONAL PROBLEMS (Bonus - 5 points)

### Problem 10: RC Circuit Time Constant

A camera flash uses a $220 \, \mu\text{F}$ capacitor that charges through a resistor. The charging circuit has a time constant of $4.5 \, \text{s}$.

**Find:**
1. The resistance value
2. How long it takes for the capacitor to reach 90% of its maximum charge
3. If the initial charging current is $15 \, \text{mA}$, what current flows after $10 \, \text{s}$?

**Equations:**
- $\tau = RC$
- $q(t) = q_{max}(1 - e^{-t/\tau})$
- $i(t) = i_0 e^{-t/\tau}$

---

## CONSTANTS FOR REFERENCE

- $k = 8.99 \times 10^9 \, \text{N·m}^2/\text{C}^2$ (Coulomb's constant)
- $\epsilon_0 = 8.85 \times 10^{-12} \, \text{C}^2/(\text{N·m}^2)$ (Permittivity of free space)
- $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$ (Permeability of free space)
- $c = 3.00 \times 10^8 \, \text{m/s}$ (Speed of light in vacuum)
- $e = 1.60 \times 10^{-19} \, \text{C}$ (Elementary charge)

---

**End of Exam**

Good luck with your preparation! Remember to:
1. **Identify knowns and unknowns** clearly
2. **Choose appropriate equations** for each physical situation
3. **Show all algebraic steps** in your calculations
4. **Check units** and verify your answers make physical sense
5. **Draw diagrams** when helpful for visualization