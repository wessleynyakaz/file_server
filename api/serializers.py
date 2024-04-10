from rest_framework import serializers
from .models import ProfilePicture, TeacherPicture, BookPicture, Assignment, Complaint


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ('image', 'uploaded_on', 'userId')

class TeacherImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherPicture
        fields = ('image', 'uploaded_on', 'userId')

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPicture
        fields = ('image', 'uploaded_on', 'bookId')

class AssignmentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('file', 'uploaded_on', 'userId')

class ComplaintUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('file', 'uploaded_on', 'userId')
