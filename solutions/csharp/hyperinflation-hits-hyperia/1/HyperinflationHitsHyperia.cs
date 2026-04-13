public static class CentralBank
{
    public static string DisplayDenomination(long @base, long multiplier)
    {
        try
        {
            checked // required to to throw OverflowException, else number wraps
            {
                return (@base * multiplier).ToString();
            }
        }
        catch (OverflowException e)
        {
            return "*** Too Big ***";
        }
    }

    public static string DisplayGDP(float @base, float multiplier)
    {
        float gdp = @base * multiplier;
        if (float.IsInfinity(gdp)) return "*** Too Big ***"; // float overflow escapes to infinity
        return gdp.ToString();
    }

    public static string DisplayChiefEconomistSalary(decimal salaryBase, decimal multiplier)
    {
        try
        {
            return (salaryBase * multiplier).ToString(); // decimal automatically throws OverflowException
        }
        catch (OverflowException e)
        {
            return "*** Much Too Big ***";
        }
    }
}