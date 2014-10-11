#a1.py
#Haewon Hwang (hh474) and Otto Godwin (oag9)
#September 25, 2013

import urllib2

"""Module for currency exchange

This module provides several string parsing functions to 
implement a simple currency exchange routine using an 
online currency service. The primary function in this 
module is exchange()."""

def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space

    Precondition: s has at least one space in it"""

    return s[:s.index(' ')]


def after_space(s):
    """Returns: Substring of s after the first space

    Precondition: s has at least one space in it"""

    return  s[s.index(' ')+1:]


def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters.

    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to use a double
    quote character (") inside of it.

    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' because
    it only picks the first such substring.

    Precondition: s is a string with at least two (double) quote characters inside."""

    a = s.index('"')+1
    b = s.index('"', s.index('"')+1)
    return s[a:b]


def get_lhs(query):
    """Returns: The LHS value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside double
    quotes (") immediately following the keyword lhs. For example, if the JSON is
    '{lhs: "2 U.S. dollars",rhs: "1.629327902 Euros",error: "",icc: true}'
    then this function returns '2 U.S. dollars' (not '"2 U.S. dollars"'). It returns
    the empty string if the JSON is the result of on invalid query.

    Precondition: query is the response to a currency query"""

    return first_inside_quotes(query)


def get_rhs(query):
    """Returns: The RHS value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside double
    quotes (") immediately following the keyword rhs. For example, if the JSON is
    '{lhs: "2 U.S. dollars",rhs: "1.629327902 Euros",error: "",icc: true}'
    then this function returns "1.629327902 Euros" (not '"1.629327902 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.

    Precondition: query is the response to a currency query"""

    a = query.index('rhs: "')+6
    b = query.index('",error')
    return query[a:b]


def get_error(query):
    """Returns: The error value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string
    inside quotes (") immediately following the keyword error. For example,
    if the JSON string is '{lhs: "",rhs: "",error: "4",icc: false}'
    then this function returns '4' (not '"4"' or the number 4). The returned
    string will be non-empty if a currency-conversion error occurred
    (e.g. if invalid currency keywords were supplied in the query).
    It returns the empty string if the JSON string is the result of a valid query.
    
    Precondition: query is the response to a currency query"""

    a = query.index('error: "')+8
    b = query.index('",icc')
    return query[a:b]


def currency_response(amount_from, currency_from, currency_to):
    """Returns: A JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form
    '{lhs: "<old-amount>",rhs: "<new-amount>",error: "",icc: true}' where the values
    old-amount and new-amount contain the value and name for the original
    and new currencies. If the query is invalid, both old-amount and new-amount
    will be empty.

    Precondition: amount_from is of type float, while currency_from and
    currency_to are of type string"""

    str_amount = str(amount_from)
    prefix = 'http://cs1110.cs.cornell.edu/a1/calculator.php?q='
    url=urllib2.urlopen(prefix + str_amount + currency_from + '=?' + currency_to)
    return url.read()


def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency.
    It returns False otherwise.

    Precondition: currency is a string."""

    x = get_error(currency_response(5.0, currency, currency))
    return (x=='')


def exchange(amount_from, currency_from, currency_to):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to.
    The value returned represents the amount in currency currencyTo.
    The value returned has type float.

    Precondition: amount_from is a float. Both currency_from and currency_to
    are strings with valid three-letter currency codes."""

    json = currency_response(amount_from, currency_from, currency_to)
    rhs = get_rhs(json)
    return float(before_space(rhs))