from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import student
import xml.etree.cElementTree as e
import json as j
# Create your views here.

def json(self):
    
    data=list(student.objects.values())
    
    with open("my.json",'a') as file:
        for i in data:
            file.write(str(i)+'\n')
    
    
    with open("my.json") as json_format_file:
        d = j.load(json_format_file)
        print(d)
    
    r = e.Element("Employee") # field

    e.SubElement(r,"name").text = d["name"]
    e.SubElement(r,"email").text = d["email"]
    e.SubElement(r,"age").text = str(d["age"])
    e.SubElement(r,"DOB").text = str(d["DOB"])
    
    # project = e.SubElement(r,"Projects")
    # for z in d["Projects"]:
    #     e.SubElement(project,"Topic").text = z["Topic"]
    #     e.SubElement(project,"Category").text = z["Category"]
    #     e.SubElement(project,"Months").text = str(z["Months"])

    a = e.ElementTree(r) 
    a.write("json_to_xml.xml")
    
    return JsonResponse(data,safe = False)
