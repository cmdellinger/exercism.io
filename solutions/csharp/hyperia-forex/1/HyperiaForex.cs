public struct CurrencyAmount : IEquatable<CurrencyAmount>
{
    private decimal _amount;
    private string _currency;

    public CurrencyAmount(decimal amount, string currency)
    {
        _amount = amount;
        _currency = currency;
    }

    private static void ThrowIfDifferentCurrency(CurrencyAmount left, CurrencyAmount right)
    {
        if (left._currency != right._currency)
            throw new ArgumentException("currencies are not the same");
    }

    public bool Equals(CurrencyAmount other)
    {
        return _currency == other._currency && _amount == other._amount;
    }

    public override bool Equals(object? obj)
    {
        return obj is CurrencyAmount ca && Equals(ca);
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(_amount, _currency);
    }

    public static bool operator ==(CurrencyAmount left, CurrencyAmount right)
    {
        ThrowIfDifferentCurrency(left, right);
        return left._amount == right._amount;
    }

    public static bool operator !=(CurrencyAmount left, CurrencyAmount right)
    {
        ThrowIfDifferentCurrency(left, right);
        return left._amount != right._amount;
    }

    public static bool operator >(CurrencyAmount left, CurrencyAmount right)
    {
        ThrowIfDifferentCurrency(left, right);
        return left._amount > right._amount;
    }

    public static bool operator <(CurrencyAmount left, CurrencyAmount right)
    {
        ThrowIfDifferentCurrency(left, right);
        return left._amount < right._amount;
    }

    public static CurrencyAmount operator +(CurrencyAmount left, CurrencyAmount right)
    {
        ThrowIfDifferentCurrency(left, right);
        return new CurrencyAmount(left._amount + right._amount, left._currency);
    }

    public static CurrencyAmount operator -(CurrencyAmount left, CurrencyAmount right)
    {
        ThrowIfDifferentCurrency(left, right);
        return new CurrencyAmount(left._amount - right._amount, left._currency);
    }

    public static CurrencyAmount operator *(CurrencyAmount left, decimal right)
    {
        return new CurrencyAmount(left._amount * right, left._currency);
    }

    public static CurrencyAmount operator *(decimal left, CurrencyAmount right)
    {
        return new CurrencyAmount(right._amount * left, right._currency);
    }

    public static CurrencyAmount operator /(CurrencyAmount left, decimal right)
    {
        return new CurrencyAmount(left._amount / right, left._currency);
    }

    public static explicit operator double(CurrencyAmount currencyAmount)
    {
        return (double)currencyAmount._amount;
    }

    public static implicit operator decimal(CurrencyAmount currencyAmount)
    {
        return currencyAmount._amount;
    }
}