"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Lani Ogunkolade

    The funcƟon should return the converted amount as a floaƟng-point number, rounded to two
    decimal point precision using Python's round() funcƟon.

 If the input amount is negaƟve, the funcƟon should return 0.0. Done
 You do not need to handle cases where non-numeric values are passed in. Done
 You do not need to handle cases for undefined currency codes. Done
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    currencies = [key for key in conversion_rate.keys()]
    
    if (from_currency not in currencies) & (to_currency not in currencies):
        return None
    
    if amount <=0:
        return 0.0
    
    try:
        float(amount)
    except ValueError:
        return None

    from_var = amount*conversion_rate[from_currency][to_currency]
    return (from_var)



    return None
