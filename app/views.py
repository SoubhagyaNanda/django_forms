from django.shortcuts import render
from app.models import *
# Create your views here.


def school_info(request):
    if request.method == 'POST':
        sname=request.POST['scname']
        scp= request.POST['scprincipal']
        sloc=request.POST['scloc']
        sid=request.POST['scid']

        scl= school.objects.get_or_create(ScName=sname, ScPrincipal=scp, ScLoc=sloc, ScId=sid)[0]
        scl.save()

        QLSO= school.objects.all()
        d={'QLSO': QLSO}
        return render(request,'display_school.html', context = d)
    return render(request, 'school_info.html')


def student_info(request):
    if request.method=='POST':

        sname=request.POST['scname']
        sc=school.objects.get(ScName=sname)



        stdname=request.POST['studentname']
        clname=request.POST['cls']
        stdid=request.POST['ID']

        std=student.objects.get_or_create(ScName=sc, Sname=stdname,ClassName=clname,Sid=stdid)[0]
        std.save()

        LST= student.objects.all()

        d = {'LST':LST}
        return render(request, 'display_student.html', context=d)
    return render(request,'student_info.html')