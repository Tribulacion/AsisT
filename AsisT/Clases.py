import datetime
from tkinter import messagebox


class Persona:
    """
    Clase Persona, define los atributos basicos de las personas

    :argument
        ID_persona: int,
        Nombre: str,
        Apellidos: str,
        Edad: str,
        Numero_telefono: str,
        Correo: str,
        Domicilio: str,
        Puesto: str,
        Sueldo: float,
    """
    _numero_personas = 0

    @classmethod
    def aumentar_persona(cls):
        cls._numero_personas += 1
        return cls._numero_personas

    def __init__(self, nombre="", apellido_p="", apellido_m="", edad=0, n_telefono="",
                 correo="", domicilio="", puesto="", sueldo=0.0):
        # Validación básica del correo electrónico
        if correo and ("@" not in correo or "." not in correo):
            messagebox.showerror("Error de Correo!", f'Correo inválido')
            raise ValueError("Dirección de correo electrónico inválida")

        self._id_persona = self.aumentar_persona()
        self._nombre = nombre

        if sueldo < 0:
            messagebox.showerror('Error de Sueldo!', f'El sueldo de {self.nombre} no puede ser menor a 0!')
            raise ValueError('Sueldo menor a 0.')

        self._apellido_P = apellido_p
        self._apellido_M = apellido_m
        self._edad = edad
        self._n_telefono = n_telefono
        self._correo = correo
        self._domicilio = domicilio
        self._puesto = puesto
        self._sueldo = sueldo

    # Setters y Getters ================================================================================================
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        if id_persona:
            self._id_persona = id_persona
        else:
            messagebox.showerror('Error', 'Faltan datos!')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            messagebox.showerror('Error', 'El nombre no puede estar vacío!')
        else:
            self._nombre = nombre

    @property
    def apellido_p(self):
        return self._apellido_P

    @apellido_p.setter
    def apellido_p(self, apellido):
        if not apellido:
            messagebox.showerror('Error', 'El apellido paterno no puede estar vacío!')
        else:
            self._apellido_P = apellido

    @property
    def apellido_m(self):
        return self._apellido_M

    @apellido_m.setter
    def apellido_m(self, apellido):
        if not apellido:
            messagebox.showerror('Error', 'El apellido materno no puede estar vacío!')
        else:
            self._apellido_M = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            messagebox.showerror('Error', 'La edad no puede ser negativa!')
        else:
            self._edad = edad

    @property
    def n_telefono(self):
        return self._n_telefono

    @n_telefono.setter
    def n_telefono(self, telefono):
        if not telefono:
            messagebox.showerror('Error', 'El número de teléfono no puede estar vacío!')
        else:
            self._n_telefono = telefono

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        if correo and ("@" not in correo or "." not in correo):
            messagebox.showerror("Error de Correo!", f'Correo inválido')
        else:
            self._correo = correo

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, domicilio):
        if not domicilio:
            messagebox.showerror('Error', 'El domicilio no puede estar vacío!')
        else:
            self._domicilio = domicilio

    @property
    def puesto(self):
        return self._puesto

    @puesto.setter
    def puesto(self, puesto):
        if not puesto:
            messagebox.showerror('Error', 'El puesto no puede estar vacío!')
        else:
            self._puesto = puesto

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        if sueldo < 0:
            messagebox.showerror('Sueldo Error!', f'El sueldo del trabajador {self.nombre} no puede ser menor de 0!')
        else:
            self._sueldo = sueldo

    # Métodos ==========================================================================================================
    def __str__(self):
        return f"""Persona: {self.id_persona}
    Persona: {self.nombre} {self.apellido_p} {self.apellido_m}, Edad: {self.edad}
    Numero de telefono: {self.n_telefono}
    Correo: {self.correo}
    Domicilio: {self.domicilio}
    Puesto: {self.puesto}
    Sueldo: {self.sueldo}
"""


class Administrador(Persona):
    """
    Clase Administrador
    Hereda de la clase Persona

    :argument
        id_administrador
    """
    _numero_admin = 0

    @classmethod
    def aumentar_admin(cls):
        cls._numero_admin += 1
        return cls._numero_admin

    def __init__(self, nombre="", apellido_p="", apellido_m="", edad=0, n_telefono="",
                 correo="", domicilio="", puesto="", sueldo=0.0):
        self._id_admin = self.aumentar_admin()
        super().__init__(nombre, apellido_p, apellido_m, edad, n_telefono, correo, domicilio, puesto, sueldo)

    # Métodos ==========================================================================================================
    def __str__(self):
        return f"""Admin: {self._id_admin}
    Persona: {self.nombre} {self.apellido_p} {self.apellido_m}, Edad: {self.edad}
    Numero de telefono: {self.n_telefono}
    Correo: {self.correo}
    Domicilio: {self.domicilio}
    Puesto: {self.puesto}
    Sueldo: {self.sueldo}
"""


class Empleado(Persona):
    """
    Clase Empleado
    Hereda de la clase persona

    :argument
        id_empleado
    """
    _numero_empleado = 0

    @classmethod
    def aumentar_empleado(cls):
        cls._numero_empleado += 1
        return cls._numero_empleado

    def __init__(self, nombre="", apellido_p="", apellido_m="", edad=0, n_telefono="",
                 correo="", domicilio="", puesto="", sueldo=0.0):
        self._id_empleado = self.aumentar_empleado()
        super().__init__(nombre, apellido_p, apellido_m, edad, n_telefono, correo, domicilio, puesto, sueldo)

    # Métodos ==========================================================================================================
    def __str__(self):
        return f"""Empleado: {self._id_empleado}
    Persona: {self.nombre} {self.apellido_p} {self.apellido_m}, Edad: {self.edad}
    Numero de telefono: {self.n_telefono}
    Correo: {self.correo}
    Domicilio: {self.domicilio}
    Puesto: {self.puesto}
    Sueldo: {self.sueldo}
"""


class Visitante:
    """
    Clase Visitante

    :argument
        id_visitante
        nombre
        apellido
        fecha_entrada
        hora_entrada
        motivo_visita
        id_empleado_a_visitar
    """
    _id_visitante = 0

    @classmethod
    def aumentar_visitante(cls):
        cls._id_visitante += 1
        return cls._id_visitante

    def __init__(self, nombre="", apellido_p="", apellido_m="",
                 fecha_entrada="", hora_entrada="", motivo_visita="", id_empleado_a_visitar=0):
        self._id_visita = self.aumentar_visitante()
        self._nombre = nombre
        self._apellido_p = apellido_p
        self._apellido_m = apellido_m
        self._fecha_entrada = fecha_entrada
        self._hora_entrada = hora_entrada
        self._motivo_visita = motivo_visita
        self._id_empleado_a_visitar = id_empleado_a_visitar

    # Getters y Setters ================================================================================================
    @property
    def id_visita(self):
        print(f'Retorno id visita')
        return self._id_visita

    @property
    def nombre(self):
        print(f'Retorno nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print(f'Asignacion nombre: {nombre}')
        self._nombre = nombre

    @property
    def apellido_p(self):
        print(f'Retorno apellido paterno')
        return self._apellido_p

    @apellido_p.setter
    def apellido_p(self, apellido):
        print(f'Asignacion apellido paterno: {apellido}')
        self._apellido_p = apellido

    @property
    def apellido_m(self):
        print(f'Retorno apellido materno')
        return self._apellido_m

    @apellido_m.setter
    def apellido_m(self, apellido):
        print(f'Asignacion apellido materno:: {apellido}')
        self._apellido_m = apellido

    @property
    def fecha_entrada(self):
        print(f'Retorno fecha entrada')
        return self._fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, f_entrada):
        print(f'Asignacion fecha entrada: {f_entrada}')
        self._fecha_entrada = f_entrada

    @property
    def hora_entrada(self):
        print(f'Retorno hora')
        return self._hora_entrada

    @hora_entrada.setter
    def hora_entrada(self, hora):
        if hora is None:
            self._hora_entrada = datetime.datetime.now()
        else:
            # Aquí puedes validar el formato de la hora
            self._hora_entrada = hora
        print(f'Asignacion hora: {hora}')

    @property
    def motivo_visita(self):
        print(f'Retorno motivo')
        return self._motivo_visita

    @motivo_visita.setter
    def motivo_visita(self, m_visita):
        print(f'Asignacion motivo: {m_visita}')
        self._motivo_visita = m_visita

    @property
    def id_empleado_a_visitar(self):
        print(f'Retorno empleado a visitar')
        return self._id_empleado_a_visitar

    @id_empleado_a_visitar.setter
    def id_empleado_a_visitar(self, id_e):
        print(f'Asignacion empleado a visitar:: {id_e}')
        self._id_empleado_a_visitar = id_e

    # Métodos ==========================================================================================================
    def __str__(self):
        return f"""Visita: {self.id_visita}
        Nombre: {self.nombre} {self.apellido_p} {self.apellido_m}
        Entrada: {self.fecha_entrada}
        Hora: {self.hora_entrada}
        Motivo: {self.motivo_visita}
        ID empleado a visitar: {self._id_empleado_a_visitar}
"""


if __name__ == '__main__':
    # persona = Persona(nombre='Carlos Edgar', apellido_p='Monroy', apellido_m='Velasco',
    #                   correo='monroyC98@gmail.com', sueldo=10)
    # print(persona)
    #
    # admin = Administrador(nombre='Carlos Edgar', apellido_p='Monroy', apellido_m='Velasco',
    #                       correo='monroyC98@gmail.com', sueldo=100)
    # print(f'\n{admin}')
    #
    # empleado = Empleado(nombre='Carlos Edgar', apellido_p='Monroy', apellido_m='Velasco',
    #                     correo='monroyC98@gmail.com', sueldo=1000)
    # print(f'\n{empleado}')

    visitante = Visitante('Carlos')
    print(f'\n{visitante}')
