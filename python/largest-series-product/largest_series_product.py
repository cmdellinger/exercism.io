"""
Exercism.io assignment: largest_series_product.py
written by (GitHub):    cmdellinger
Python version:         2.7

Given a string of digits, calculate the largest product for a contiguous
substring of digits of length n.
    
See README for additional problem constraints.
"""

def largest_product(series, size):
    """ Returns largest product for segments of given size in provided series.
        
    Args:
        series (string): string containing all digits for the series without
            any delimiters.
        size (int): the length of the segment to take a product of.
    Returns:
        The maximum product of given size contained in the series.
    """
    # validate inputs
    if not size: return 1
    if size > len(series) or size < 0:
        raise ValueError, \
              "Segment size must be a positive integer less than series length."
    if not series.isdigit():
        raise ValueError, "Series should only contain numbers."
    # convert series to list of int's
    series = map(int, list(series))
    # find maximum product of all segments
    mul = lambda x,y: x*y
    return max(reduce(mul, series[i:i+size]) for i in xrange(len(series)-size+1))
