from django.db import models


class ProfilePicture(models.Model):
    image = models.ImageField()
    userId = models.TextField(blank=False, null=False, primary_key=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_on.date()

    class Meta:
        db_table = 'profile_image'

class BookPicture(models.Model):
    image = models.ImageField()
    bookId = models.TextField(blank=False, null=False, primary_key=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_on.date()

    class Meta:
        db_table = 'book_image'


class Assignment(models.Model):
    file = models.FileField(blank=False, null=False)
    userId = models.TextField(blank=False, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'assignments'

class Complaint(models.Model):
    file = models.FileField(blank=False, null=False)
    userId = models.TextField(blank=False, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'complaints_files'
