def parse_set(prompt):
    raw = input(prompt).strip()
    if not raw:
        return set()
    return set(raw.replace(",", " ").split())


def implication(A, B):
    counter = A - B
    if counter:
        return f"False ❌  (əks-nümunə: {counter})"
    return "True ✅  (A ⊆ B)"


def main():
    print("=== Çoxluq və Məntiqi Əməliyyatlar ===")

    while True:
        n = input("Neçə çoxluq? (2 və ya 3): ").strip()
        if n.isdigit() and int(n) in (2, 3):
            n = int(n)
            break
        print("❌ 2 və ya 3 yaz!")

    names = "ABC"
    sets = [parse_set(f"{names[i]} elementləri: ") for i in range(n)]
    for i in range(n):
        print(f"{names[i]} = {sets[i]}")

    A, B = sets[0], sets[1]
    C = sets[2] if n == 3 else None

    while True:
        print("""
--- ƏMƏLİYYAT SEÇ ---
1. A ∩ B (AND)
2. A ∪ B (OR)
3. A XOR B
4. A - B
5. A -> B (implication)""")
        if n == 3:
            print("""6. A ∪ B ∪ C
7. A ∩ B ∩ C
8. (A ∪ B) ∩ C
9. (A ∩ B) ∪ C
10. A -> B -> C (zəncir)""")
        print("0. Çıxış")

        ch = input("Seçim: ").strip()

        if ch == "0":
            print("Proqram bitdi!")
            break
        elif ch == "1":
            print("Nəticə:", A & B)
        elif ch == "2":
            print("Nəticə:", A | B)
        elif ch == "3":
            print("Nəticə:", A ^ B)
        elif ch == "4":
            print("Nəticə:", A - B)
        elif ch == "5":
            print("A -> B =", implication(A, B))
        elif ch == "6" and n == 3:
            print("Nəticə:", A | B | C)
        elif ch == "7" and n == 3:
            print("Nəticə:", A & B & C)
        elif ch == "8" and n == 3:
            print("Nəticə:", (A | B) & C)
        elif ch == "9" and n == 3:
            print("Nəticə:", (A & B) | C)
        elif ch == "10" and n == 3:
            print("A -> B =", implication(A, B))
            print("B -> C =", implication(B, C))
            print("A -> C =", implication(A, C))
            if A <= B <= C:
                print("Transitivlik ✅")
            else:
                print("Zəncir pozulub ❌")
        else:
            print("❌ Yanlış seçim!")


main()