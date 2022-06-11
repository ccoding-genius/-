from django.shortcuts import render
from datetime import datetime

# Create your views here.
def Time_Table(request):
    date_time_str = request.GET.get('date', None)
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    print(date_time_obj)
    return render(request, 'blog/Time_Table.html', {})

def VIOL(request):
    return render(request, 'VIOL.html', {})
