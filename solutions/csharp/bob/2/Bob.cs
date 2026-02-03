public static class Bob
{
    public static string Response(string statement)
    {
        statement = statement.Trim();
        bool isYelling = statement == statement.ToUpper() && statement.Any(Char.IsLetter);
           
        if (statement.EndsWith('?'))
        {
            if (isYelling) return "Calm down, I know what I'm doing!";
            return "Sure.";
        }
        if (isYelling) return "Whoa, chill out!";
        if (statement == "") return "Fine. Be that way!";
        return "Whatever."; 
    }
}