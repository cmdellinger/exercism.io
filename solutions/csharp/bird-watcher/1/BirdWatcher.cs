class BirdCount
{
    private int[] _birdsPerDay;

    public BirdCount(int[] birdsPerDay)
    {
        _birdsPerDay = birdsPerDay;
    }

    public static int[] LastWeek()
    {
        return [0, 2, 5, 3, 7, 8, 4];
    }

    public int Today()
    {
        return _birdsPerDay[^1];
    }

    public void IncrementTodaysCount()
    {
        _birdsPerDay[^1] += 1;
    }

    public bool HasDayWithoutBirds()
    {
        foreach (int birdCount in _birdsPerDay)
        {
            if (birdCount == 0) return true;
        }
        return false;
    }

    public int CountForFirstDays(int numberOfDays)
    {
        return _birdsPerDay[..(numberOfDays)].Aggregate(0, (sum, next) => sum + next);
    }

    public int BusyDays()
    {
        return _birdsPerDay.Count(countPerDay => countPerDay >=5);
    }
}
