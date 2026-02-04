public static class Identifier
{
    public static string Clean(string identifier)
    {
        identifier = identifier.Replace(" ", "_").Replace("\0", "CTRL");
        identifier = String.Join("", identifier.Split("-").Select(
            (part, index) => (index > 0) ? Char.ToUpper(part[0]) + part.Substring(1): part
        ));
        identifier = String.Join("", identifier.Select(
            character => (Char.IsLetter(character) || character == '_') ? character : ' '
        )).Replace(" ", "");
        identifier = String.Join("", identifier.Where(c => !(c >= '\u03B1' && c <= '\u03C9')));
        return identifier;
    }
}
