from django.db import models

# Create your models here.
class Topic(models.Model):
    """Temat poznawany przez uzytkownika."""
    text = models.CharField(max_length=200)
    data_added = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        """Zwraca reprezentację modelu w postaci ciągu tekstowego."""
        return self.text