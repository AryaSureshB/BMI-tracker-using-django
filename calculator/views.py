from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class BmiView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")
    
    def post(self,request,*args,**kwargs):

        weight=int(request.POST.get("wbox"))
        height=int(request.POST.get("hbox"))
        height_in_meter=height/100
        bmi=weight/(height_in_meter)**2
        bmi=round(bmi,2)

        result=""

        if bmi<19:
            result="underweight"
        elif bmi<25:
            result="normalweight"
        elif bmi<30:
            result="overweight"
        elif bmi>30:
            result="obese"


        return render(request,"bmi.html",{"data":result})
