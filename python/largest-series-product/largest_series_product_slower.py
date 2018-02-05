def largest_product(series, size):
    # validate inputs
    if not size: return 1
    series_length = len(series)
    if size > series_length or size < 0:
        raise ValueError, \
            "Segment size must be a positive integer less than series length."
    if not series.isdigit():
        raise ValueError, "Series should only contain numbers."
    
    maximum = 0
    mul = lambda x,y: x*y
    for start in xrange(series_length-size+1):
        maximum = max(maximum, \
                      #get product of new segment
                      reduce(mul, map(int, list(series[start:start+size]))))
    return maximum
