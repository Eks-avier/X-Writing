# Light and Mirrors - Comprehensive Notes

## Early Theories on Light

- **Particle Theory** (Isaac Newton)
	- Light consists of particles called "corpuscles"
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

## Fundamentals of Refraction

**Refraction** is the bending of light when it passes from one medium to another with different optical densities.

### Key Terminology

- **Index of Refraction** ($n$): Measure of how much light slows down in a medium
  $n = \frac{c}{v}$
  where $c$ = speed of light in vacuum, $v$ = speed of light in medium

- **Common Indices of Refraction** (at λ = 589 nm):
  - Vacuum: $n = 1.000$ (exactly)
  - Air: $n = 1.000$ (approximately)
  - Water: $n = 1.333$
  - Glass (crown): $n = 1.52$
  - Diamond: $n = 2.42$

### Snell's Law

$n_1 \sin \theta_1 = n_2 \sin \theta_2$

where:
- $n_1$, $n_2$ = indices of refraction of media 1 and 2
- $\theta_1$ = angle of incidence (measured from normal)
- $\theta_2$ = angle of refraction (measured from normal)

**Physical Meaning**: The product of index and sine of angle remains constant across the boundary.

### Refraction Behavior

**When light enters a denser medium** ($n_2 > n_1$):
- Light bends **toward** the normal
- $\theta_2 < \theta_1$
- Light slows down

**When light enters a less dense medium** ($n_1 > n_2$):
- Light bends **away from** the normal  
- $\theta_2 > \theta_1$
- Light speeds up

## Total Internal Reflection

### Critical Angle

When light travels from a denser to less dense medium, there exists a **critical angle** $\theta_c$ where the refracted ray grazes along the boundary ($\theta_2 = 90°$).

$\sin \theta_c = \frac{n_2}{n_1} \quad \text{(where } n_1 > n_2\text{)}$

**For angles greater than critical angle** ($\theta_1 > \theta_c$):
- **Total Internal Reflection** occurs
- No light passes into the second medium
- All light is reflected back into the first medium

### Applications of Total Internal Reflection

- **Optical fibers**: Light guidance in telecommunications
- **Prisms**: Light direction in optical instruments  
- **Diamonds**: Brilliance due to high refractive index
- **Mirages**: Atmospheric refraction effects

## Thin Lenses

### Lens Types

**Converging Lenses (Convex)**:
- Thicker at center than edges
- Focal length is positive ($f > 0$)
- Parallel rays converge to focal point

**Diverging Lenses (Concave)**:
- Thinner at center than edges  
- Focal length is negative ($f < 0$)
- Parallel rays appear to diverge from focal point

### Lens Sign Conventions

**For lenses, using the convention where light travels from left to right:**

- **Object distance** ($d_o$): Positive for real objects (left of lens)
- **Image distance** ($d_i$): 
  - Positive for real images (right of lens)
  - Negative for virtual images (left of lens)
- **Focal length** ($f$):
  - Positive for converging lenses
  - Negative for diverging lenses
- **Heights**: Positive above optical axis, negative below

### Thin Lens Equation

$\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}$

*Same form as mirror equation, but different sign conventions!*

### Lens Magnification

$m = \frac{h_i}{h_o} = -\frac{d_i}{d_o}$

**Interpretation**:
- $|m| > 1$: Magnified image
- $|m| < 1$: Diminished image
- $m > 0$: Upright image (virtual)
- $m < 0$: Inverted image (real)

### Lens Power

$P = \frac{1}{f} \quad \text{(when } f \text{ is in meters)}$

**Units**: Diopters (D) = m⁻¹
- Converging lens: $P > 0$
- Diverging lens: $P < 0$

## Image Formation by Lenses

### Converging Lenses

**Object beyond 2F** ($d_o > 2f$):
- Real, inverted, diminished
- $f < d_i < 2f$

**Object at 2F** ($d_o = 2f$):
- Real, inverted, same size
- $d_i = 2f$, $m = -1$

**Object between F and 2F** ($f < d_o < 2f$):
- Real, inverted, magnified
- $d_i > 2f$

**Object at focal point** ($d_o = f$):
- No image (parallel rays exit)
- $d_i = \infty$

**Object inside focal length** ($d_o < f$):
- Virtual, upright, magnified
- $d_i < 0$, acts as magnifying glass

### Diverging Lenses

**All object positions**:
- Always virtual, upright, diminished
- Image always between lens and focal point
- $d_i < 0$, $0 < |m| < 1$

## Ray Tracing for Lenses

### Converging Lens Rules:
1. Ray parallel to axis passes through focal point
2. Ray through focal point emerges parallel to axis
3. Ray through optical center passes straight through

### Diverging Lens Rules:
1. Ray parallel to axis appears to come from focal point
2. Ray toward focal point emerges parallel to axis  
3. Ray through optical center passes straight through

## Problem-Solving Strategy for Refraction

### For Snell's Law Problems:
1. **Identify the media** and their indices of refraction
2. **Measure angles from the normal** (not from surface)
3. **Apply Snell's Law**: $n_1 \sin \theta_1 = n_2 \sin \theta_2$
4. **Check for total internal reflection** if going from dense to less dense medium

### For Lens Problems:
1. **Identify lens type** and determine sign of focal length
2. **Apply sign conventions** consistently
3. **Use thin lens equation** to find unknown distances
4. **Calculate magnification** for image characteristics
5. **Verify physical reasonableness** of results

## The Lensmaker's Equation

For understanding how lens shape affects focal length:

$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$

where:
- $n$ = refractive index of lens material
- $R_1$, $R_2$ = radii of curvature of lens surfaces

## Practical Applications

### Refraction Applications:
- **Eyeglasses**: Correcting vision defects
- **Cameras**: Focusing light onto sensors
- **Telescopes**: Magnifying distant objects
- **Microscopes**: Magnifying small objects
- **Fiber optics**: High-speed data transmission

### Lens Combinations:
- **Compound microscopes**: Objective + eyepiece
- **Telescopes**: Various lens arrangements
- **Camera systems**: Multiple lens elements for image quality