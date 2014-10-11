#a1test.py
#Haewon Hwang (hh474) and Otto Godwin (oag9)
#September 25, 2013

"""Unit test for module a1

When run as a script, this module invokes several 
procedures that test the various functions in the module 
a1."""

import cornelltest
from a1 import *


def testA():
    """testA() tests the functions before_space(s) and after_space(s) in module a1.py"""

    #test before_space(s)
    s='hello world'
    result = before_space(s)
    cornelltest.assert_equals('hello', result)

    s='hello      world'
    result = before_space(s)
    cornelltest.assert_equals('hello', result)

    s='helloworld  '
    result = before_space(s)
    cornelltest.assert_equals('helloworld', result)

    s='hello world   '
    result = before_space(s)
    cornelltest.assert_equals('hello', result)

    s=' hello world'
    result= before_space(s)
    cornelltest.assert_equals('', result)

    s='  hello world'
    result = before_space(s)
    cornelltest.assert_equals('', result)

    #test after_space(s)
    s='hello world'
    result = after_space(s)
    cornelltest.assert_equals('world', result)

    s='hello      world'
    result = after_space(s)
    cornelltest.assert_equals('     world', result)

    s='helloworld  '
    result = after_space(s)
    cornelltest.assert_equals(' ', result)

    s='hello world   '
    result = after_space(s)
    cornelltest.assert_equals('world   ', result)

    s=' hello world'
    result= after_space(s)
    cornelltest.assert_equals('hello world', result)

    s='  hello world'
    result = after_space(s)
    cornelltest.assert_equals(' hello world', result)


def testB():
    """testB() tests the functions first_inside_quotes(s), get_lhs(query),
    get_rhs(query), and get_error(query) in module a1.py"""

    #test first_inside_quotes(s)
    s = 'A "B C" D'
    result = first_inside_quotes(s)
    cornelltest.assert_equals('B C', result)

    s = 'A "B C" D "E F"'
    result = first_inside_quotes(s)
    cornelltest.assert_equals('B C', result)

    s = '""'
    result = first_inside_quotes(s)
    cornelltest.assert_equals('', result)

    s = 'the teacher said "hello!!!!!" to the students'
    result = first_inside_quotes(s)
    cornelltest.assert_equals('hello!!!!!', result)

    #test get_lhs(query)
    query = '{lhs: "5 U.S. dollars",rhs: "18.3650007 United Arab Emirates dirhams",error: "",icc: true}'
    result = get_lhs(query)
    cornelltest.assert_equals('5 U.S. dollars', result)

    query = '{lhs: "",rhs: "",error: "4",icc: false}'
    result = get_lhs(query)
    cornelltest.assert_equals('', result)

    #test get_rhs(query)
    query = '{lhs: "5 U.S. dollars",rhs: "18.3650007 United Arab Emirates dirhams",error: "",icc: true}'
    result = get_rhs(query)
    cornelltest.assert_equals('18.3650007 United Arab Emirates dirhams', result)

    query = '{lhs: "",rhs: "",error: "4",icc: false}'
    result = get_lhs(query)
    cornelltest.assert_equals('', result)

    #test get_error(query)
    query='{lhs: "5 U.S. dollars",rhs: "18.3650007 United Arab Emirates dirhams",error: "",icc: true}'
    result = get_error(query)
    cornelltest.assert_equals('', result)

    query = '{lhs: "",rhs: "",error: "4",icc: false}'
    result = get_error(query)
    cornelltest.assert_equals('4', result)


def testC():
    """testC() tests the function
    currency_response(amount_from, currency_from, currency_to) in module a1.py"""

    amount_from = 5.0
    currency_from = 'USD'
    currency_to = 'EUR'
    result = currency_response(amount_from, currency_from, currency_to)
    cornelltest.assert_equals('{lhs: "5 U.S. dollars",rhs: "3.77216145 Euros",error: "",icc: true}', result)

    amount_from = -5.0
    currency_from = 'USD'
    currency_to = 'EUR'
    result = currency_response(amount_from, currency_from, currency_to)
    cornelltest.assert_equals('{lhs: "-5 U.S. dollars",rhs: "-3.77216145 Euros",error: "",icc: true}', result)

    amount_from = 'hello'
    currency_from = 'USD'
    currency_to = 'EUR'
    result = currency_response(amount_from, currency_from, currency_to)
    cornelltest.assert_equals('{lhs: "",rhs: "",error: "4",icc: false}', result)

    amount_from = 5.0
    currency_from = 'US'
    currency_to = 'EUR'
    result = currency_response(amount_from, currency_from, currency_to)
    cornelltest.assert_equals('{lhs: "",rhs: "",error: "4",icc: false}', result)

    amount_from = 5.0
    currency_from = 'USD'
    currency_to = 'EU'
    result = currency_response(amount_from, currency_from, currency_to)
    cornelltest.assert_equals('{lhs: "",rhs: "",error: "4",icc: false}', result)


def testD():
    """testD() tests the functions iscurrency(currency) and
    exchange(amount_from, currency_from, currency_to) in module a1.py"""

    #test iscurrency(currency)
    currency = 'USD'
    result = iscurrency(currency)
    cornelltest.assert_equals(True, result)

    currency = 'US'
    result = iscurrency(currency)
    cornelltest.assert_equals(False, result)

    #test exchange(amount_from, currency_from, currency_to)
    amount_from = 5.0
    currency_from = 'USD'
    currency_to = 'EUR'
    result = exchange(amount_from, currency_from, currency_to)
    cornelltest.assert_floats_equal(3.77216145, result)

    amount_from = -5.0
    currency_from = 'KRW'
    currency_to = 'USD'
    result = exchange(amount_from, currency_from, currency_to)
    cornelltest.assert_floats_equal(-0.004609999993546, result)

    amount_from = 576.5
    currency_from = 'TRY'
    currency_to = 'KRW'
    result = exchange(amount_from, currency_from, currency_to)
    cornelltest.assert_floats_equal(308288.69086087, result)


if __name__ == '__main__':
    testA()
    testB()
    testC()
    testD()
    print "Module a1 is working correctly"