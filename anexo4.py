#* «Copyright 2023 Roberto Reinosa Fernández»
#*
#* This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#*

import math


def funcion_logistica(x, k, x_o):

    y = 1.0/(1.0 + pow(math.e, -k*(x - x_o)))
    return y


def funcion_probabilidades(marcador, valor):

    if marcador == 1:

        #Calculos MTA

        probabilidad_MTA = funcion_logistica(valor, 1.022, 10.5)

        return probabilidad_MTA

    elif marcador == 2:

        #Calculos MTB

        probabilidad_MTB = funcion_logistica(valor, 0.02, 268.5)

        return probabilidad_MTB


    elif marcador == 3:

        #Calculos MTC

        probabilidad_MTC = funcion_logistica(valor, 0.132, 65.0)

        return probabilidad_MTC


def probabilidad_combinada(lista_valores):

    producto = 1.0

    for i in range(0, len(lista_valores)):

        producto *= 1.0 - float(lista_valores[i])

    return 1.0 - producto


MTA = float(input("Introduce la concentración de MTA: "))
MTB = float(input("Introduce la concentración de MTB: "))
MTC = float(input("Introduce la concentración de MTC: "))

print("\nProbabilidades Individuales: MTA = " + str(round(funcion_probabilidades(1, MTA), 3))
      + ", MTB = " + str(round(funcion_probabilidades(2, MTB), 3))
      + ", MTC = " + str(round(funcion_probabilidades(3, MTC), 3)), "\n")

lista_probabilidades_individuales = []

lista_probabilidades_individuales.append(funcion_probabilidades(1, MTA))
lista_probabilidades_individuales.append(funcion_probabilidades(2, MTB))
lista_probabilidades_individuales.append(funcion_probabilidades(3, MTC))

print("Probabilidad combinada =",
      probabilidad_combinada(lista_probabilidades_individuales))
