class RemoteControlCar
{
    private int _speed;
    private int _batteryDrain;
    private int _batteryPercentage;
    
    public RemoteControlCar(int speed, int batteryDrain)
    {
        this._speed = speed;
        this._batteryDrain = batteryDrain;
        this._batteryPercentage = 100;
    }

    public bool BatteryDrained()
    {
        return _batteryPercentage < _batteryDrain;
    }

    public int DistanceDriven()
    {
        return (100 - _batteryPercentage) * _speed / _batteryDrain;
    }

    public void Drive()
    {
        if (!BatteryDrained())
        {
            _batteryPercentage -= _batteryDrain;
        }
    }

    public static RemoteControlCar Nitro()
    {
        return new RemoteControlCar(50, 4);
    }
}

class RaceTrack
{
    private int _distance;
    
    public RaceTrack(int distance)
    {
        this._distance = distance;
    }

    public bool TryFinishTrack(RemoteControlCar car)
    {
        while (!car.BatteryDrained())
        {
            car.Drive();
            if (car.DistanceDriven() >= _distance) return true;
        }
        return false;
    }
}
