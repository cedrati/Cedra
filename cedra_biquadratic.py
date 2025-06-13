"""
Cedra Temporal Quasicrystal Generator
Author: Olivier Cedrati
Year: 2025
Description: Cedra biquadratic solver.

License: CC BY-NC 4.0
Repository: https://github.com/cedrati/Cedra
Paper: "Cedra: A Mathematical Constant for Temporal Quasicrystal Generation" (2025)
"""

import math

class CedraSolver:
   """
   Biquadratic equation solver: ax⁴ + bx² + c = 0
   Uses substitution y = x² to transform into quadratic equation
   """
   
   def __init__(self):
       self.solutions_count = 0
       self.special_cases_count = 0
   
   def _detect_special_cases(self, a, b, c):
       """Detect and solve special cases for better numerical stability"""
       eps = 1e-15
       
       if abs(a) < eps:
           return None
       
       self.special_cases_count += 1
       
       # Case 1: c = 0 -> x²(ax² + b) = 0
       if abs(c) < eps:
           if abs(b) < eps:
               return [0.0]
           elif -b/a > eps:
               sqrt_val = math.sqrt(-b/a)
               return sorted([-sqrt_val, 0.0, sqrt_val])
           else:
               return [0.0]
       
       # Case 2: b = 0 -> ax⁴ + c = 0
       if abs(b) < eps:
           ratio = -c/a
           if ratio < -eps:
               return []
           elif abs(ratio) < eps:
               return [0.0]
           else:
               root = math.pow(ratio, 0.25)
               return sorted([-root, root])
       
       # Case 3: Perfect square form (discriminant = 0)
       discriminant = b*b - 4*a*c
       if abs(discriminant) < eps * max(b*b, abs(4*a*c), 1):
           x_squared = -b/(2*a)
           if x_squared > eps:
               x_val = math.sqrt(x_squared)
               return sorted([-x_val, x_val])
           elif abs(x_squared) <= eps:
               return [0.0]
           else:
               return []
       
       return None
   
   def _solve_general_case(self, a, b, c):
       """Solve general biquadratic equation using quadratic formula"""
       # Substitution y = x² transforms ax⁴ + bx² + c = 0 into ay² + by + c = 0
       discriminant = b*b - 4*a*c
       
       if discriminant < 0:
           return []
       
       sqrt_discriminant = math.sqrt(discriminant)
       
       # Use numerically stable formulas (Citardauq method)
       if b >= 0:
           y1 = (-b - sqrt_discriminant) / (2*a)
           y2 = (2*c) / (-b - sqrt_discriminant) if sqrt_discriminant > 1e-15 else 0
       else:
           y1 = (-b + sqrt_discriminant) / (2*a)
           y2 = (2*c) / (-b + sqrt_discriminant) if sqrt_discriminant > 1e-15 else 0
       
       # Convert y solutions back to x solutions
       solutions = []
       tolerance = 1e-14
       
       for y in [y1, y2]:
           if y > tolerance:
               x_val = math.sqrt(y)
               solutions.extend([x_val, -x_val])
           elif abs(y) <= tolerance:
               solutions.append(0.0)
       
       # Remove duplicates
       unique_solutions = []
       for sol in sorted(solutions):
           if not any(abs(sol - existing) < tolerance for existing in unique_solutions):
               unique_solutions.append(sol)
       
       return unique_solutions
   
   def solve(self, a, b, c):
       """
       Solve biquadratic equation ax⁴ + bx² + c = 0
       
       Args:
           a, b, c: Coefficients of the biquadratic equation
           
       Returns:
           List of real solutions sorted in ascending order
       """
       self.solutions_count += 1
       
       # Input validation
       if not all(math.isfinite(x) for x in [a, b, c]):
           return []
       if abs(a) < 1e-16:
           return []
       
       # Try special cases first
       special_result = self._detect_special_cases(a, b, c)
       if special_result is not None:
           return special_result
       
       # Solve general case
       return self._solve_general_case(a, b, c)
   
   def get_stats(self):
       """Return solver statistics"""
       return {
           'total_solutions': self.solutions_count,
           'special_cases': self.special_cases_count,
           'special_case_rate': self.special_cases_count / max(1, self.solutions_count) * 100
       }


# Example usage and test cases
if __name__ == "__main__":
   solver = CedraSolver()
   
   # Test cases
   test_cases = [
       (1, -5, 4),      # x⁴ - 5x² + 4 = 0, solutions: ±1, ±2
       (1, -2, 1),      # x⁴ - 2x² + 1 = 0, solutions: ±1 (perfect square)
       (1, 0, -1),      # x⁴ - 1 = 0, solutions: ±1
       (1, -10, 9),     # x⁴ - 10x² + 9 = 0, solutions: ±1, ±3
       (2, -8, 6),      # 2x⁴ - 8x² + 6 = 0, solutions: ±1, ±√3
       (1, 1, 1),       # x⁴ + x² + 1 = 0, no real solutions
   ]
   
   print("Cedra Biquadratic Solver Test Results:")
   print("=" * 50)
   
   for i, (a, b, c) in enumerate(test_cases, 1):
       solutions = solver.solve(a, b, c)
       print(f"Test {i}: {a}x⁴ + {b}x² + {c} = 0")
       
       if solutions:
           print(f"  Solutions: {[f'{x:.6f}' for x in solutions]}")
           # Verify solutions
           max_error = 0
           for x in solutions:
               error = abs(a * x**4 + b * x**2 + c)
               max_error = max(max_error, error)
           print(f"  Max error: {max_error:.2e}")
       else:
           print("  No real solutions")
       print()
   
   # Display statistics
   stats = solver.get_stats()
   print("Solver Statistics:")
   print(f"  Total equations solved: {stats['total_solutions']}")
   print(f"  Special cases detected: {stats['special_cases']}")
   print(f"  Special case rate: {stats['special_case_rate']:.1f}%")
