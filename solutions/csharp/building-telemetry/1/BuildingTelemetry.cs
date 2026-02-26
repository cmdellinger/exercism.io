public class RemoteControlCar
{
    private int _batteryPercentage = 100;
    private int _distanceDrivenInMeters = 0;
    private string[] _sponsors = [];
    private int _latestSerialNum = 0;

    public void Drive()
    {
        if (_batteryPercentage > 0)
        {
            _batteryPercentage -= 10;
            _distanceDrivenInMeters += 2;
        }
    }

    public void SetSponsors(params string[] sponsors)
    {
        _sponsors = sponsors;
    }

    public string DisplaySponsor(int sponsorNum)
    {
        return _sponsors[sponsorNum];
    }

    public bool GetTelemetryData(ref int serialNum,
        out int batteryPercentage, out int distanceDrivenInMeters)
    {
        if (serialNum < _latestSerialNum)
        {
            serialNum = _latestSerialNum;
            batteryPercentage = -1;
            distanceDrivenInMeters = -1;
            return false;
        }
        else
        {
            _latestSerialNum = serialNum;
            batteryPercentage = _batteryPercentage;
            distanceDrivenInMeters = _distanceDrivenInMeters;
            return true;
        }
    }

    public static RemoteControlCar Buy()
    {
        return new RemoteControlCar();
    }
}

public class TelemetryClient
{
    private RemoteControlCar _car;

    public TelemetryClient(RemoteControlCar car)
    {
        _car = car;
    }

    public string GetBatteryUsagePerMeter(int serialNum)
    {
        bool dataFetched = _car.GetTelemetryData(ref serialNum, out int batteryPercentage, out int distanceDrivenInMeters);
        if(dataFetched && distanceDrivenInMeters > 0)
        {
            return $"usage-per-meter={(100-batteryPercentage)/distanceDrivenInMeters}";
        }
        return "no data";
    }
}
