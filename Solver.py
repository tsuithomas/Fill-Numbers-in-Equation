import re
import itertools

def solve_equation(equation_str):
    # Find all variable names (assume single letters a-z, not 'e' for exponent)
    variables = sorted(list(set(re.findall(r'\b[a-df-z]\b', equation_str))))
    n_vars = len(variables)
    
    # Generate all permutations of 1-9 of length n_vars
    for perm in itertools.permutations(range(1, 10), n_vars):
        # Prepare local variables for eval
        local_vars = dict(zip(variables, perm))
        # Replace '^' with '**' if needed (Python uses ** for power)
        expr = equation_str.replace('^', '**')
        try:
            # Evaluate the equation: left = right
            left, right = expr.split('=')
            if eval(left, {}, local_vars) == eval(right, {}, local_vars):
                # Return just one valid solution as a list, in variable order
                return [local_vars[v] for v in variables]
        except Exception:
            continue
    # If no solution is found
    return None

# Example usage
example1 = "a+b=4"
example2 = "a*b-c=71"
example3 = "(a*b*c)-d = 128"
example4 = "(a*(b+c))-d = 44"
example5 = "b^c-d=129"

print(solve_equation(example1)) # Example output: [1, 3]
print(solve_equation(example2)) # Example output: [8, 9, 1]
print(solve_equation(example3)) # Example output: [3, 5, 9, 7]
print(solve_equation(example4)) # Example output: [3, 6, 9, 1]
print(solve_equation(example5)) # None
