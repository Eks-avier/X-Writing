# Light and Mirrors - Comprehensive Notes

## Early Theories on Light

- **Particle Theory** (Isaac Newton)
	- Light consists of particles called “corpuscles”
	- Explained reflection and some refraction phenomena
	- Struggled with interference and diffraction
- **Wave Theory** (Christiaan Huygens)
	- Light is a wave phenomenon
	- Successfully explained interference, diffraction, and polarization
	- Huygens' Principle: Every point on a wavefront acts as a source of secondary wavelets
- **Electromagnetic Wave Theory** (James Clerk Maxwell)
	- Light is an electromagnetic wave with electric and magnetic field components
	- Speed of light: $c = 3.00 \times 10^8$ m/s in vacuum
	- Relationship: $c = f\lambda$ where $f$ is frequency and $\lambda$ is wavelength
- **Quantum Theory** (Max Planck, Albert Einstein)
	- Light travels in discrete energy packets called photons
	- Energy of a photon: $E = hf = \frac{hc}{\lambda}$ where $h = 6.626 \times 10^{-34}$ J·s
- **Wave-Particle Duality**: Light exhibits both wave and particle properties depending on the experimental setup

## Characteristics of Light

- Light travels in straight lines (rectilinear propagation)
- Light travels at finite speed ($c = 3.00 \times 10^8$ m/s in vacuum)
- Light exhibits:
	- **Reflection**: bouncing off surfaces
	- **Refraction**: bending when entering different media
	- **Interference**: wave superposition effects
	- **Diffraction**: bending around obstacles
	- **Polarization**: orientation of electric field vector

## Reflection

### Types of Reflection

- **Specular Reflection**: Mirror-like reflection from smooth surfaces
	- Follows laws of reflection precisely
	- Produces clear, well-defined images
- **Diffuse Reflection**: Scattering from rough surfaces
	- Each ray follows laws of reflection locally
	- No clear image formation due to surface irregularities

### Laws of Reflection

1. The incident ray, reflected ray, and normal to the surface all lie in the same plane
2. The angle of incidence equals the angle of reflection: $\theta_i = \theta_r$

*These laws apply to ALL reflecting surfaces, regardless of shape.*

## Mirror Types and Equations

### Sign Conventions (Essential for Problem Solving)

**For mirrors, using the convention where light travels from left to right:**

- **Object distance** ($d_o$): Always positive for real objects
- **Image distance** ($d_i$):
	- Positive for real images (in front of mirror)
	- Negative for virtual images (behind mirror)
- **Focal length** ($f$):
	- Positive for concave mirrors
	- Negative for convex mirrors
- **Radius of curvature** ($R$):
	- Positive for concave mirrors (center of curvature in front)
	- Negative for convex mirrors (center of curvature behind)

### Relationship Between Focal Length and Radius

**Concave Mirror:**
$$f = \frac{R}{2} \quad \text{(both positive)}$$

**Convex Mirror:**
$$f = -\frac{R}{2} \quad \text{(both negative)}$$

*Physical meaning: The focal point is halfway between the mirror surface and center of curvature.*

### Mirror Equation (Gaussian Form)

$$\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}$$

*This equation works for both concave and convex mirrors when proper sign conventions are used.*

### Magnification Equations

**Linear Magnification:**
$$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}$$

**Interpretation of Magnification:**
- $|m| > 1$: Image is larger than object (magnified)
- $|m| < 1$: Image is smaller than object (diminished)
- $|m| = 1$: Image is same size as object
- $m > 0$: Image is upright (virtual)
- $m < 0$: Image is inverted (real)

## Image Characteristics by Mirror Type

### Plane Mirrors

- **Always produces**: Virtual, upright, same size, laterally reversed
- Image distance equals object distance: $d_i = -d_o$
- Magnification: $m = +1$

### Concave Mirrors (Converging)

**Object beyond center of curvature** ($d_o > R$):
- Real, inverted, diminished image
- $0 < d_i < R$, $m < 0$, $|m| < 1$

**Object at center of curvature** ($d_o = R$):
- Real, inverted, same size image
- $d_i = R$, $m = -1$

**Object between center and focal point** ($f < d_o < R$):
- Real, inverted, magnified image
- $d_i > R$, $m < 0$, $|m| > 1$

**Object at focal point** ($d_o = f$):
- No image formed (rays parallel after reflection)
- $d_i = \infty$

**Object inside focal length** ($d_o < f$):
- Virtual, upright, magnified image
- $d_i < 0$, $m > 0$, $|m| > 1$

### Convex Mirrors (Diverging)

**All object positions**:
- Always virtual, upright, diminished
- $d_i < 0$, $m > 0$, $|m| < 1$
- Used in security mirrors and car side mirrors for wide field of view

## Ray Tracing Rules

### For Concave Mirrors:

1. Ray parallel to principal axis reflects through focal point
2. Ray through focal point reflects parallel to principal axis
3. Ray through center of curvature reflects back on itself
4. Ray hitting vertex reflects with equal angles to principal axis

### For Convex Mirrors:

1. Ray parallel to principal axis reflects as if coming from focal point
2. Ray directed toward focal point reflects parallel to principal axis
3. Ray directed toward center of curvature reflects back on itself

## Problem-Solving Strategy

1. **Identify knowns**: Object distance, mirror type, focal length/radius
2. **Choose sign convention**: Apply consistently throughout problem
3. **Apply mirror equation**: Solve for unknown distances
4. **Calculate magnification**: Determine image characteristics
5. **Verify results**: Check signs and physical reasonableness
6. **Draw ray diagram**: Confirm analytical results geometrically

## Common Applications

- **Concave mirrors**: Telescopes, satellite dishes, makeup mirrors, headlights
- **Convex mirrors**: Security mirrors, car side mirrors, wide-angle surveillance
- **Plane mirrors**: Bathroom mirrors, periscopes, optical instruments

---

# Refraction and Lenses

## Refraction Fundamentals

### Index of Refraction

The index of refraction quantifies how much light slows down in a medium:
$n = \frac{c}{v}$
where $c$ is speed of light in vacuum and $v$ is speed in the medium.

**Common indices:**
- Air: $n \approx 1.00$
- Water: $n = 1.33$
- Glass: $n \approx 1.5$
- Diamond: $n = 2.42$

### Snell's Law

When light passes from one medium to another:
$n_1 \sin \theta_1 = n_2 \sin \theta_2$

where:
- $n_1, n_2$ are indices of refraction
- $\theta_1$ is angle of incidence (measured from normal)
- $\theta_2$ is angle of refraction (measured from normal)

**Key behaviors:**
- Light bends **toward** normal when entering denser medium ($n_2 > n_1$)
- Light bends **away** from normal when entering less dense medium ($n_2 < n_1$)

## Total Internal Reflection

### Critical Angle

When light travels from denser to less dense medium, total internal reflection occurs when:
$\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right)$

**Applications:**
- Optical fibers
- Prisms in binoculars
- Diamond brilliance

## Lenses

### Types of Lenses

**Converging Lenses (Convex)**:
- Thicker in center than edges
- Focal length is positive: $f > 0$
- Converge parallel rays to a focal point

**Diverging Lenses (Concave)**:
- Thinner in center than edges
- Focal length is negative: $f < 0$
- Diverge parallel rays as if from a focal point

## Thin Lens Equation

The same form as the mirror equation:
$\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}$

### Sign Conventions for Lenses

**From your classroom slide - these are crucial!**

**Focal Length:**
- $f$ is **positive** for a **converging lens**
- $f$ is **negative** for a **diverging lens**

**Object Distance:**
- $d_o$ is **positive** if object is to the **left** of lens
- $d_o$ is **negative** if object is to the **right** of lens

**Image Distance:**
- $d_i$ is **positive** for image formed to **right** of lens (**real image**)
- $d_i$ is **negative** for image formed to **left** of lens (**virtual image**)

**Magnification:**
- $m$ is **positive** for **upright** image
- $m$ is **negative** for **inverted** image

### Lens Magnification

Same equations as mirrors:
$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}$

## Image Formation by Lenses

### Converging Lenses ($f > 0$)

**Object beyond 2f** ($d_o > 2f$):
- Real, inverted, diminished
- $f < d_i < 2f$, $m < 0$, $|m| < 1$

**Object at 2f** ($d_o = 2f$):
- Real, inverted, same size
- $d_i = 2f$, $m = -1$

**Object between f and 2f** ($f < d_o < 2f$):
- Real, inverted, magnified
- $d_i > 2f$, $m < 0$, $|m| > 1$

**Object at focal point** ($d_o = f$):
- No image (parallel rays emerge)
- $d_i = \infty$

**Object inside focal length** ($d_o < f$):
- Virtual, upright, magnified
- $d_i < 0$, $m > 0$, $|m| > 1$

### Diverging Lenses ($f < 0$)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
**All object positions**:
- Always virtual, upright, diminished
- $d_i < 0$, $m > 0$, $|m| < 1$

## Ray Tracing for Lenses

### Converging Lens Rules:

1. Ray parallel to axis refracts through far focal point
2. Ray through near focal point emerges parallel to axis
3. Ray through center passes straight through (undeviated)

### Diverging Lens Rules:

1. Ray parallel to axis refracts as if from near focal point
2. Ray toward far focal point emerges parallel to axis
3. Ray through center passes straight through

## Lens Vs Mirror Comparison

| Property | Mirrors | Lenses |
|----------|---------|---------|
| Fundamental Equation | $\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}$ | $\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}$ |
| Physical Process | Reflection | Refraction |
| Real Image Location | In front of mirror | Behind lens |
| Virtual Image Location | Behind mirror | In front of lens |
| Sign Convention Basis | Light direction | Light direction |

## Applications

**Converging Lenses:**
- Camera lenses
- Magnifying glasses
- Telescope objectives
- Human eye lens

**Diverging Lenses:**
- Correcting nearsightedness
- Peepholes in doors
- Wide-angle camera lenses
- Beam expanders

**Total Internal Reflection:**
- Fiber optic communications
- Medical endoscopes
- Automotive light guides
- Optical sensors

---

# Pairs of Lenses and Multi-Lens Systems

## Fundamental Principle

In a multi-lens system, **the image formed by the first lens becomes the object for the second lens**. This sequential approach allows us to analyze complex optical systems step by step.

## Sequential Analysis Method

### Step-by-Step Protocol:

1. **Analyze First Lens**:
   - Apply thin lens equation: $\frac{1}{d_{o1}} + \frac{1}{d_{i1}} = \frac{1}{f_1}$
   - Calculate image distance $d_{i1}$ and magnification $m_1$

2. **Transition to Second Lens**:
   - The image from lens 1 becomes the object for lens 2
   - **Key relationship**: $d_{o2} = D - d_{i1}$
   - Where $D$ = separation distance between lenses

3. **Analyze Second Lens**:
   - Apply thin lens equation: $\frac{1}{d_{o2}} + \frac{1}{d_{i2}} = \frac{1}{f_2}$
   - Calculate final image distance $d_{i2}$ and magnification $m_2$

4. **Calculate Overall Properties**:
   - **Total magnification**: $M_{total} = m_1 \times m_2$
   - **Final image characteristics**: Combine orientations and sizes

## Critical Sign Convention Rules

### Object Distance for Second Lens ($d_{o2}$):

**Case 1: Image 1 would form to the right of Lens 2**
- $d_{i1} > D$ (image distance from lens 1 exceeds separation)
- $d_{o2} = D - d_{i1} < 0$ (**negative**)
- Physical meaning: Object for lens 2 is **virtual** (to the right of lens 2)

**Case 2: Image 1 forms between the lenses**
- $d_{i1} < D$ (image distance from lens 1 less than separation)
- $d_{o2} = D - d_{i1} > 0$ (**positive**)
- Physical meaning: Object for lens 2 is **real** (to the left of lens 2)

**Case 3: Image 1 forms to the left of Lens 1**
- $d_{i1} < 0$ (virtual image from lens 1)
- $d_{o2} = D - d_{i1} = D + |d_{i1}| > 0$ (**positive**)
- Physical meaning: Virtual image from lens 1 acts as real object for lens 2

## Overall System Properties

### Total Magnification

$M_{total} = m_1 \times m_2 = \frac{h_{final}}{h_{original}}$

**Sign interpretation:**
- $M_{total} > 0$: Final image is upright relative to original object
- $M_{total} < 0$: Final image is inverted relative to original object
- $|M_{total}| > 1$: Final image is magnified
- $|M_{total}| < 1$: Final image is diminished

### Equivalent Focal Length

For thin lenses separated by distance $D$:
$\frac{1}{f_{eq}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{D}{f_1 f_2}$

**Special case**: When lenses are in contact ($D = 0$):
$\frac{1}{f_{eq}} = \frac{1}{f_1} + \frac{1}{f_2}$

## Common Lens Pair Configurations

### 1. **Telescope (Astronomical)**

- **Purpose**: Magnify distant objects
- **Configuration**: Two converging lenses
- **Objective lens**: Large $f_1$, collects light
- **Eyepiece**: Small $f_2$, provides magnification
- **Angular magnification**: $M_\theta = \frac{f_1}{f_2}$

### 2. **Microscope**

- **Purpose**: Magnify small, nearby objects
- **Configuration**: Two converging lenses
- **Objective**: Short $f_1$, high magnification
- **Eyepiece**: Longer $f_2$, comfortable viewing
- **Total magnification**: $M = M_{obj} \times M_{eye}$

### 3. **Galilean Telescope**

- **Configuration**: Converging + diverging lens
- **Advantage**: Shorter, upright images
- **Disadvantage**: Limited field of view

### 4. **Beam Expander**

- **Purpose**: Increase beam diameter
- **Configuration**: Usually diverging + converging
- **Applications**: Laser systems, telescopes

## Problem-Solving Strategy for Lens Pairs

### Systematic Approach:

1. **Draw the system**: Show both lenses, separation distance, initial object
2. **Identify given information**: Object distance, lens focal lengths, separation
3. **Apply first lens**: Calculate $d_{i1}$ and $m_1$
4. **Determine $d_{o2}$**: Use $d_{o2} = D - d_{i1}$ with careful attention to signs
5. **Apply second lens**: Calculate $d_{i2}$ and $m_2$
6. **Find total magnification**: $M_{total} = m_1 \times m_2$
7. **Verify results**: Check signs for physical reasonableness

### Common Pitfalls to Avoid:

❌ **Treating lenses independently** - Must use sequential approach
❌ **Sign errors in $d_{o2}$** - Carefully apply $d_{o2} = D - d_{i1}$
❌ **Forgetting magnification multiplication** - Total mag = $m_1 \times m_2$
❌ **Mixing up final image location** - Always measured from the last lens

## Ray Tracing for Lens Pairs

### Key Rays to Trace:

1. **Ray parallel to axis**:
   - Through lens 1, bends toward focal point
   - Continues to lens 2 as determined by lens 1's refraction

2. **Ray through focal point of lens 1**:
   - Emerges parallel from lens 1
   - Enters lens 2 parallel to axis

3. **Ray through center of lens 1**:
   - Passes straight through lens 1
   - Hits lens 2 at some angle, follows lens 2's rules

## Practical Applications

### **Photography**:

- Camera lenses often use multiple elements
- Each element corrects specific aberrations
- Overall system optimizes image quality

### **Vision Correction**:

- Eye + corrective lens system
- Contact lens + glasses combination
- Bifocal and progressive lenses

### **Scientific Instruments**:

- Compound microscopes
- Telescopes (refracting and catadioptric)
- Spectrometers and interferometers

### **Laser Systems**:

- Beam shaping and conditioning
- Focusing systems
- Beam expansion for uniform illumination