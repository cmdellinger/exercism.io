public static class SimpleCalculator
{
    public static string Calculate(int operand1, int operand2, string? operation)
    {
        int? solution = operation switch
        {
            "+" => operand1 + operand2,
            "*" => operand1 * operand2,
            "/" when operand2 != 0 => operand1 / operand2,
            "/" when operand2 == 0 => null,
            "" => throw new ArgumentException("No operation passed."),
            null => throw new ArgumentNullException("No operation passed."),
            _ => throw new ArgumentOutOfRangeException(operation, "Not a supported operation.")
        };
        return (solution is not null) ? $"{operand1} {operation} {operand2} = {solution}" : "Division by zero is not allowed.";
    }
}