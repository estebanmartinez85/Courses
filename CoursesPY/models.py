from django.db import models
from Libraries.models import Library
from django.contrib.auth.models import User
from CoursesPY.enums import CourseStatus
from Storyboard.models import Storyboard


class Course(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    archived = models.BooleanField(default=False)
    users = models.ManyToManyField(User)
    code = models.CharField(max_length=255, unique=True)
    final_review = models.BooleanField(default=False)
    final_revisions_complete = models.BooleanField(default=False)
    final_team_review = models.BooleanField(default=False)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL)
    manager_quality_check = models.BooleanField(default=False)
    manager_quality_revision = models.BooleanField(default=False)
    planning_meeting_complete = models.BooleanField(default=False)
    sme_course_review = models.BooleanField(default=False)
    sme_course_revisions = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=[(tag, tag.value) for tag in CourseStatus],
                              default=CourseStatus.ASSIGN_WRITER)
    title = models.CharField(max_length=255, unique=True)


class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=False, blank=False)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL)


class TaskCategory(models.Model):
    name = models.CharField(max_length=50)


class EWebOQCourse(Course):
    equivalent = models.OneToOneField('self')
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL)







