from django.db import models


class Members(models.Model):
    memeber_name = models.CharField(max_length=255)
    memmber_added_date = models.DateTimeField()
    member_president = models.CharField(max_length=255)
    member_image = models.ImageField(upload_to='member/', blank=True)

    def __str__(self):
        return self.memeber_name

    class Meta:
        ordering = ['id', ]
        db_table = 'members'
        verbose_name = "Members"


class Organizations(models.Model):
    organization_name = models.CharField(max_length=255)
    organization_organizate_date = models.DateTimeField()
    organization_president = models.CharField(max_length=255)
    organization_logo = models.ImageField(upload_to='organization/', blank=True)

    def __str__(self):
        return self.organization_name

    class Meta:
        ordering = ['id', ]
        db_table = 'organizations'
        verbose_name = "Organizations"
