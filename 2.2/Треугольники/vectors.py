#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:25:31 2022

@author: user
"""


import math


def add(a: list, b: list) -> list:
    """Сложение векторов"""
    return [x+y for x, y in zip(a, b)]


def sub(a: list, b: list) -> list:
    """Вычитание векторов"""
    return [x-y for x, y in zip(a, b)]


def scalar_product(vec: list, scal: int) -> list:
    """Умножение вектора на скаляр"""
    return [x*scal for x in vec]


def dot_product(a: list, b: list) -> float:
    """Скалярное произведение"""
    return sum([x*y for x, y in zip(a, b)])


def is_collinear(a: list, b: list) -> bool:
    """Проверка на колинеарность"""
    flag = True
    if a[0] == 0 or b[0] == 0:
        flag = False
    else:
        k = a[0]/b[0]
        for i in range(1, len(a)):
            if a[i] == 0 or b[i] == 0:
                flag = False
                break
            if a[i]/b[i] != k:
                flag = False
                break
    return flag


def vector_lenght(vector: list) -> float:
    """Вычисление длинны вектора"""
    output = 0
    for cord in vector:
        output += math.pow(cord, 2)
    return math.sqrt(output)


def is_vectors_equal(a: list, b: list) -> bool:
    """Равны ли вектора"""
    flag = True
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
    return flag


def koef_collinearity(a: list, b: list) -> float:
    """Вычесление коэфицента ортогональности"""
    if is_collinear(a, b):
        return a[0]/b[0]
    else:
        return 0.0


def cos_of_vectors(a: list, b: list) -> float:
    """Вычесление коссинуса угла между двумя векторами"""
    return dot_product(a, b)/(vector_lenght(a)*vector_lenght(b))


def angle_of_vectors(a: list, b: list) -> float:
    """Вычисление угла между двумя векторами (в градусах)"""
    return math.acos(cos_of_vectors(a, b))*57.29577951308


def vector_normalize(vector: list):
    """Нормализация вектора"""
    return scalar_product(vector, 1/vector_lenght(vector))


def vector_projection(a: list, b: list) -> float:
    """Проекция вектора а на b"""
    return dot_product(a, b) / vector_lenght(b)


def printing_res(c, message: str = "&&?"):
    print(message, c)
