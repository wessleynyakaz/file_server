from django.urls import path
from .views import UploadProfileImageView, UploadBookImageView, UploadAssignmentView, UploadComplaintView

urlpatterns = [
    path('upload_profile_image/', UploadProfileImageView.as_view(), name='upload-profile-image'),
    path('upload_book_image/', UploadBookImageView.as_view(), name='upload-book-image'),
    path('upload_assignment/', UploadAssignmentView.as_view(), name='upload-assignment'),
    path('upload_complaint/', UploadComplaintView.as_view(), name='upload-complaint'),

]
