from Paquete.FuncionesCadenas import contarLetra
from Paquete.FuncionesNumericas import multiplicar, potenciar
from Paquete.menu import Menu, gotoxy, cls
import time

class EjerciciosVideos():
    def Presentar(self):
        pass

class HolaMundo(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Hola Mundo', '*' * 14)
        print('Hola mundo')

class Variables(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Variables', '*' * 14)
        nombre = 'Birgner'
        print(nombre)

        edad = 25
        print(edad)

        edad = True
        print(edad)

        sueldo = 205.10
        print(sueldo)
class Converciones(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Converciones', '*' * 14)
        numero1 = '35'
        numero2 = '18'
        print(numero1 + numero2)

        num1 = int(numero1)
        num2 = int(numero2)
        print(num1 + num2)

        sueldo = 1200.43
        sueldoentero = int(sueldo)
        print(sueldoentero)

        valor = 4500.89
        valordecimal = float(valor)
        print(valordecimal)

        edad = 100
        print(len(str(edad)))
class NumerosOperaciones(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Numeros Operaciones', '*' * 14)
        num1 = 20
        num2 = 4

        print('Suma: ', num1 + num2)
        print('Resta: ', num1 - num2)
        print('Multiplicación: ', num1 * num2)
        print('Divición: ', num1 / num2)
        print('Divición Exacta: ', num1 // num2)
        print('Potencia: ', num1 ** num2)
class Concatenacion(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Concatenacion', '*' * 14)
        texto1 = 'Hola'
        texto2 = 'Mundo'
        textoFinal = texto1 + ' ' + texto2
        print(textoFinal)

        print('El saludo es: %s %s' % (texto1, texto2))

        saludoFinal = 'Saludo: {0} {1}'.format(texto1, texto2)
        print(saludoFinal)

        saludoFinal2 = 'Saludo: {y} {x}'.format(x=texto1, y=texto2)
        print(saludoFinal2)
class FuncionCadenas(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Funcion Cadenas', '*' * 14)
        texto = 'Bienvenidos a la tarea de POO'

        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title())  # Comvierte una cadena aun formato de titulo.
        print(texto.find('la'))  # Busca la posicion deonde se encuentra la cade o porcion.
        print(texto.count('e'))  # Cantidad de ocurrencias de una letra o porcion.

        textofinal = texto.replace('e', '3')
        print(textofinal)

        valor = texto.isnumeric()  # Arroja True o False dependiendo si es numerico.
        print(valor)

        cadenaseparada = texto.split(' ')
        print(cadenaseparada)
class Tuplas(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Tuplas', '*' * 14)
        tupla = (1, 2, 3, 4, 5)
        print(tupla)
        tupla2 = (7, 'Oscar', True, 450.1, 16 + 7j, 15, 'Felicidad', False)
        print(tupla2)
        tupla3 = (9, 3, (4, 5, 6))
        print(tupla3)
        print(tupla2[1])
        print(tupla2[-1])
        print(tupla2[0:4])
        print(tupla2[-2])

        a, b, c, d, e = tupla
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)

        tuplafinal = tupla + tupla3
        print(tuplafinal)
class Listas(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Listas', '*' * 14)
        lista1 = ['Oscar', 25, 98.3, True, 'Flavio', 56.3]
        print(lista1)
        print((lista1[:]))
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append('Brigner')
        lista1.insert(4, 'carriel')
        lista1.extend([12, 45])
        print(lista1)

        print(lista1.index('Brigner'))
        lista1.remove('carriel')
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2 = [21, 55, 12]
        lista3 = lista1 + lista2
        print(lista3)

        print(lista2 * 3)

        print('Brigner' in lista1)
class Diccionario(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Diccionario', '*' * 14)
        miDiccionaio = {'España': 'Madrid', 'Pais': 'Ecuador', 'Ecuador': 'Quito'}
        print(miDiccionaio['Ecuador'])

        miDiccionaio['Cantón'] = 'Vinces'
        print(miDiccionaio)

        miDiccionaio['Cantón'] = 'Antonio Sotomayor'
        print(miDiccionaio)

        del miDiccionaio['España']
        print(miDiccionaio)

        dic2 = {'Garcia': 'Oscar', 25: True, 'Sueldo': 150.80}
        print(dic2[25])

        llaves = ('españa', 'francia', 'italia')
        dicpaises = {llaves[0]: 'barcelona', llaves[1]: 'pais', llaves[2]: 'milan'}
        print(dicpaises)

        datospersonales = {'apellido': 'carriel', 'anios': {1: 2011, 2: 2014}}
        print(datospersonales)
        print(datospersonales['anios'])

        print(datospersonales.get('apel', 'oscar'))

        print(datospersonales.keys())
        valores = tuple(datospersonales.values())
        print(valores)
class IngresoDatos(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Ingreso De Datos', '*' * 14)
        nombre = input('Ingresa Tu Nombre: ')
        edad = int(input('Ingresa Tu edad: '))
        sueldo = float(input('Ingrese sueldo: '))
        edadFututura = edad + 20
        print('hola, ' + nombre)
        print('Tu edad es:', edad)
        print('Tu edad es:', sueldo)
        print('Tu edad (dentro de 20 años) será:', edadFututura)
class Ifelse(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'If_Else', '*' * 14)
        edad = int(input('Ingresa su edad: '))
        if edad > 18:
            print('Eres mayor de edad')
        elif edad == 18:
            print('"tienes 18 años!"')
        else:
            print('Eres menor de edad')
class Funciones(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Funciones', '*' * 14)
        def saludar():
            print('Carriel')
            print('Brigner')
            print('BC brigner')
            return 'Hola'

        print(saludar())
class EvaluarsueldoMinimo(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Evaluar Sueldo Minimo', '*' * 14)
        def Presentar(sueldo):
            if sueldo >= 400:
                print('Cumples con el sueldo')
            else:
                print('No cumples con el sueldo minimo')

        Presentar(3400)
class Operadorlodico(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Operador Logico', '*' * 14)
        distancia = 400
        numeroHermanos = 3
        salariospadres = 3500

        tienebeneficio = False

        if (distancia > 1000 and numeroHermanos > 2) or salariospadres < 2000:
            tienebeneficio = True

        print(not tienebeneficio)

        if 5 > 3 and 8 < 5:
            print('Verdad')
        else:
            print('Es mentira...')

        if 5 > 3 or 8 < 5:
            print('Verdad')
        else:
            print('Es mentira...')
class Operadorternario(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Operador Tenario', '*' * 14)
        sexos = ('Hombre', 'Mujer')

        posicion = True

        sexo = sexos[posicion]
        print(sexo)

        sexo = sexos[not posicion]
        print(sexo)
class Range(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Range', '*' * 14)
        numeros = range(5)
        print(numeros[1])

        numeros1 = range(4, 10)
        print(numeros1[5])

        numeros2 = range(10, 100, 8)
        print(numeros2[9])
class For1(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'For', '*' * 14)
        for num in range(1, 13):
            print('Valor actial es: {}'.format(num))

        for i in range(1, 13):
            print('{} X {} = {}'.format(i, i, i * i))
        for nombre in ['Brigner', 'Ariel', 'Cariiel', 'Rodríguez']:
            print('Cantidad de letras de {} es de: {}'.format(nombre, len(nombre)))
class Ifin(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Cursos', '*' * 14)
        print('Matematica', 'Biologia', 'Ingles', 'Ciencias')
        print('*' * 36)
        curso = input('Ingresa un Curso Deseado: ')

        if curso in ('Matematica', 'Biologia', 'Ingles', 'Ciencias'):
            print('Curso "{}" seleccionado.'.format(curso))
        else:
            print('No esiste ese curso...')
class Factorial(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Factorial', '*' * 14)
        numero = int(input('Ingresa un numero: '))
        factorial = 1
        for n in range(1, numero + 1):
            factorial = n * factorial

        print('El factorial del numero {} es {}...'.format(numero, factorial))
class While1(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'While', '*' * 14)
        indice = 1
        # while indice<10:
        #     print('Valor actula: {}'.format(indice))
        #     indice+=1

        inicio = 2
        while inicio <= 100:
            print('El nuemro par: {}'.format(inicio))
            inicio += 2
        print('Hemos terminado el while')
class Breakcontinue(EjerciciosVideos):
    def Presentar(self):
        """for numero in range(1,6):
            if numero==3:
                break
            print('El numero es {}'.format(numero))

        print('Bucle terminado')"""

        """for numero in range(1,6):
            if numero==3:
                continue
            print('El numero es {}'.format(numero))

        print('Bucle terminado')"""

        for numero in range(1, 6):
            if numero == 3:
                pass
            else:
                print('El siguiente valor es mayor a 3')
            print('El numero es {}'.format(numero))

        print('Bucle terminado')

        def funcionDonImplemetar():
            pass

class Generadores(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Generadores', '*' * 14)
        def generaMiltiplos7(limite):
            numero=1
            listaNumeros=[]

            while numero <= limite:
                listaNumeros.append(numero*7)
                numero+=1
            return listaNumeros

        print(generaMiltiplos7(10))

class Generadores2(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Generadosres 2', '*' * 14)
        """def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield leng"""

        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                for letra in leng:
                    yield letra

        LenguajesObtenidos = devuelveLenguajes('Python', 'Java', 'PHP', 'Rudy', 'JavaScript')

        print(next(LenguajesObtenidos))
        print(next(LenguajesObtenidos))
class Excepciones(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Excepciones', '*' * 14)
        numero1 = 20
        numero2 = 5

        """print('La divicion de {} entre {} es: {}'.format(numero1,numero2,numero1/numero2))"""

        try:
            resultado = numero1 / numero2
            print(resultado)
        except ZeroDivisionError:
            print('No se puede dividir 0...')
        finally:
            print('Siempre aparezco')

        print('Aquí termina mi programa.')
class Raise1(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Raise', '*' * 14)
        def evaluNota(nota):
            if nota < 0:
                raise ValueError('No se permiten valores negativos')
            elif nota >= 16:
                print('Exelente')
            elif nota >= 11:
                print('Aprovado')
            else:
                print('Desaprobado')

        evaluNota(-1)

class Modulos(EjerciciosVideos):
    def Presentar(self):
        from Modulos.FuncionesMatematicas import sumar, multiplicar
        print('*' * 14, 'Modulos', '*' * 14)
        print(sumar(6,5))
        print(multiplicar(2,6))

class Paquete(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Paquete', '*' * 14)
        print(multiplicar(5, 6))
        print(potenciar(4, 7))
        print(contarLetra('Brigner Ariel Carriel Rodríguez'))

class Cuenta(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Cuenta', '*' * 14)
        class Cuenta():
            def __init__(self, pro, sal, mon):
                self.__propietario = pro
                self.__saldo = sal
                self.__moneda = mon

            # Getters (Metodos GET)
            def get_Saldo(self):
                return self.__saldo

            def get_Propietario(self):
                return self.__propietario

            def get_Moneda(self):
                return self.__moneda

            # Setters (Metodos SET)
            def set_Moneda(self, moneda):
                self.__moneda = moneda

        cuenta1 = Cuenta('Brigner Carreil', 1300, 'Soles')
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda('dolares')
        print(cuenta1.get_Moneda())

class Curso(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Curso', '*' * 14)
        class Curso():
            def __init__(self, nombre, cre, pro):
                self.nombre = nombre
                self.creditos = cre
                self.profecion = pro
                self.__imparticion = 'Precencial'

            def mostrarDatos(self):
                dat = 'Nombre: {} / Creditos: {} / Modo de Impartición: {} '
                print(dat.format(self.nombre, self.creditos, self.__imparticion))
                docenteAsignado = self.__verificarDocente()
                if docenteAsignado:
                    print('Existe docente asignado.')
                else:
                    print('No es necesario asignar un docente...')

            def __verificarDocente(self):
                # print('Verificando si existe docente asignado...')
                if self.__imparticion == 'Precencial':
                    return True
                else:
                    return False

            def __str__(self):
                texto = 'Nombre: {} - Creditos: {}'
                return texto.format(self.nombre, self.creditos)

        curso1 = Curso('Matematicas', 6, 'Ingeniería de Software')
        print(curso1)
        curso1.mostrarDatos()

class Herencia(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Herencia', '*' * 14)
        class Persona():
            def __init__(self, apellidopat, apellidomat, nombre):
                self.apellidoPatrerno = apellidopat
                self.apellidoMaterno = apellidomat
                self.nombre = nombre

            def mostrarNombreCompleto(self):
                txt = '{} __ {} __ {}'
                return txt.format(self.apellidoPatrerno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())

        class Estudiante(Persona):

            def __init__(self, apellidopat, apellidomat, nombre, pro):
                super().__init__(apellidopat, apellidomat, nombre)
                self.profecion = pro

            def datos(self):
                super().datos()
                print('Profesión: {}'.format(self.profecion))

        # estu1=Estudiante('Carreil','Rodriguez','Brigner','Ingenieria en Software')
        per1 = Persona('Carreil', 'Rodriguez', 'Brigner')
        """print(estu1.mostrarNombreCompleto())
        print(estu1.profecion)"""
        # estu1.datos()
        print(isinstance(per1, Estudiante))

class HerenciaMultiple(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Herencia Multiple', '*' * 14)
        class ClaseA():
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2

        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5

        class ClaseX(ClaseA, ClaseB):
            pass

        cx1 = ClaseX(12, 14)

class Persona(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Persona', '*' * 14)
        class Persona():
            apellido = ''
            nombres = ''
            edad = 0
            despierta = False

            def despertar(self):
                self.despierta = True
                print('Buen día..')

        persona1 = Persona()
        persona1.apellido = 'Carriel Rodriguez'
        print(persona1.apellido)
        persona1.despertar()
        print(persona1.despierta)
        print()
        persona2 = Persona()
        persona2.apellido = 'Carriel Rodriguez'
        print(persona2.apellido)

        print(persona2.despierta)

class Polimorfismo(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Polimorfismo', '*' * 14)
        class Estudiante():
            def describir(self):
                print('Soy un buen estiante')

        class Docente():
            def describir(self):
                print('Me dedico a enseñar cursos')

        class Trabajador():
            def describir(self):
                print('Trabajo dentro de una gran empresa.')

        def describirPersona(persona):
            persona.describir()

        doc1 = Trabajador()
        describirPersona(doc1)

class RelacionesClases(EjerciciosVideos):
    def Presentar(self):
        print('*' * 14, 'Relaciones De Clases', '*' * 14)
        class Pais:
            def __init__(self,nom, pre):
                self.nombre=nom
                self.presidente=pre
            def __str__(self):
                txt='Pais: {} - Presidente: {}'
                return txt.format(self.nombre,self.presidente)
        class Cuidad:
            def __init__(self,nom,hab,pai):
                self.nombre=nom
                self.habitantes=hab
                self.pais=pai

            def __str__(self):
                txt='Cuidad {} - N° Habitantes: {} ({})'
                return txt.format(self.nombre,self.habitantes,self.pais)
        class Urbanizacion:
            def __init__(self,nom,ciu):
                self.nombre=nom
                self.ciudad=ciu

            def __str__(self):
                txt='Urbanizacion: {} ({})'
                return txt.format(self.nombre,self.ciudad)

        pais1=Pais('Ecuador','Brigner')
        print(pais1)
        cuidad1=Cuidad('Vinces',123000,pais1)
        print(cuidad1)
        urba1=Urbanizacion('Antonio Sotomayor',cuidad1)
        print(urba1)





menu1=Menu()
ejercicio1=HolaMundo()
ejercicio2=Variables()
ejercicio3=Converciones()
ejercicio4=NumerosOperaciones()
ejercicio5=Concatenacion()
ejercicio6=FuncionCadenas()
ejercicio7=Tuplas()
ejercicio8=Listas()
ejercicio9=Diccionario()
ejercicio10=IngresoDatos()
ejercicio11=Ifelse()
ejercicio12=Funciones()
ejercicio13=Operadorlodico()
ejercicio14=Operadorternario()
ejercicio15=Range()
ejercicio16=For1()
ejercicio17=Factorial()
ejercicio18=While1()
ejercicio19=Breakcontinue()
ejercicio20=Generadores()
ejercicio21=Generadores2()
ejercicio22=Excepciones()
ejercicio23=Raise1()
ejercicio24=Modulos()
ejercicio25=Paquete()
ejercicio26=Cuenta()
ejercicio27=Curso()
ejercicio28=Herencia()
ejercicio29=HerenciaMultiple()
ejercicio30=Persona()
ejercicio31=Polimorfismo()
ejercicio32=RelacionesClases()


opciones=['Hola mundo','Variables', 'Converciones','NumerosOperaciones','Concatenacion','Funcion Cadenas','Tuplas','Listas',
          'Diccionario','IngresoDatos','Ifelse','Funciones','Operador Lodico','Operador Ternario','Range',
          'For','Factorial','While1','Breakcontinue','Generadores 1','Generadores 2','Excepciones','Raise1','Modulos','Paquete','Clase Cuenta',
          'Clase Curso','Herencia','HerenciaMultiple','Clase Persona','Polimorfismo','Relaciones Clases']


def Execute(Objeto):
    Objeto.Presentar()

Listaopciones = [ejercicio1, ejercicio2, ejercicio3,ejercicio4,ejercicio5,ejercicio6,ejercicio7,ejercicio8,ejercicio9,
                ejercicio10,ejercicio11,ejercicio12,ejercicio13,ejercicio14,ejercicio15,ejercicio16,ejercicio17,
                ejercicio18,ejercicio19,ejercicio20,ejercicio21,ejercicio22,ejercicio23,ejercicio24,ejercicio25,ejercicio26,
                ejercicio27,ejercicio28,ejercicio29,ejercicio30,ejercicio31,ejercicio32]

ban = True
while ban:
    cls()
    opcion = int(menu1.menu(opciones, "Menú"))
    if opcion in range(0,33):
        cls()
        gotoxy(1,3);Execute(Listaopciones[opcion-1])
    else:
        print("No existe tal opción...")

    if ban:
        resp = input("\nPresiona enter para volver")
        if resp.lower() == "n":
            ban = False
            cls()
            print("Saliendo del programa...");time.sleep(1)