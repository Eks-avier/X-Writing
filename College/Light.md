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
$$
n_1 \sin \theta_1 = n_2 \sin \theta_2
$$
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