#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
import json
import re
import copy
import jieba
import time
from answer_generator import AnsGenerator

inPage = []
matchList = []
resultNum = 0
inputText = ''

def mainView(request):
    return render(request, "mainView.html")

def receiveInput(request):
    global inPage
    global matchList
    global resultNum
    global inputText

    request.encoding = 'utf-8'

    tempInputText = request.GET.get('inputText')

    if not tempInputText:
        return render(reuqest, "mainView.html")

    ansGen = AnsGenerator(tempInputText)
    type, results = ansGen.getAnsList()
    if type is "html":
        return render(request, results)
    if type is "normal":
        return HttpResponseRedirect("https://www.baidu.com/s?wd=" + tempInputText)
    '''
    results:
    [
        {
            title: (str)
            desription: {
                passage:
                static:
            }
            url:
        }
    ]
    '''
    resultNum = len(results)

    if resultNum % 10 == 0 and resultNum is not 0:
        n = resultNum / 10
    else:
        n = int(resultNum / 10) + 1

    inPage = [{'num': i + 1, 'nextNum': i + 2, 'hasNext': True, 'in': False} for i in range(n)]
    inPage[n - 1]['hasNext'] = False
    matchList = []
    for i in range(0, n - 1):
        matchList.append(results[i : i + 10])
    matchList.append(results[10 * (n - 1):])

    return renderPage(request)

def image(request):
    return render(request, "image.html")

def baike(request):
    return render(request, "baike.html")

def wish(request):
    return render(request, "wish.html")

def newsBroswer(request):
    print request.path
    reg = re.compile(r'\d+')
    s = reg.search(request.path)
    uniId = s.group()
    id = int(uniId.encode('utf-8'))
    newsDict = search.newsList[id]
    news = {}
    news['title'] = newsDict['title']
    news['passage'] = newsDict['passage'].split('\n')
    news['time'] = newsDict['time']

    simiList = search.getSimilar(id)
    simiNews = []
    for id in simiList:
        simiNews.append(search.newsList[id])
    return render(request, "newsBroswer.html", {'news': news, 'simiNews': simiNews})

def renderPage(request):
    reg = re.compile(r'\d+')
    s = reg.search(request.path)
    uniPageNum = s.group()
    pageNum = int(uniPageNum.encode('utf-8'))
    for page in inPage:
        page['in'] = False
    inPage[pageNum - 1]['in'] = True
    startN = 0
    endN = 0
    if len(inPage) <= 10:
        startN = 0
        endN = len(inPage)
    else:
        if pageNum - 1 - 5 < 0:
            startN = 0
            endN = 10
        elif pageNum - 1 + 5 > len(inPage):
            startN = len(inpage) - 10
            endN = len(inPage)
        else:
            startN = pageNum - 1 - 5
            endN = pageNum - 1 + 5
    limitInPage = inPage[startN : endN]
    return render(request, 'showResult.html', {'results': matchList[pageNum - 1], 'number': resultNum, 'inPage': limitInPage, 'inputText': inputText})
