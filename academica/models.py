from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.db.models import Avg, Count, Q

class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    genero = models.CharField(max_length=20, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def edad(self):
        today = timezone.now().date()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

class Docente(Persona):
    especialidad = models.CharField(max_length=100)
    grado_academico = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f"{self.nombre_completo()} - {self.especialidad}"

    # ... (métodos existentes)

class Alumno(Persona):
    matricula = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField()
    correo_padre = models.EmailField()
    correo_madre = models.EmailField()

    def __str__(self):
        return f"{self.nombre_completo()} - {self.matricula}"

    # ... (métodos existentes)

class Aula(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50)  # Por ejemplo: "Laboratorio", "Aula regular", etc.

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    creditos = models.PositiveIntegerField()
    docentes = models.ManyToManyField(Docente, through='CursoProfesor')
    alumnos = models.ManyToManyField(Alumno, through='Inscripcion')
    semestre = models.PositiveIntegerField(default=1)
    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    # ... (métodos existentes)

class CursoProfesor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    es_titular = models.BooleanField(default=False)

    class Meta:
        unique_together = ('curso', 'docente')

    def __str__(self):
        return f"{self.docente} - {self.curso}"

class Horario(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=[
        ('LUN', 'Lunes'), ('MAR', 'Martes'), ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'), ('VIE', 'Viernes'), ('SAB', 'Sábado'), ('DOM', 'Domingo')
    ])
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        unique_together = ('curso', 'dia_semana', 'hora_inicio')

    def __str__(self):
        return f"{self.curso} - {self.dia_semana} {self.hora_inicio}-{self.hora_fin}"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    calificacion_final = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    asistencia = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        unique_together = ('alumno', 'curso')

    def __str__(self):
        return f"{self.alumno} - {self.curso}"

    def estado(self):
        if self.calificacion_final is None:
            return "En curso"
        elif self.calificacion_final >= 6:
            return "Aprobado"
        else:
            return "Reprobado"

class Evaluacion(models.Model):
    TIPO_CHOICES = [
        ('CONTINUA', 'Evaluación Continua'),
        ('TRIMESTRAL', 'Evaluación Trimestral'),
    ]
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.curso} - {self.tipo} - {self.fecha}"

class CalificacionEvaluacion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    calificacion = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        unique_together = ('evaluacion', 'alumno')

    def __str__(self):
        return f"{self.alumno} - {self.evaluacion} - {self.calificacion}"

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"De: {self.emisor} - Para: {self.receptor} - Asunto: {self.asunto}"
    
    