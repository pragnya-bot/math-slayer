from solver import MathEngine as me


def print_menu():
    print("\n" + "=" * 48)
    print("        MATH SLAYER: COMPETITION TOOLKIT        ")
    print("=" * 48)
    print("1. Prime Factorization & Divisors")
    print("2. Last Digits / Modular Exponentiation (a^b % m)")
    print("3. Combinations (nCr) & Permutations (nPr)")
    print("4. Exit")
    print("=" * 48)


def main():
    while True:
        print_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            n = int(input("Enter positive integer: "))
            factors = me.prime_factors(n)
            divisors = me.count_divisors(n)
            factor_str = " * ".join([f"{p}^{e}" if e > 1 else str(p)
                                    for p, e in factors.items()])
            print(f"\nPrime Factorization: {n} = {factor_str}")
            print(f"Total Positive Divisors: {divisors}")

        elif choice == '2':
            base = int(input("Enter base (a): "))
            exp = int(input("Enter exponent (b): "))
            mod = int(
                input("Enter modulus (e.g., 10 for last digit, 100 for last two): "))
            result = me.modular_power(base, exp, mod)
            print(f"\n({base}^{exp}) mod {mod} = {result}")

        elif choice == '3':
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print(f"\n{n}C{r} (Combinations): {me.combinations_count(n, r):,}")
            print(f"{n}P{r} (Permutations): {me.permutations_count(n, r):,}")

        elif choice == '4':
            print("\nGo ace that math contest! Goodbye!")
            break
        else:
            print("\nInvalid choice, please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
