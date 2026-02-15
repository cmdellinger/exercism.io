public static class TelemetryBuffer
{
    public static byte[] ToBuffer(long reading)
    {
        Byte[] bytes = BitConverter.GetBytes(reading);
        
        bool signed;
        int width;
        
        if (reading < 0)
        {
            signed = true;
            width = 16; // default: type = "short";
            if (reading < short.MinValue) //type = "int";
                width = 32;
            if (reading < int.MinValue) //type = "long";
                width = 64;
        }
        else
        {
            width = 16; //default: type = "ushort";
            signed = false;
            if (reading > ushort.MaxValue) //type = "int";
            {
                signed = true;
                width = 32;
            }
            if (reading > int.MaxValue) //type = "uint";
            {
                signed = false;
                width = 32;
            }
            if (reading > uint.MaxValue) //type = "long";
            {
                signed = true;
                width = 64;
            }
        }

        byte[] buffer = new byte[9];
        if (signed)
            Buffer.SetByte(buffer, 0, (byte)(256 - width/8));
        else
            Buffer.SetByte(buffer, 0, (byte)(width/8));
        
        Buffer.BlockCopy(bytes, 0, buffer, 1, width/8);

        return buffer;
    }

    public static long FromBuffer(byte[] buffer)
    {
        byte prefix = Buffer.GetByte(buffer, 0);
        return prefix switch
        {
            (byte) (256-8)  => BitConverter.ToInt64(buffer, 1),
            (byte) (256-4)  => BitConverter.ToInt32(buffer, 1),
            (byte) (256-2)  => BitConverter.ToInt16(buffer, 1),
            (byte) 2        => BitConverter.ToUInt16(buffer, 1),
            (byte) 4        => BitConverter.ToUInt32(buffer, 1),
            _ => 0,
           
        };
    }
}
