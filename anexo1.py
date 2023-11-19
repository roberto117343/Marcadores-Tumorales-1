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

    y = 1.0/(1.0 + pow(math.e, -k * (x - x_o)))
    return y


kEncontrada = 0.0

valorDiscriminante = float(input("Introduce el valor discriminante: "))
limiteSuperiorReferencia = float(input("Introduce el límite superior de referencia: "))

k = 0.0
x_o = ((limiteSuperiorReferencia + valorDiscriminante)/2.0)

while k <= 50.0:

    try:

        alto = funcion_logistica(valorDiscriminante, k, x_o)
        bajo = funcion_logistica(limiteSuperiorReferencia, k, x_o)

        if 0.99 < alto < 1.0 and 0.00 < bajo < 0.01:

            kEncontrada = k

            break

    except:

        break

    k += 0.001

print("\nfmt(x) = 1/(1+e^(-" + str(round(kEncontrada, 3)) +
      "(x -", str(round(x_o, 3)) + ")))")

print("\nk = " + str(round(kEncontrada, 3)))
print("x0 = " + str(round(x_o, 3)))
