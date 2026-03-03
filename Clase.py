
#Ejercicio Versión 1
class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre

    def verServicio(self):
        return self.__servicio

    def verGenero(self):
        return self.__genero

    def verCedula(self):
        return self.__cedula

    def asignarNombre(self, n):
        self.__nombre = n

    def asignarServicio(self, s):
        self.__servicio = s

    def asignarGenero(self, g):
        self.__genero = g

    def asignarCedula(self, c):
        self.__cedula = c


class Sistema:
    def __init__(self):
        # como voy a tener uno o muchos pacientes los manejare en una lista
        self.__lista_pacientes = []
        # esta variable siempre dependera del tamanio de la lista por lo
        # que no se podra modificar con un metodo asignar
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self):
        # 1 solicito los datos por teclado
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")
        # 2 creo el objeto Paciente y le asigno los datos
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        # 3 guardo el paciente en la lista
        self.__lista_pacientes.append(p)
        # 4 actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes

    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cedula a buscar: "))
        # cedula in self.__lista_pacientes: no sirve porque en la lista
        # hay Pacientes no numeros:
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                # si coincide la cedula del paciente con la buscada
                # muestro los datos
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())

    def salir(self):
        print("Hasta luego!")


# cuando creamos las clases podemos generar objetos de esas clases y con esos objetos
# acceder a las funcionalidades o metodos
mi_sistema = Sistema()  # Se Crea una instancia de la clase Sistema.

# ciclo infinito
while True:
    opcion = int(input("1. nuevo paciente - 2. Numero de Pacientes - 3. Datos Paciente - 4. Salir: "))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion == 2:
        print("Ahora hay : " + str(mi_sistema.verNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        mi_sistema.salir()
        break
    else:
        print("Opcion invalida")

#Ejercicio Versión 2
class Sistema:
    def __init__(self):
        self.__lista_pacientes = []

    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)

    def verDatosPaciente(self, c):
        # voy a buscar paciente por paciente
        for p in self.__lista_pacientes:
            # por cada paciente de la lista, le digo al paciente que me
            # retorne la cedula y la comparo con la ingresada por teclado
            if c == p.verCedula():
                return p  # si encuentro el paciente lo retorno

    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")


def main():
    sis = Sistema()
    # probemos lo que llevamos programado
    while True:
        # TAREA HACER EL MENU
        opcion = int(input("Ingrese 0 para salir, 1 para ingresar nuevo paciente, 2 ver Paciente: "))

        if opcion == 1:
            # ingreso pacientes
            print("A continuacion se solicitaran los datos ...")
            # 1. Se solicitan los datos
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")

            # 2. se crea un objeto Paciente
            pac = Paciente()

            # como el paciente esta vacio debo ingresarle la informacion
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarNombre(nombre)
            pac.asignarServicio(servicio)

            # 3. se almacena en la lista que esta dentro de la clase sistema
            sis.ingresarPaciente(pac)

        elif opcion == 2:
            # 1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: "))

            # le pido al sistema que me devuelva en la variable p al paciente que tenga
            # la cedula c en la lista
            p = sis.verDatosPaciente(c)

            # 2. si encuentro al paciente imprimo los datos
            print("Nombre: " + p.verNombre())
            print("Cedula: " + str(p.verCedula()))
            print("Genero: " + p.verGenero())
            print("Servicio: " + p.verServicio())

        elif opcion != 0:
            continue
        else:
            break



# aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main()