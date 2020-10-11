# I have created this file - Shawon Mahmud

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>Hi, I am Shawon Mahmud lived in the kushtia city.</h1>')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('full_caps', 'off')
    new_line_remover = request.POST.get('new_line_remover', 'off')

    # check which checkbox is on
    if (removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed += i
        params = {
            'purpose': 'Removed Punctuations',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (full_caps == 'on'):
        analyzed = djtext.upper()
        params = {
            'purpose': 'Capitalize Full Text',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (new_line_remover == 'on'):
        analyzed = ""
        for i in djtext:
            if i != '\n' and i != '\r':
                analyzed += i
            params = {
                'purpose': 'Remove New Line',
                'analyzed_text': analyzed
            }
            # djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (removepunc != 'on' and full_caps != 'on' and new_line_remover != 'on'):
        return HttpResponse('Please select the operation and try again.')
    
    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse('Error')
