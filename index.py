import diccionario
import promedio

def alumnos():

  while True:
    print('-----------------------------------------------------------------')
    print('*************** PROGRAMA DE EVALUACION DE NOTAS ****************')
    print('                 SELECCIONE EL CURSO A EVALUAR                 \n')
    print(
      '[1]', diccionario.name_cursos[0],
      '[2]', diccionario.name_cursos[1],
      '[3]', diccionario.name_cursos[2]
    )
    print('-----------------------------------------------------------------')
    
    try:
      select_curso = int(input('ingrese curso para evaluar: '))
      select_curso = select_curso - 1

      if select_curso < 0 or select_curso > 2:
        print('>> ERROR: escriba una opcion valida \n')
        continue
      
      lista_curso = diccionario.cursos[select_curso]
      break

    except ValueError:
      print('>> ERROR: Debe elegir una opcion valida \n')

  while True:
    print('\n-----------------------------------------------')
    print('********SELECCIONE EL NOMBRE EL ALUMNO*********\n')
    for al in range(len(lista_curso)):
      print('[', al + 1 ,']' , 'para evaluar a: ' , lista_curso[al]['name'])
    print('-----------------------------------------------')

    try:  
      select_alumno = int(input('ingrese la opcion del nombre para evaluar: '))
      select_alumno = select_alumno -1

      if select_alumno >= len(lista_curso) or select_alumno < 0:
        print('>> ERROR: Escriba una opcion valida \n')
        continue
      
      print('Alumno:', lista_curso[select_alumno]['name'],'\n')
      promedio.promedio_notas()
      diccionario.cursos[select_curso][select_alumno]['nota_final'] = diccionario.resultado
      diccionario.cursos[select_curso][select_alumno]['notas'] = diccionario.acum_notas_alumno
      print('RESUMEN DEL ALUMNO: ',diccionario.cursos[select_curso][select_alumno])
      break
    
    except ValueError:
      print('>> ERROR: Debe elegir una opcion valida')

alumnos()
