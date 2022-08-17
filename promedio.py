import diccionario

def promedio_notas():

  print('----------------------------------------')
  print('***********PROMEDIO DE NOTAS************')
  print('Ingrese las notas del alumno selecionado')
  print('----------------------------------------')

  acum_notas = []
  resultado = 0
  nota = 0
  suma = 0

  while True:
    try:
      nota = int(input('ingrese la nota: '))
      print('la nota es: ', nota, '\n')

      if nota < 10 or nota > 71:
        print('>> ERROR: la nota debe ser entre 10 y 70')
        continue

      if nota >= 10 or nota <= 70:
        acum_notas.append(nota)
        suma = suma + nota
        resultado = suma / len(acum_notas)

      if len(acum_notas) == 4:
        print('---------------------------------------------')
        print('\n*********** PROMEDIO DE NOTA **************')
        print('Acumulacion de notas: ', acum_notas), '\n'
        diccionario.resultado = resultado
        diccionario.acum_notas_alumno = acum_notas
        return print('El promedio de notas es: ', resultado)
        
    except ValueError:
      print('>> ERROR: Debe ingresar un numero')

