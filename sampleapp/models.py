from django.db import models

class Collection(models.Model):
    disease_term = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Sample(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    donor_count = models.IntegerField()
    material_type = models.CharField(max_length=100)
    last_updated = models.DateField()

    def __str__(self):
        return f"Sample {self.id} - Collection: {self.collection.title}"

