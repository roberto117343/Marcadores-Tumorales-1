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

        return round(probabilidad_MTA, 3)

    elif marcador == 2:

        #Calculos MTB

        probabilidad_MTB = funcion_logistica(valor, 0.02, 268.5)

        return round(probabilidad_MTB, 3)


    elif marcador == 3:

        #Calculos MTC

        probabilidad_MTC = funcion_logistica(valor, 0.132, 65.0)

        return round(probabilidad_MTC, 3)


print("Selecciona marcador: \n")
valor_menu = input("1. MTA\n2. MTB\n3. MTC\n\n")

valor_concentracion = input("\nIntroduce el valor de la concentración del marcador tumoral:"
                            "\n\n")

print("\nLa probabilidad de sospecha es: ",
      funcion_probabilidades(int(valor_menu), float(valor_concentracion)))
