abstract class Character
{
    private string _characterType;
    protected bool _isVulnerable;
    
    protected Character(string characterType)
    {
        this._characterType = characterType;
        this._isVulnerable = false;
    }

    public abstract int DamagePoints(Character target);

    public virtual bool Vulnerable()
    {
        return _isVulnerable;
    }

    public override string ToString()
    {
        return $"Character is a {_characterType}";
    }
}

class Warrior : Character
{
    public Warrior() : base("Warrior")
    {
    }

    public override int DamagePoints(Character target)
    {
        if (target.Vulnerable())
            return 10;
        else
            return 6;
    }
}

class Wizard : Character
{
    public Wizard() : base("Wizard")
    {
        this._isVulnerable = true;
    }

    public override int DamagePoints(Character target)
    {
        if (_isVulnerable)
            return 3;
        else
            return 12;
    }

    public void PrepareSpell()
    {
        _isVulnerable = false;
    }
}
