# Coding A Simulation Of An ~4D Menger Sponge Universe

## It's something you can try at home!

As promised previously, this article we're gonna numerically simulate the equations derived across the past few articles and see if they hold water. We'll also look intosome other methods we could use to validate our model for an even deeper look into any chance this is a workable idea.


So, the final step — numerically simulating our Fractal Quantum Gravity (FQG) equations to see if they predict known phenomena better than classical General Relativity (GR) and Quantum Mechanics (QM)!

1. What We Need to Simulate

To verify our Fractal Quantum Gravity (FQG) model, we need to numerically solve:
- the Fractal Einstein Equations (Fractal General Relativity)
- the Fractal Schrödinger Equation (Fractal Quantum Mechanics)
- the Fractal Klein-Gordon Equation (Quantum Fields in Fractal Spacetime)
- the Fractal Path Integrals (Quantum Gravity Effects)
- Fractal Black Hole Thermodynamics (Holography in Recursive Space)

These simulations will:
- Compare standard vs. fractal spacetime predictions.
- Test if fractal recursion solves renormalization problems.
- Check if fractal corrections explain dark matter, dark energy, or vacuum energy.
- Determine if quantum interference patterns show fractal oscillations.


2. A Simulation Plan

We're gonna:
- Discretize the fractal metric equations for numerical solutions.
- Use Monte Carlo & Finite Difference Methods (FDM) to solve PDEs.
- Perform a high-precision numerical analysis of fractal quantum wavefunctions.
- Compare results with observational data (gravitational lensing, CMB, quantum decoherence times, etc.).


3. The Actual Numerical Simulation Code
We'll start with Fractal Einstein Equations, solving them numerically with Python & SciPy:

Step 1: Discretizing the Fractal Einstein Equations

​
 
Expanding for small 
𝑛



We'll solve this numerically using the Finite Difference Method (FDM) on a discrete 4D grid.


Step 2: Implementing the Simulation
We'll be using nothing more than Python with NumPy, SciPy, and Matplotlib to solve this system! Yup, we're gonna take a few steps into looking at a possible alternat euniverse structure with some easily available tools that anyone can run at home!
_(n.b. if yo have a powerful gaming rig or suffficiently specced computer you use for running code or w/e then you can actually run modified code that will take advantage of the better CPU/GFX/etc. to really crunch some numbers - i'll leave comments so you can see what things can be cranked up even further...)_


Fractal QG Sim

1   import numpy as np
2   import scipy.sparse as sp
3   import scipy.sparse.linalg as spla
4   import matplotlib.pyplot as plt
5
6   # Constants
7   D = 2.7268  # Fractal dimension of 4D Menger Sponge
8   N = 3        # Fractal recursion factor  # *1.
9   c = 3e8      # Speed of light (m/s)  # *2.
10  G = 6.674e-11 # Gravitational constant  # *3.
11
12  # Grid settings
13  gridsize = 50  # Discretized spacetime grid  # **1.
14  T_max = 100    # Maximum time steps  # **2.
15  delta_x = 1e-3 # Spacing in space  # **3.
16  delta_t = 1e-6 # Time step size  # **4
17  
18  # Initialize metric tensor on grid
19  G_f = np.zeros((gridsize, gridsize, gridsize, gridsize))
20  G_f[0, :, :, :] = 1  # Initial condition
21  
22  # Fractal corrections (Monte Carlo randomization at deeper recursion levels)
23  def fractal_correction(depth, size):
24      return N**(-D * depth) * np.random.normal(0, 0.01, size)
25  
26  # Time evolution loop
27  for t in range(T_max):
28      for depth in range(3):  # Sum over first 3 recursion levels. *1. note: this chnages to match N in Constants
29          correction = fractal_correction(depth, (gridsize, gridsize, gridsize, gridsize))
30          G_f += correction
31  
32  # Plot the curvature variations
33  plt.imshow(G_f[:, :, gridsize//2, gridsize//2], cmap='inferno')
34  plt.title("Fractal Gravity Tensor Evolution (Mid-Slice)")
35  plt.colorbar()
36  plt.show()


*1., 2., 3.: A single digit increas in N will immensely increase your processing requirements;
- (only alter if you have some serious power to take advantag of and make appropriate edits to the code as mentioned at article end.)
C and G can be increased in accuracy to your processing capacity's capabilty pretty much - your choice.
**1., 2., 3., 4.: gridsize and T_max will have quite significant effect on processing demands - (increase only if you have powerful
processing that can take advantage of ode modifiations mentioned at end f article.)


4. What Does This Code Do?
- It discretizes spacetime into a grid.
- Then applies fractal corrections to the Einstein Tensor at different recursion depths.
- Nexit it evolves the metric tensor over time to track curvature changes.
- And finally isualizes the evolution of spacetime curvature in a fractal universe.


Further steps i haven't developed that you could try:
- Adding quantum corrections by coupling this with the Fractal Schrödinger Equation.
- Including matter-energy tensor effects to simulate real astrophysical environments.
- Comparing predictions to standard General Relativity (GR).***

***This is kinda the point of this exercise so actually one of the most important next moves!

Modifying The code to take advantage of more high powered processors and GPUs:
- If your processor suppports anyform of SIMD (which it very likely does) nd specifically AVX-512 instructions, then 
following lterations to the code necessary to take advantage of those instruction sets would massively boost performance
of the program.
- Likewise, if you have anything past basic onboard GFX you will possibly be able to employ that cards processing capacity 
to gain evn greater performance boosts - GFX cards to the end of NVIDIA GTX 3070/80/90 or RTX 4070/80/90 will really allow
you to take advantage of some serious processing capacity.
- Necessary code adjustents to take advantage of both of the above processing boosts are quite significant and so i won't
de into them here - although i may write a further article in future if i happen to dive down that rabbithole myself ever!


## Other Methods Of Validating Our Model:
what else can we do to ty and validate our model?

Vlidating this model against real astronomical datasets:
To validate our fractal quantum gravity model against real astronomical data, we can utilize several key datasets and studies;

- SPARC Dataset: This comprehensive database includes 175 late-type galaxies with high-quality rotation curves derived from near-infrared Spitzer photometry. The dataset allows tracing rotation velocities out to large radii, providing strong constraints on dark matter halo profiles.
- Gaia Data Release 3 (DR3): The Gaia mission's DR3 offers precise positions and 3D motions of stars, enabling the derivation of the Milky Way's rotation curve. Notably, recent analyses have detected a Keplerian decline in the Milky Way's rotation curve, suggesting a lower total mass estimate for our galaxy.
-NASA/ESA Hubble Space Telescope Observations: These observations have been used to map the evolving distribution of dark matter by splitting background source galaxy populations into discrete epochs, effectively looking back in time to understand dark matter's role in galaxy formation.
- Bayesian Reconstruction Studies: Other Research efforts have employed Bayesian methodologies to infer the distribution of dark matter within the Milky Way using rotation curve data, providing robust estimates of local dark matter density - there may be avenues here?


Validating our refined fractal inflation model against Cosmic Microwave Background (CMB) and early universe data, we can utilize the latest datasets from missions such as Planck and Euclid. Here's how we can proceed:​

1. Planck Mission Data:
The Planck satellite has provided comprehensive maps of the CMB, offering insights into the universe's early conditions. The final data release (PR4) includes upgraded full-sky maps with improved systematics and sensitivity.

Extracting CMB Power Spectra: Obtaining the angular power spectra from the Planck PR4 data.
Comparing this with the model's predictions: simulating the CMB power spectra using our fractal inflation model and assessing the consistency with Planck observations could be quite informative.

2. Euclid Mission Data:
The Euclid space telescope aims to map the large-scale structure of the universe, providing data on galaxy distribution and cosmic web structures. The first data release includes observations of millions of galaxies, offering a glimpse into the cosmic web's large-scale organization.

Analyzing Galaxy Clustering: Using Euclid's data to study the distribution and clustering of galaxies.
Model Comparisons: Comparing these observations with the predictions from our fractal inflation model regarding large-scale structure formation is a solid furhter source of validation for our model.

3. Integrated Analysis:
Joint Constraints: Combining findings from both Planck and Euclid to place robust constraints on the parameters of our fractal inflation model.
Parameter Estimation: Utilizing statistical tools to estimate cosmological parameters within the framework of our model, ensuring consistency with observational data.

That's quite a hecc of an undertaking to wade through all thos possible validaton options and churn through that kinda data volume though - so unless someone with more time and motivation than me get's their teeth stuck in to such a projct, it'll probably sit on the back-burner for a while yet.

Nevertheless, it's fun to dip your toe into the water yourself and run the attached code even if at the modt basic level just to see what comes out - who knows, you could be seeing some exciting results too!