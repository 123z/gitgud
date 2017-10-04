from django.shortcuts import render

#from django.http import HttpResponse

def about(request):
    #return HttpResponse()
    context_dict = {'boldmessage': "ASDF"}
    return render(request, 'auscities/about.html', context=context_dict)
