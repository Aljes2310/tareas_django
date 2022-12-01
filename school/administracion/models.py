from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    born_date = models.DateField(default="")

    class Meta:
        abstract=True   #el modelo que usa abstract no se crea

class ClassRoom(models.Model):
    name= models.CharField(max_length=200)
    start_time = models.TimeField()

    def __str__(self):
        return self.name + " - " + str(self.start_time) #sino altera la base de datos no se necesita migraciones

    class Meta:
        db_table = "classroom"   #permite darle un nombre a mi tabla y ya no salga django_classrom


class Student(Person):
    classroom_id=models.ForeignKey(ClassRoom, on_delete=models.CASCADE) #se elimina db en cascada si se elimina la padre
    grade_lab=models.FloatField(default=0.0)
    grade_exam=models.FloatField(default=0.0)
    grade_final=models.FloatField(default=0.0)

    class Meta:
        db_table = "students"

class StudentProxu(Student):
    class Meta:
        ordering= ["-id"] #forma descendente
        proxy=True
    
    def average(self):
        return self.grade_exam*0.1 + self.grade_lab*0.6 + self.grade_final*0.3



class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)    

    class Meta:
        db_table = "teachers"

class TeacherProxy(Teacher):
    class Meta:
        proxy=True
    
    def get_bonus(self):
        return self.salary + self.rating*100


class Evaluacion(models.Model):
    Fecha=models.DateTimeField()
    Curso=models.CharField(max_length=30)
    Evaluador=models.CharField(max_length=50)

    class Meta:
        abstract=True
        db_table= "Evaluacion"

class Examen_Final(Evaluacion):
    Duracion=models.IntegerField()
    Preguntas=models.IntegerField()
    Puntaje_total=models.IntegerField()

    class Meta:
        db_table="Examen_Final"

    def puntaje(self):
        return self.Preguntas/self.Puntaje_total

class Proyecto(Evaluacion):
    Tema=models.CharField(max_length=100)
    Grupos=models.IntegerField()

    class Meta:
        db_table = "Proyecto"

class ProyectoProxy(Proyecto):
    class Meta:
        proxy=True
        ordering = ['Tema']

