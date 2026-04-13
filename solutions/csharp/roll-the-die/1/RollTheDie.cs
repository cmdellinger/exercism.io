public class Player
{
    public int RollDie()
    {
        return new Random().Next(1, 19); // `Next` range is [min, max)
    }

    public double GenerateSpellStrength()
    {
        return new Random().NextDouble() * 100;
    }
}
