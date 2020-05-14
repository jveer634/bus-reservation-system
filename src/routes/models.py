from django.db import models

class City(models.Model):
    cname = models.CharField("City Name", max_length = 255)
    ccode = models.CharField("City Code", max_length = 5)

    class Meta:
        verbose_name_plural = "Cities"
    
    def __str__(self):
        return self.cname


class Route(models.Model):
    source = models.OneToOneField(City, on_delete = models.CASCADE, related_name = "From")
    destination = models.OneToOneField(City, on_delete = models.CASCADE, related_name = "To")
    through = models.ForeignKey(City, on_delete = models.CASCADE)
    rname = models.CharField("Route Name", max_length = 10)


    def __str__(self):
        return self.rname