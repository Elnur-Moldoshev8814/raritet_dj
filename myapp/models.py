from django.db import models

class Filial(models.Model):
    name = models.CharField(max_length=88)
    address = models.CharField(max_length=88)

    def __str__(self):
        return f"{self.name} | {self.address}"

class Author(models.Model):
    name = models.CharField(max_length=14)
    date_of_birth = models.DateTimeField(auto_now=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    title = models.CharField(max_length=14)
    description = models.TextField()
    id_author = models.ForeignKey(Author, on_delete=models.PROTECT)
    id_filial = models.ForeignKey(Filial, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} | {self.description[:50]}..."