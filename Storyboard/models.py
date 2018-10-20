from django.db import models
from CoursesPY.models import Course
from Storyboard.enums import *
from django.contrib.auth.models import User


class Storyboard(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    graphic_hours_goal = models.FloatField(default=0.0)
    graphic_hours_actual = models.FloatField(default=0.0)
    graphic_status = models.CharField(max_length=30,
                                      choices=[(tag, tag.value) for tag in GraphicStatus])
    in_lms = models.BooleanField(default=False)
    length = models.FloatField(default=0.0)
    narration_status = models.CharField(max_length=30,
                                        choices=[(tag, tag.value) for tag in NarrationStatus])
    narration_tone = models.CharField(max_length=255, blank=True)
    objective = models.TextField(blank=True)
    references = models.TextField(blank=True)
    regulatory = models.TextField(blank=True)
    retake_months = models.FloatField(default=0.0)
    sme_review = models.BooleanField(default=False)
    sme_revisions_complete = models.BooleanField(default=False)
    status = models.CharField(max_length=30,
                              choices=[(tag, tag.value) for tag in StoryboardStatus],
                              default=StoryboardStatus.NONE)


class Term(models.Model):
    definition = models.TextField(blank=False)
    graphic_number = models.CharField(max_length=50, unique=True, blank=True)
    screen_number = models.CharField(max_length=50, unique=True, blank=True)
    storyboard = models.ForeignKey(Storyboard, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)


class MapEntry(models.Model):
    storyboard = models.ForeignKey(Storyboard, on_delete=models.CASCADE)
    assessments = models.TextField(blank=True)
    course_goal = models.TextField(blank=True)
    course_objective = models.TextField(blank=True)
    teaching = models.TextField(blank=True)


class Revision(models.Model):
    category = models.CharField(max_length=30,
                                choices=[(tag, tag.value) for tag in RevisionCategory])
    date_complete = models.DateTimeField(blank=True)
    date_issued = models.DateTimeField()
    issued_to = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="revision_issued_to")
    issuer = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="revision_issuer")
    text = models.TextField(blank=True)
    storyboard = models.ForeignKey(Storyboard, on_delete=models.CASCADE)
    type = models.CharField(max_length=30,
                            choices=[(tag, tag.value) for tag in RevisionType])


class ActivityType(models.Model):
    name = models.CharField(max_length=255)


class LearningActivity(models.Model):
    storyboard = models.ForeignKey(Storyboard, on_delete=models.CASCADE)
    path = models.CharField(max_length=255, blank=True)
    upload_type = models.CharField(max_length=30,
                                   choices=[(tag, tag.value) for tag in UploadType])
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    purpose = models.TextField(blank=True)
    types = models.ManyToManyField(ActivityType)


class Lesson(models.Model):
    number = models.IntegerField()
    storyboard = models.ForeignKey(Storyboard, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Screen(models.Model):
    complete = models.BooleanField(default=False)
    content = models.TextField(blank=True)
    graphic_note = models.TextField(blank=True)
    number = models.CharField(max_length=10)
    position = models.IntegerField()

    class Meta:
        abstract = True


class LessonScreen(Screen):
    graphic_filename = models.CharField(max_length=255, blank=True)
    narration_filename = models.CharField(max_length=255, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    writing_note = models.TextField(blank=True)
    type = models.CharField(max_length=30,
                            choices=[(tag, tag.value) for tag in ScreenType])


class ActivityScreen(Screen):
    learning_activity = models.ForeignKey(LearningActivity, on_delete=models.CASCADE)
    narration = models.TextField(blank=True)


