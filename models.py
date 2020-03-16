from django.db import models

class Book(models.Model):
    book_id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    report = models.ForeignKey('Report', to_field='book_id', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Report(models.Model):
    book_id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
