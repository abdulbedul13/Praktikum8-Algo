# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:26:39 2021

@author: Abdullah
"""

# ELEMEN KOMPETENSI 1
elkom1 = input("PROGRAM MEMUNCULKAN KARAKTER INDEKS GANJIL\nMasukkan sebuah kata: ")


def indeks_ganjil(huruf):
    list_huruf = []
    for index in range(1, len(huruf), 2):
        list_huruf.append(huruf[index])
    return "".join(list_huruf)


print("Karakter indeks ganjil:", indeks_ganjil(elkom1))
