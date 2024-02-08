from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormClass
from .models import storedata

def showdata(request):
    
    # if request.method=="POST":
        
    #     num1=int(request.POST.get("first"))
    #     num2=int(request.POST.get("second"))
    #     fm=FormClass(initial={"first":num1,"second":num2})
    #     lst=[]
    #     for i in range(1,(num2+1)):
    #         lst.append(f"{num1}*{i}={num1*i}")
    #     return render(request,"baseform.html",{"dict":lst,"form":fm,"num1":num1,"second":num2})     
    # else:
    #     fm=FormClass()
    #     return render(request,"baseform.html",{"form":fm})

    if request.method=="POST":
        
        num1=int(request.POST.get("first"))
        num2=int(request.POST.get("second"))
        fm=FormClass(initial={"first":num1,"second":num2})
        lst=[]
        for i in range(1,(num2+1)):
            lst.append(f"{num1}*{i}={num1*i}")
        newdata=storedata(data=lst)
        newdata.save()
        return render(request,"baseform.html",{"dict":lst,"form":fm,"num1":num1,"second":num2})     
    else:
        fm=FormClass()
        return render(request,"baseform.html",{"form":fm})




    
#     return render(request,"base.html")
# def table(request):
#     lst=[]
#     if request.method == 'POST':
#         num1= int(request.POST.get('fnum'))
#         num2 = int(request.POST.get('lnum'))
#         for i in range(1,(num2+1)):
#             lst.append(f"{num1}*{i}={num1*i}")
#         lst.append(f"{num1}*{i}={num1 * i}")
#         return render(request, 'base.html', {"lst": lst,"num1":num1,"num2":num2
#                                              })
#     else:
#         return render(request,"base.html")


    

    
