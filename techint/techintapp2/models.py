from django import forms
from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    class Meta:
        verbose_name_plural = "people"

    name = models.CharField(max_length=50, verbose_name="Imię")
    date_of_birth = models.DateField(verbose_name="Data urodzenia")
    email = models.EmailField(verbose_name="Adres e-mail")
    height = models.IntegerField(verbose_name="Wzrost", default=170)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nazwa")
    description = models.CharField(max_length=1000, verbose_name="Opis")
    client = models.CharField(max_length=1000, verbose_name="Klient")

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Nazwa")
    description = models.CharField(max_length=1000, verbose_name="Opis")
    time_elapsed = models.IntegerField(
        verbose_name="Przepracowany czas", null=True, default=None, blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, verbose_name="Projekt",
        null=True, default=None, blank=True)
    app_user = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name="Wykonawca")

    def __str__(self):
        return self.title


class Supervisor(Person):
    specialisation = models.CharField(
        max_length=50, verbose_name="Specjalizacja")


class Developer(Person):
    dev_supervisor = models.ForeignKey(
        Supervisor, on_delete=models.CASCADE, verbose_name="Przełożony")


BIRTH_YEAR_CHOICES = range(1900, 2018)


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['name', 'date_of_birth', 'email', 'height', 'dev_supervisor']
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
        }
