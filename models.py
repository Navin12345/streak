from django.db import models
import datetime

class classcast_karma_history(models.Model):
    Serial_Number=models.IntegerField(null=False, primary_key=True)
    student_id = models.IntegerField(null=False)
    date = models.DateField(default=datetime.date.today)
    karma_points = models.FloatField() 

    class Meta:
        db_table = 'classcast_karma_history'
    def __str__(self):
        return u'student id, %s- score-%s' % (str(self.student_id), str(self.karma_points))
