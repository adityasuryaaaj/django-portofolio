from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to="projects/",blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tech_stack = models.CharField(max_length=200, blank=True)
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
