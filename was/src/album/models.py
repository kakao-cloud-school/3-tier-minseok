from django.db import models

# Create your models here.
class Album(models.Model):
    a_no = models.AutoField(primary_key=True)
    a_type = models.CharField(max_length=50)
    a_title = models.CharField(max_length=255)
    a_note = models.CharField(max_length=4096, blank=True, null=True)
    a_image = models.CharField(max_length=4096, blank=True, null=True)
    a_count = models.IntegerField()
    a_datetime = models.DateTimeField(blank=True, null=True)
    a_usage = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'album'


    def __str__(self):
        return "제목 :" + self.a_title + ", 유형 : " + self.a_type
