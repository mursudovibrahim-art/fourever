import re

# 8-bitlik rəqəmlər (bit zəncirləri)
x_str, y_str, z_str = "00001111", "00110011", "01010101"
vars_bit = {"x": x_str, "y": y_str, "z": z_str}
vars_val = {"x": int(x_str, 2), "y": int(y_str, 2), "z": int(z_str, 2)}


def to_bin(val, bits=8):
    return format(val & ((1 << bits) - 1), f"0{bits}b")


def get_operation_name(expr):
    """Əməliyyatın ingilis dilində adını təyin edir"""
    expr_upper = expr.upper()
    ops = []
    if "NOT" in expr_upper:
        ops.append("NOT (Inversion)")
    if "AND" in expr_upper:
        ops.append("AND (Conjunction)")
    if "XOR" in expr_upper:
        ops.append("XOR (Exclusive OR)")
    elif "OR" in expr_upper:
        ops.append("OR (Disjunction)")

    return " + ".join(ops) if ops else "Logical Operation"


def replace_variables_with_bits(expr):
    """x, y, z dəyişənlərini 0 və 1-lərdən ibarət rəqəmlərlə əvəz edir"""
    result = expr
    for var in ["x", "y", "z"]:
        result = re.sub(rf"\b{var}\b", vars_bit[var], result, flags=re.IGNORECASE)
    return result


print("=" * 65)
print("LOGICAL OPERATIONS EVALUATOR (ENGLISH WORDS ONLY)")
print("=" * 65)
print("Available Binary Numbers:")
print(f"  x = {x_str}")
print(f"  y = {y_str}")
print(f"  z = {z_str}")
print("-" * 65)
print("Use ONLY word operators: NOT, AND, OR, XOR")
print("Example inputs: 'NOT x', 'x AND y', 'x XOR z', '(x OR y) AND NOT z'")
print("Type 'exit' or 'quit' to stop.")
print("=" * 65)

while True:
    user_input = input("\nEnter operation: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Program finished.")
        break

    if not user_input:
        continue

    # Yalnız ingilis dilindəki söz-operatorları Python operatorlarına çeviririk
    eval_expr = user_input.upper()
    eval_expr = re.sub(r"\bNOT\b", "~", eval_expr)
    eval_expr = re.sub(r"\bAND\b", "&", eval_expr)
    eval_expr = re.sub(r"\bOR\b", "|", eval_expr)
    eval_expr = re.sub(r"\bXOR\b", "^", eval_expr)

    for var in ["X", "Y", "Z"]:
        eval_expr = re.sub(rf"\b{var}\b", var.lower(), eval_expr)

    try:
        # Məntiqi əməliyyatı hesablayırıq
        res_val = eval(eval_expr, {"__builtins__": None}, vars_val)
        res_bin = to_bin(res_val)

        op_name = get_operation_name(user_input)
        num_expr = replace_variables_with_bits(user_input)

        print("-" * 50)
        print(f"Operation Name : {op_name}")
        print(f"Your Expression: {user_input}")
        print(f"With Numbers   : {num_expr}")
        print(f"Result (Binary) : {res_bin}")
        print(f"Result (Decimal): {res_val & 0xFF}")
        print("-" * 50)

    except Exception:
        print("Error! Zəhmət olmasa işarə (~, &, |, ^) yox, nyalnız sözlərdən (NOT, AND, OR, XOR) və x, y, z-dən istifadə et.")