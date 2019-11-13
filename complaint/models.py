from django.db import models


class ComplaintCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Complaint(models.Model):
    complaint = models.TextField()
    student = models.CharField(max_length=200)

    complaint_category = models.ForeignKey(
        'ComplaintCategory',
        on_delete = models.CASCADE
    )