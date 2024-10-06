def safe_divide(numerator, denominator):
    try:
        
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator / denominator

        if result.is_integer():
            return f"The result of the division is {int(result)}"
        else:
            return f"The result of the division is {result:.1f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."

