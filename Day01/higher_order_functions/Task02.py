def check_password(rule, n, string):
    if rule not in ["lower", "special"]:
        raise ValueError("Invalid rule. Supported rules are 'lower' and 'special'.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid value for 'n'. 'n' should be a non-negative integer.")

    if not isinstance(string, str):
        raise ValueError("Invalid value for 'string'. 'string' should be a string.")

    if rule == "lower":
        def nbr_lower(string):
            count = 0
            for char in string:
                if char.islower():
                    count += 1
            return count

        if nbr_lower(string) >= n:
            return True
        else:
            return False

    if rule == "special":
        def nbr_special(string):
            count = 0
            for char in string:
                if not (char.isalpha() or char.isdigit()):
                    count += 1
            return count

        if nbr_special(string) >= n:
            return True
        else:
            return False

# Example usage with error handling
try:
    print(check_password("lower", 4, "bonjour123"))  # Vérifie les minuscules
    print(check_password("special", 2, "coucou!!!"))  # Vérifie les caractères spéciaux
    # Uncomment the lines below to test invalid inputs and rules:
    # print(check_password("invalid_rule", 2, "password"))  # Invalid rule
    # print(check_password("lower", -2, "password"))  # Invalid n
    # print(check_password("lower", 2, 123))  # Invalid string
except ValueError as e:
    print(f"Error: {e}")
