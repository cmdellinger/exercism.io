public class WeatherStation
{
    private Reading latestReading;
    private readonly List<DateTime> recordDates = new();
    private readonly List<decimal> temperatures = new();

    public void AcceptReading(Reading reading)
    {
        latestReading = reading;
        recordDates.Add(DateTime.Now);
        temperatures.Add(reading.Temperature);
    }

    public void ClearAll()
    {
        latestReading = new Reading();
        recordDates.Clear();
        temperatures.Clear();
    }

    public decimal LatestTemperature => latestReading.Temperature;

    public decimal LatestPressure => latestReading.Pressure;

    public decimal LatestRainfall => latestReading.Rainfall;

    public bool HasHistory => recordDates.Count > 1;

    public Outlook ShortTermOutlook => latestReading.Equals(new Reading()) ? throw new ArgumentException()
        : latestReading switch
        {
            {Pressure: < 10m, Temperature: < 30m} => Outlook.Cool,
            {Temperature: > 50m} => Outlook.Good,
            _ => Outlook.Warm
        };

    public Outlook LongTermOutlook => latestReading switch
        {
            {WindDirection: WindDirection.Easterly, Temperature: >20m} => Outlook.Good,
            {WindDirection: WindDirection.Southerly} => Outlook.Good,
            {WindDirection: WindDirection.Northerly} => Outlook.Cool,
            {WindDirection: WindDirection.Easterly} => Outlook.Warm,
            {WindDirection: WindDirection.Westerly} => Outlook.Rainy,
            _ => throw new ArgumentException()
        };

    public State RunSelfTest() => latestReading.Equals(new Reading()) ? State.Bad : State.Good;
}

/*** Please do not modify this struct ***/
public struct Reading
{
    public decimal Temperature { get; }
    public decimal Pressure { get; }
    public decimal Rainfall { get; }
    public WindDirection WindDirection { get; }

    public Reading(decimal temperature, decimal pressure,
        decimal rainfall, WindDirection windDirection)
    {
        Temperature = temperature;
        Pressure = pressure;
        Rainfall = rainfall;
        WindDirection = windDirection;
    }
}

/*** Please do not modify this enum ***/
public enum State
{
    Good,
    Bad
}

/*** Please do not modify this enum ***/
public enum Outlook
{
    Cool,
    Rainy,
    Warm,
    Good
}

/*** Please do not modify this enum ***/
public enum WindDirection
{
    Unknown, // default
    Northerly,
    Easterly,
    Southerly,
    Westerly
}
