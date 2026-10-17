# Math Slayer: Competition Math Toolkit 🎯

**Math Slayer** is a fast, algorithmic Python engine designed to efficiently solve challenging competitive mathematics problems, such as those found in the **AMC 8, AMC 10/12, and various Math Olympiads**.

---

## 🚀 Features## 🛠️ Requirements & Installation

This toolkit runs entirely on standard Python libraries, meaning **no external dependencies** are required. 

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Math-Slayer
   ```

2. **Ensure you have Python 3 installed:**
   ```bash
   python --version
   ```

---

## 💻 Quick Start & Usage

Here is a quick look at how you can utilize the `MathEngine` within your own scripts or your main entry point:
```python
from app import MathEngine

# 1. Get Prime Factorization & Divisor Count for 360
n = 360
print(f"Prime Factors of {n}:", MathEngine.prime_factors(n)) 
# Output: {2: 3, 3: 2, 5: 1}

print(f"Total Divisors of {n}:", MathEngine.count_divisors(n))
# Output: 24 (since (3+1)*(2+1)*(1+1) = 24)

# 2. Fast Modular Exponentiation: (7^100000) % 13
print("Modular Power:", MathEngine.modular_power(7, 100000, 13))
# Output: 9

# 3. Combinatorics: Selecting 3 items out of 10
print("Combinations (10C3):", MathEngine.combinations_count(10, 3))
# Output: 120
```

---

## 📈 Future Roadmap
* [ ] Add Great Common Divisor (GCD) & Least Common Multiple (LCM) Euclidean engines.
* [ ] Integrate Chinese Remainder Theorem (CRT) solvers.
* [ ] Support for Diophantine equation solvers.

---

## 🤝 Contributing & Feedback
If you are preparing for math competitions or love number theory, feel free to **star** this repository, open an **issue**, or submit a **pull request** to add new algorithmic tools!


* **Prime Factorization & Divisors**: Computes complete canonical prime factorizations and counts total positive divisors using exponent products.
* **Fast Modular Exponentiation**: Solves massive modular powers (\(b^e \pmod{m}\)) in logarithmic time to prevent memory bottlenecks.
* **Combinatorics Engine**: Calculates precise permutations (\(_nP_r\)) and combinations (\(_nC_r\)) without floating-point errors or integer overflow.
