static class Badge
{
    public static string Print(int? id, string name, string? department)
    {
        List<string> idString = new List<string>();
        if (id is not null) idString.Add($"[{id}]");
        idString.Add($"{name}");
        idString.Add(department?.ToUpper() ?? "OWNER");
        return String.Join(" - ", idString);
    }
}