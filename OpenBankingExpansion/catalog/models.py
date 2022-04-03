from django.db import models

class clientes(models.Model):
    cliente_id = models.TextField(primary_key=True)
    secret = models.TextField()
    token = models.TextField()

    class Meta:
        ordering = ['-clientes']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cliente_id

