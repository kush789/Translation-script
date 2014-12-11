import json, requests

def readableform(input):
    if isinstance(input, dict):
        return {readableform(key):readableform(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [readableform(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def prepare(lang1,lang2,text):
    text.replace(" ","%20")
    apikey = "trnsl.1.1.20141211T185649Z.4500c98611fee85d.8ea47016ff18f145a0655321e8dc58e5e8a90351"
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key="+apikey+"&lang="+lang1+"-"+lang2+"&text="+text
    return url

def getresponse(lang1,lang2,text):
    url = prepare(lang1,lang2,text)
    yandexresponse = requests.post(url)
    return yandexresponse

def translatetext(lang1,lang2,text):
    yandexresponse = getresponse(lang1,lang2,text)
    translatedtext = readableform(json.loads(yandexresponse.text)['text'])[0]

    translatedtextfile = open('translatedtextfile.txt','w')
    translatedtextfile.write(translatedtext)
    translatedtextfile.close()

    return translatedtext











