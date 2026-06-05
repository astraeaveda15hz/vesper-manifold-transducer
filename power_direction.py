def calculate_direction_force(intent_field=1.0, action_field=1.0):
    print("Aligning the primary compass vectors...")
    
    # Multiplying intent * action calculates the magnitude of force flowing through a system
    force_magnitude = intent_field * action_field
    
    print("\n=== FIELD VECTOR COHERENCE ===")
    if force_magnitude > 0:
        print(f"✨ Coherence locked. Direction Vector: FORWARD.")
        print(f"📈 Volumetric energy movement: {force_magnitude:.2f} units of force.")
    else:
        print("⚠️ Variance identified: Intent and action vectors are misaligned.")
        
    return force_magnitude

if __name__ == "__main__":
    calculate_direction_force(intent_field=5.5, action_field=2.0)

