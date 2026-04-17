import numpy as np
import matplotlib.pyplot as plt

# Parameters for a periodic potential (Kronig-Penney simplified)
energy = np.linspace(0.1, 30, 1000)
P = 3.0  # Barrier strength

# The function f(E) comes from the Schrodinger equation in a periodic potential
# If |f(E)| <= 1, the energy is "Allowed" (Resonance/Transmission)
# If |f(E)| > 1, the energy is "Forbidden" (Gap)
f_E = np.cos(np.sqrt(energy)) + (P / np.sqrt(energy)) * np.sin(np.sqrt(energy))

plt.figure(figsize=(10, 5))
plt.plot(energy, f_E, label='Dispersion Relation $f(E)$')
plt.axhspan(-1, 1, color='green', alpha=0.2, label='Allowed Bands (Resonance)')
plt.axhline(1, color='red', linestyle='--')
plt.axhline(-1, color='red', linestyle='--')

plt.title('Resonance in Periodic Potentials: Energy Bands')
plt.xlabel('Energy (E)')
plt.ylabel('f(E)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
