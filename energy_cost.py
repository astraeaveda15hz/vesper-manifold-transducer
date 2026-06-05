import math

def calculate_energy_toll(temperature_kelvin=300):
    print(f"Calibrating balancing scales at ambient temperature: {temperature_kelvin} K")
    
    # Absolute physical constants used in thermodynamics
    boltzmann_constant = 1.380649e-23
    
    # Landauer's Principle: The exact physical cost to clear 1 bit of friction/noise
    # Formula: E = k * T * ln(2)
    landauer_minimum = boltzmann_constant * temperature_kelvin * math.log(2)
    
    print("\n=== THERMODYNAMIC COST BALANCE ===")
    print(f"✨ Minimum energy to lock 1 bit of chaos into reality: {landauer_minimum:.4e} Joules")
    
    return landauer_minimum

if __name__ == "__main__":
    calculate_energy_toll()

