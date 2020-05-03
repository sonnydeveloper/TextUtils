from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'hello': ' Hello Guys, Welcome', 'template': 'Template'}
    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    djcheck = request.POST.get('isanalyze', 'off')
    djcapfirst = request.POST.get('capfirst', 'off')
    newlinesremover = request.POST.get('newlinesremover', 'off')
    extraspacesremover = request.POST.get('extraspacesremover', 'off')
    totalcharcount = request.POST.get('totalcharcount', 'off')

    punctualtions = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    if djcheck == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctualtions:
                analyzed = analyzed + char

        djtext = analyzed
        data = {'purpose' : 'Removed Punctuation', 'analyzed_text' : analyzed}

    if djcapfirst == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        djtext = analyzed
        data = {'purpose': 'Change Uppercase', 'analyzed_text': analyzed}

    if newlinesremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        djtext = analyzed
        data = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}

    if extraspacesremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        djtext = analyzed
        data = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}

    if totalcharcount == "on":
        analyzed = ""
        i = 0
        for char in djtext:
            i += 1
        analyzed = i

        data = {'purpose': 'Total Characters', 'analyzed_text': analyzed}

    if djtext == "" and djcheck != "on" and djcapfirst != "on" and newlinesremover != "on" and \
            extraspacesremover != "on" and totalcharcount != "on":
        return HttpResponse("<h1>Please Check Selections checkbox and try again.</h1>")

    return render(request, 'analyzed.html', data)
