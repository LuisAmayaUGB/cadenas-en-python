recibo = '''Venta CV202005260456
Date: 26-05-2020
Artículo: Tornillos 35x6 100 unidades
Precio: 0.55 euros
Artículo: Tacos de metal 8x46 20 unidades
Precio: 2.46 euros
Artículo: Lubricante de maquinaria
Precio: 13.80 euros
Pago realizado
Total: 16.81 euros'''


#la manera de conocer el número de articulos es contar el número de
#apariciones de la palabra artículo antes de eliminarla del recibo

#necesitamos una variable para guardar el número de artículos
numero_articulos = recibo.count('Artículo')

#hay que extraer el código de venta, guardarlo y eliminarlo de su sitio
#sabemos que tiene 14 caracteres y que empieza en la posición 6
#(5 de la palabra Venta + 1 del espacio entre Venta y el código
codigo_venta = recibo[6:20]
recibo_formateado = recibo.replace(codigo_venta, '')

#reemplazamos Venta por VENTA con un salto de línea \n, la línea de asteriscos
#y un salto de línea más
recibo_formateado = recibo_formateado.replace('Venta', 'VENTA\n*****\n')

#corregirmos la palabra Date
recibo_formateado = recibo_formateado.replace('Date', 'Fecha')

#sustituimos la subcadena "Artículo: " por un salto de línea
#para dejar el espacio correspondiente entre un artículo y otr
recibo_formateado = recibo_formateado.replace('Artículo: ', '\n')

#eliminamos la subcadena "Precio: "
recibo_formateado = recibo_formateado.replace('Precio: ', '')

#sustituimos los puntos por comas, los guiones por barras
#y la palabra "euros" por "EUR".
recibo_formateado = recibo_formateado.replace('.', ',')
recibo_formateado = recibo_formateado.replace('-', '/')
recibo_formateado = recibo_formateado.replace('euros', 'EUR')

#eliminamos la subcadena Pago realizado.
recibo_formateado = recibo_formateado.replace('Pago realizado', '')

#generamos la subcadena  del número de articulos
subcadena_numero_articulos = 'Número de artículos: ' + str(numero_articulos)

#sustituimos la palabra "Total" por la subcadena del número de artículo,
#un salto de línea y la palabra TOTAL
recibo_formateado = recibo_formateado.replace('Total', subcadena_numero_articulos + '\nTOTAL')

#añadimos finalmente el código de venta al recibo
recibo_formateado = recibo_formateado + '\n' + codigo_venta

print(recibo_formateado)
