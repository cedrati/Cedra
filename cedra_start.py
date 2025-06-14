"""
Cedra Constant - Quick Start Demo
Author: Olivier Cedrati
Year: 2025
Description: Demonstration of the Cedra constant properties including deterministic chaos 
             sequences, golden ratio connections, and discrete spacetime geometry.
             
Cedra = √3 + √2 + √(1/2) - 2 ≈ 1.853371151128520

Key Features:
- Deterministic chaos sequence with perfect uniform distribution
- Exact golden ratio relationship via auxiliary constant Delta
- Duality between structured chaos and pure order
- Applications in quantum Monte Carlo, discrete time systems, and 3+1D spacetime modeling

License: CC BY-NC 4.0
Repository: https://github.com/cedrati/Cedra
"""

import math

# Define Cedra constant
cedra = math.sqrt(3) + math.sqrt(2) + math.sqrt(1/2) - 2
ln_cedra = math.log(cedra)

# Define Delta constant
delta = (1 + math.sqrt(5)) / (2*math.sqrt(3) + 3*math.sqrt(2) - 4)

# Golden ratio connection
phi = cedra * delta
golden_ratio = (1 + math.sqrt(5)) / 2

print(f"Cedra = {cedra}")
print(f"ln(Cedra) = {ln_cedra}")
print(f"Delta = {delta}")
print(f"Phi (Cedra * Delta) = {phi}")
print(f"Golden Ratio = {golden_ratio}")
print(f"Connection precision: {abs(phi - golden_ratio):.10f}")

# DETERMINISTIC CHAOS Formula: Xn = (n × ln(Cedra)) mod 1
def chaos_sequence(n):
    return (n * ln_cedra) % 1

# ORDER Formula: Yn = (n - ln(Cedra)) mod 1
def order_sequence(n):
    return (n - ln_cedra) % 1

# Test the sequences
print("\nCHAOS sequence (first 10 values):")
for n in range(1, 11):
    xn = chaos_sequence(n)
    print(f"X{n} = {xn:.6f}")

print(f"\nORDER sequence (constant value):")
yn = order_sequence(1)
print(f"Yn = {yn:.6f} (same for all n)")

# Verify the duality
print(f"\nDuality verification:")
print(f"ln(Cedra) = {ln_cedra:.6f}")
print(f"1 - ln(Cedra) = {1 - ln_cedra:.6f}")
print(f"Sum = {ln_cedra + (1 - ln_cedra):.6f}")

# Golden ratio relationship
print(f"\nGolden Ratio Connection:")
print(f"Cedra * Delta = {cedra * delta:.10f}")
print(f"φ (exact) = {golden_ratio:.10f}")
print(f"Perfect match: {abs(cedra * delta - golden_ratio) < 1e-15}")
