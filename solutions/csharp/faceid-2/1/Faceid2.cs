public class FacialFeatures : IEquatable<FacialFeatures>
{
    public string EyeColor { get; }
    public decimal PhiltrumWidth { get; }
    
    public FacialFeatures(string eyeColor, decimal philtrumWidth)
    {
        EyeColor = eyeColor;
        PhiltrumWidth = philtrumWidth;
    }
    
    public bool Equals(FacialFeatures? other)
    {
        if (other is null) return false;
        return EyeColor == other.EyeColor && PhiltrumWidth == other.PhiltrumWidth;
    }
    
    public override bool Equals(object? obj)
    {
        return Equals(obj as FacialFeatures);
    }
    
    public override int GetHashCode()
    {
        return HashCode.Combine(EyeColor, PhiltrumWidth);
    }
    
    public static bool operator ==(FacialFeatures? face1, FacialFeatures? face2)
    {
        return Equals(face1, face2);
    }
    
    public static bool operator !=(FacialFeatures? face1, FacialFeatures? face2)
    {
        return !Equals(face1, face2);
    } 
}

public class Identity : IEquatable<Identity>
{
    public string Email { get; }
    public FacialFeatures FacialFeatures { get; }

    public Identity(string email, FacialFeatures facialFeatures)
    {
        Email = email;
        FacialFeatures = facialFeatures;
    }

    public bool Equals(Identity? other)
    {
        if (other is null) return false;
        return Email == other.Email && FacialFeatures == other.FacialFeatures;
    }
    
    public override bool Equals(object? obj)
    {
        return Equals(obj as Identity);
    }
    
    public override int GetHashCode()
    {
        return HashCode.Combine(Email, FacialFeatures);
    }
    
    public static bool operator ==(Identity? id1, Identity? id2)
    {
        return Equals(id1, id2);
    }
    
    public static bool operator !=(Identity? id1, Identity? id2)
    {
        return !Equals(id1, id2);
    } 
}

public class Authenticator
{
    private readonly Identity admin = new Identity("admin@exerc.ism", new FacialFeatures("green", 0.9m));
    
    public HashSet<Identity> Users { get; }

    public Authenticator()
    {
        Users = new HashSet<Identity> { admin };
    }
    
    public static bool AreSameFace(FacialFeatures faceA, FacialFeatures faceB)
    {
        return faceA == faceB;
    }

    public bool IsAdmin(Identity identity)
    {
        return identity == admin;
    }

    public bool Register(Identity identity)
    {
        return Users.Add(identity);
    }

    public bool IsRegistered(Identity identity)
    {
        return Users.Contains(identity);
    }

    public static bool AreSameObject(Identity identityA, Identity identityB)
    {
        return ReferenceEquals(identityA, identityB);
    }
}