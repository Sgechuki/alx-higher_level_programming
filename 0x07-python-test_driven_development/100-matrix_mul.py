#!/usr/bin/python3
"""
    This module has matrix_mul function that  multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif not all(isinstance(lst, list) for lst in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(isinstance(lst, list) for lst in m_b):
        raise TypeError("m_b must be a list of lists")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif not all(isinstance(i, (int, float)) for lst in m_a for i in lst):
        raise TypeError("m_a should contain only integers or floats")
    elif not all(isinstance(i, (int, float)) for lst in m_b for i in lst):
        raise TypeError("m_b should contain only integers or floats")
    elif not all(len(m_a[0]) == len(lst) for lst in m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not all(len(m_b[0]) == len(lst) for lst in m_b):
        raise TypeError("each row of m_b must be of the same size")
    elif len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    else:
        res = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    res[i][j] += m_a[i][k] * m_b[k][j]
    return res
