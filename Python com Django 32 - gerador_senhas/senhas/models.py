from django.db import models

class Senha(models.Model):
    valor = models.CharField(max_length=40)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.valor
