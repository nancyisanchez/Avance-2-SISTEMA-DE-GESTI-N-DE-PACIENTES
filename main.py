# Sistema para registrar pacientes y consultar sus datos.
# Se aplican conceptos de Programación Orientada a Objetos como:
# - Encapsulamiento
# - Herencia
# - Polimorfismo
# --------------------------------------------------


# --------------------------------------------------
# CREACIÓN DE LA CLASE BASE
# --------------------------------------------------
class Paciente:

    def __init__(self, nombre, edad, diagnostico, presion_arterial):
        self.nombre = nombre
        self.edad = edad
        self.diagnostico = diagnostico

        # Aplicación de Encapsulamiento
        self.__presion_arterial = presion_arterial

    # Getter para consultar el atributo privado
    def get_presion_arterial(self):
        return self.__presion_arterial

    # Setter para modificar el atributo privado
    def set_presion_arterial(self, nueva_presion):
        if nueva_presion != "":
            self.__presion_arterial = nueva_presion
        else:
            print("Error: la presión arterial no puede estar vacía.")

    # Método 1
    def mostrar_nombre(self):
        print(f"Nombre: {self.nombre}")

    # Método 2
    def mostrar_edad(self):
        print(f"Edad: {self.edad} años")

    # Método 3
    def mostrar_diagnostico(self):
        print(f"Diagnóstico: {self.diagnostico}")

    # Método 4
    def mostrar_presion_arterial(self):
        print(f"Presión arterial: {self.__presion_arterial} mmHg")


# --------------------------------------------------
# CREACIÓN DE LA SUBCLASE
# APLICACIÓN DE HERENCIA Y SUPER()
# --------------------------------------------------
class PacienteHospitalizado(Paciente):

    def __init__(self, nombre, edad, diagnostico,
                 presion_arterial, habitacion, dias_internado):

        # Uso de super() y Herencia
        super().__init__(
            nombre,
            edad,
            diagnostico,
            presion_arterial
        )

        # Nuevos atributos de la subclase
        self.habitacion = habitacion
        self.dias_internado = dias_internado

    # Método propio de la subclase
    def mostrar_hospitalizacion(self):
        print(
            f"Habitación: {self.habitacion} | "
            f"Días internado: {self.dias_internado}"
        )

    # Sobrescritura de métodos (Polimorfismo)
    def mostrar_diagnostico(self):
        print(
            f"Diagnóstico: {self.diagnostico} | "
            f"Habitación: {self.habitacion} | "
            f"Días internado: {self.dias_internado}"
        )


# --------------------------------------------------
# INSTANCIACIÓN Y PRUEBAS
# --------------------------------------------------

# Objeto de la clase base
paciente1 = Paciente(
    "Graciela",
    60,
    "Hepatitis",
    "110/70"
)

# Objetos de la subclase
paciente2 = PacienteHospitalizado(
    "Alejandro",
    47,
    "Hipertension",
    "140/90",
    "201A",
    5
)

paciente3 = PacienteHospitalizado(
    "Monserrat",
    46,
    "Diabetes",
    "120/80",
    "305B",
    3
)

# --------------------------------------
# PRUEBA DEL OBJETO 1
# --------------------------------------
print("PACIENTE 1")
paciente1.mostrar_nombre()
paciente1.mostrar_edad()
paciente1.mostrar_diagnostico()
paciente1.mostrar_presion_arterial()

print("\n" + "-" * 40)

# --------------------------------------
# PRUEBA DEL OBJETO 2
# --------------------------------------
print("PACIENTE 2")
paciente2.mostrar_nombre()
paciente2.mostrar_edad()
paciente2.mostrar_diagnostico()
paciente2.mostrar_presion_arterial()
paciente2.mostrar_hospitalizacion()

print("\n" + "-" * 40)

# --------------------------------------
# PRUEBA DEL OBJETO 3
# --------------------------------------
print("PACIENTE 3")
paciente3.mostrar_nombre()
paciente3.mostrar_edad()
paciente3.mostrar_diagnostico()
paciente3.mostrar_presion_arterial()
paciente3.mostrar_hospitalizacion()

print("\n" + "-" * 40)

# --------------------------------------
# DEMOSTRACIÓN DEL ENCAPSULAMIENTO
# --------------------------------------
print("PRUEBA DE GETTER Y SETTER")

print(
    f"Presión original: "
    f"{paciente1.get_presion_arterial()}"
)

paciente1.set_presion_arterial("115/75")

print(
    f"Nueva presión: "
    f"{paciente1.get_presion_arterial()}"
)
