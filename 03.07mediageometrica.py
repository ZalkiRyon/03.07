import math



def media_geometrica(sueldos):

  producto = 1

  for sueldo in sueldos:

    producto *= sueldo

  media = math.pow(producto, 1/len(sueldos))

  return media



# Ejemplo de uso:

sueldos = [2500, 3000, 2800, 3200, 2700]

resultado = media_geometrica(sueldos)

print(f"La media geométrica de los sueldos es: {resultado:.2f}")