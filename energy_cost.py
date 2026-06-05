import math

class EnergyThermodynamics:
    def __init__(self, temp_kelvin=300):
        # Standard physical constants initialized precisely
        self.k_b = 1.380649e-23  # Boltzmann Constant
        self.T = temp_kelvin

    def get_landauer_minimum(self) -> float:
        """
        Calculates the minimum energy required to erase 1 bit of system friction.
        """
        return self.k_b * self.T * math.log(2)

    def calculate_net_work(self, initial_k: float, final_k: float) -> float:
        """
        W_net = Delta_Ek (Classical Work-Energy Theorem applied to kinetic shift)
        """
        return final_k - initial_k

if __name__ == "__main__":
    thermo = EnergyThermodynamics(temp_kelvin=300)
    min_energy = thermo.get_landauer_minimum()
    print("=== THERMODYNAMIC ENGINE LEDGER ===")
    print(f"Minimum Negentropy Threshold: {min_energy:.4e} Joules")
