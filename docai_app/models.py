from django.db import models
from django.urls import reverse

class Document(models.Model):
    doc_id = models.AutoField(db_column='DOC_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', unique=True, max_length=255)  # Field name made lowercase.
    doc_url = models.URLField(db_column='DOC_URL')  # Field name made lowercase.
    doc_summary = models.TextField(db_column='DOC_SUMMARY', blank=True, null=True)  # Field name made lowercase.
    upload_date = models.DateField(db_column='UPLOAD_DATE')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'ibef_tb'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("docai_app:detail", kwargs={"pk": self.pk})
    