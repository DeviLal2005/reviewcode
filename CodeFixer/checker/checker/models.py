from django.db import models

class CodeSubmission(models.Model):
    code = models.TextField()
    errors = models.TextField(blank=True,null=True)
    suggestions = models.TextField(blank=True,null=True)
    fixed_code = models.TextField(blank=True,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)