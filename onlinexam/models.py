from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Exam(models.Model):
	exam_id = models.AutoField(primary_key=True)
	#user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	exam_title = models.CharField(max_length=30)
	start_date = models.DateTimeField()
	finish_date = models.DateTimeField()

	def __str__(self):
		return '%s' % self.exam_title

	def get_absolute_url(self):
		now = timezone.now()
		if self.finish_date <= now:
			return "/onlinexam/exam/%i/expired" % self.exam_id
		elif self.start_date > now:
			return "/onlinexam/exam/%i/notStarted" % self.exam_id
		else:
			return "/onlinexam/exam/%i/solve" % self.exam_id



class Question(models.Model):
	question_id = models.AutoField(primary_key=True)
	exam_id = models.ForeignKey(Exam, on_delete = models.CASCADE)
	question_text = models.TextField()
	answer_A = models.TextField()
	answer_B = models.TextField()
	answer_C = models.TextField()
	answer_D = models.TextField()
	answer_E = models.TextField()

	def __str__(self):
		return "%s - Question %s" % (self.exam_id, self.question_id)

class Question_Answer(models.Model):
	question_answer_id = models.AutoField(primary_key=True)
	exam_id = models.ForeignKey(Exam, on_delete = models.CASCADE)
	question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
	answer_number = models.IntegerField()
	point = models.IntegerField()


class Student_Answer(models.Model):
	student_answer_id = models.AutoField(primary_key=True)
	#user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	exam_id = models.ForeignKey(Exam, on_delete = models.CASCADE)
	question_id = models.ForeignKey(Question, on_delete = models.CASCADE)
	answer_number = models.IntegerField()
