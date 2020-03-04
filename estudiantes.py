class Estudiantes:
    def __init__(self, matricula, nombre, apellido, curso, estado):
        self.matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        if estado in ("aprobado","reprobado"):
            self.estado = estado
        else:
            self.estado = "aprobado"

#En la primera ruta debe presentar un listado de estudiantes que reciba desde la función
#render_templates. Cada estudiante tendrá matricula, nombre, apellido y curso, estado (aprobado o
#reprobado) Deberá mostrar los datos en una tabla en la plantilla.