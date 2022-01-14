from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.FileField(
        upload_to='proj_thumbnails', help_text="Small img")
    h1 = models.CharField(max_length=200, help_text="Name of the project")
    intro = models.TextField(
        max_length=500, help_text="Brief discription of the project")
    made_with = models.CharField(
        max_length=240, help_text="Technologies used for building  a project, separate with #")
    paragraph = models.TextField(
        help_text="Full discription of the project. Use HTML tags to style a text.")
    image = models.FileField(upload_to='projects',
                             help_text="Full size img")
    source_file = models.URLField(help_text="Link to source code")
    live_demo = models.URLField(help_text="Url link of live webpage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
