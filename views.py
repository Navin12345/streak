from django.http import HttpResponse
from rest_framework.views import APIView
from .models import classcast_karma_history
from datetime import date, timedelta


class streak(APIView):
    def get(self, request, student_id):
        streak=0
        d = date.today()
        try:
            today_point = classcast_karma_history.objects.get(student_id = student_id, date = d)
            if(today_point.karma_points >=60.0):
                streak=1
        except:
            pass;
        yesterday = d - timedelta(1)
        if not classcast_karma_history.objects.filter(student_id = student_id, date = yesterday).exists():
            return(HttpResponse(streak))
        
        while(True):
            d = d - timedelta(1)
            Classcast_karma_history2 = classcast_karma_history.objects.get(student_id = student_id, date = d)
            point = Classcast_karma_history2.karma_points
            if(type(point) == int or float):
                if(point < 60.0):
                    break;
                streak += 1
            else:
                break
        return(HttpResponse(streak))

    def post(self):
        pass
