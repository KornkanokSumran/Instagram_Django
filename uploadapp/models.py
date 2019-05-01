from django.db import models


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    caption = models.CharField(max_length=256 ,null="No Caption")
    def __str__(self):
        return self.file.name

class Description(models.Model):
    name = models.ForeignKey(File, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

class Comment(models.Model):
    name = models.ForeignKey(File, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)


