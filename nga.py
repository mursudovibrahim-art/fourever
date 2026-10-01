# ============================================================
# Məntiqi (Bool) əməliyyatlar — dərstdəki qapıların analoqu
# ============================================================

def AND(p, q):       return p and q
def OR(p, q):        return p or q
def XOR(p, q):       return p != q          # fərqli olduqda 1 (True)
def NOT(p):          return not p
def IMPLICATION(p, q): return (not p) or q  # p -> q : yalnız p=1, q=0 olduqda 0
def EQUIVALENCE(p, q): return p == q        # p <-> q
def NAND(p, q):      return not (p and q)
def NOR(p, q):       return not (p or q)


def truth_table():
    """Bütün əməliyyatların həqiqət cədvəli (0/1 ilə)"""
    print(f"{'p':^3} {'q':^3} | {'AND':^4} {'OR':^4} {'XOR':^4} {'IMP(->)':^8} {'EQ(<->)':^8} {'NAND':^5}")
    print("-" * 55)
    for p in (0, 1):
        for q in (0, 1):
            print(f"{p:^3} {q:^3} | "
                  f"{int(AND(p,q)):^4} {int(OR(p,q)):^4} {int(XOR(p,q)):^4} "
                  f"{int(IMPLICATION(p,q)):^8} {int(EQUIVALENCE(p,q)):^8} {int(NAND(p,q)):^5}")


# ============================================================
# Çoxluq (set) əməliyyatları — X, Y, Z ilə işləyəcək hissə
# ============================================================

def set_operations(X, Y, Z, U=None):
    """
    Çoxluq versiyaları:
      AND(X,Y)      -> X ∩ Y        (kəsişmə)
      OR(X,Y)       -> X ∪ Y        (birləşmə)
      XOR(X,Y)      -> simmetrik fərq (yalnız birində olanlar)
      NOT(X)        -> U \ X        (tamamlayıcı, universal çoxluq lazımdır)
      IMP(X,Y)      -> X ⊆ Y yoxlanışı (hər element yoxlanılır)
    """
    print("X =", X)
    print("Y =", Y)
    print("Z =", Z)
    print("-" * 40)
    print("X ∩ Y (AND)        :", X & Y)
    print("X ∪ Y (OR)         :", X | Y)
    print("X XOR Y            :", X ^ Y)
    print("X - Y              :", X - Y)
    print("Y - X              :", Y - X)
    if U is not None:
        print("X-in tamamlayıcısı (NOT):", U - X)
    print("X ∪ Y ∪ Z          :", X | Y | Z)
    print("X ∩ Y ∩ Z          :", X & Y & Z)
    print("(X ∪ Y) ∩ Z        :", (X | Y) & Z)
    print("(X ∩ Y) ∪ Z        :", (X & Y) | Z)

    # İmplication: X -> Y  ⇔  X hər elementi Y-dədirsə True
    print("X ⊆ Y (X -> Y)     :", X.issubset(Y))
    print("Y ⊆ Z (Y -> Z)     :", Y.issubset(Z))
    print("X ⊆ Z (X -> Z)     :", X.issubset(Z))


def implication_analysis(X, Y):
    """
    İmplication-ın çoxluq izahı:
    p -> q yalnız p=1, q=0 olduqda False-dir.
    Çoxluqda: X-də olan, Y-də OLMAYAN elementlər varsa,
    implication pozulur (cavab False).
    """
    counterexample = X - Y          # "p=1, q=0" halları
    if counterexample:
        print(f"X -> Y = False ❌ (əks-nümunə elementlər: {counterexample})")
    else:
        print("X -> Y = True ✅ (X-in bütün elementləri Y-dədir)")


# ============================================================
# Nümunə istifadə — siz öz X, Y, Z-nizi bura yazacaqsınız
# ============================================================

if __name__ == "__main__":
    truth_table()
    print()

    # Test üçün nümunə çoxluqlar (siz bunları dəyişəcəksiniz):
    U = {1, 2, 3, 4, 5, 6, 7, 8}
    X = {1, 2, 3}
    Y = {2, 3, 4, 5}
    Z = {3, 4, 5, 6}

    set_operations(X, Y, Z, U)
    print()
    implication_analysis(X, Y)