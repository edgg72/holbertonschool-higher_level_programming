#!/usr/bin/python3
import hidden_4
lista = dir(hidden_4)
for i in lista:
    if i[0] != '_':
        print(i)
