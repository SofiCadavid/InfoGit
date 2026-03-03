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