from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.views import APIView

from django_filters import rest_framework as filters
import django_filters.rest_framework

from rest_framework import generics
from test1.models import testserial,showdata
from rest_framework.response import Response
from .serializers import *
import csv
from django.conf import settings

# from iteration_utilities import unique_everseen
from word2number import w2n
import difflib  
from difflib import SequenceMatcher
import os  
import sys
import re
import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.toolkit.text.regular_expression_text_extraction import RegularExpressionTextExtraction, PDFMatch
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
from borb.toolkit.location.location_filter import LocationFilter
from decimal import Decimal

from dateutil.parser import parse 

class Deatilviews(APIView):

    serializer_class=Poi
    
    def get(self,request):

        queryset=testserial.objects.all()
        serializer = Poi(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer_class=self.serializer_class(data=request.data)
        serializer_class.is_valid()
        serializer_class.save()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class UpdateDeatils(APIView):

    def get_object(self,id):
        try:
            return testserial.objects.get(id=id)
        except testserial.DoesNotExist:
            raise Http404
            
    def get(self, request,id, format=None):
        snippet = self.get_object(id)
        serializer =Poi(snippet)
        return Response(serializer.data)
    
    def patch(self, request,id, *args, **kwargs):
        snippet = self.get_object(id)
        serializer = Poi(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def store(self):
    with open('media/data1.csv', 'r') as f:
        csv_reader = csv.DictReader(f)
            
        # csv_reader = csv.DictReader(unique_everseen(f))
        for row in csv_reader:
            model=showdata.objects.create(
                    name=row.get('Name',''),
                    email=row.get('Email',''),
                    )
     
            model.save()
        
        
        for row in showdata.objects.all():
            
            if showdata.objects.filter(email=row.email).count() > 1:
                row.delete()
                    

class showcsv(APIView):
    
    def get(self,request):
        queryset=showdata.objects.all()
        serializer = Csvserializer(queryset, many=True)
        return Response(serializer.data)


class PutData(APIView):
   
    def get_object(self, id):
        try:
            return testserial.objects.get(id=id)
        except testserial.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = Poi(snippet)
        return Response(serializer.data)
    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = Poi(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class showall(APIView):
    
    def get(self,request):
        queryset=testserial.objects.all()
        serializer = Poi(queryset, many=True)
        return Response(serializer.data)

class ModelFilter(django_filters.FilterSet):
    field1= django_filters.ModelChoiceFilter(queryset=testserial.objects.all())
    class Meta:
        model = testserial
        fields = {
            'field3' : ['exact'],
            'field2' : ['exact']
        }


class Demoview(APIView):
    serializer_class = NewSerializer

    # def get(self, request):
    #     queryset = Plo.objects.all()
    #     print(queryset)
    #     serializer = DemoSerializer(queryset, many = True)
    #     return Response(serializer.data)

    def post(self,  request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid()
        serializer.save()  

        try:
            value=serializer.data['file']
            value1 = str(settings.BASE_DIR)+value
            print(value1)
            d: typing.Optional[Document] = None
            b: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Billing Address :")
            m: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice Number :")
            n: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice Date :")
            u: RegularExpressionTextExtraction = RegularExpressionTextExtraction("State/UT Code:")
            f: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Amount in Words:")
            rup: RegularExpressionTextExtraction = RegularExpressionTextExtraction("TOTAL:")
            main_dict={}
            main_file=open(value1, "rb")
            legderlist=["Digital Documentation Systems"]
            # mod=ladgernamedata.objects.all()
            # for a in mod:
            #     legderlist.append(a.ledeger_name)
            try:
                if b:
                    d = PDF.loads(main_file, [b])
                    assert d is not None
                    matches: typing.List[PDFMatch] = b.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(180),
                                                data.get_y() - Decimal(100),
                                                Decimal(400),
                                                Decimal(100))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)
                    d = PDF.loads(main_file, [l0])
                    assert d is not None
                    y=l1.get_text_for_page(0)
                    print(y)
                    data=''
                    for leg in legderlist:
                        if leg[:4] in y:
                            data=leg
                fff = main_dict['Buyer Data']=data
                print(data)
            except:
                pass
                
            try:
                if m:
                    d = PDF.loads(main_file, [m])
                    assert d is not None
                    matches: typing.List[PDFMatch] = m.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                            data.get_y() - Decimal(5),
                                            Decimal(400),
                                            Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])
                    assert d is not None
                    y=l1.get_text_for_page(0)
                    aaa = main_dict['Invoice Number']=y.replace('Invoice Number :', '')
            except:
                    pass

            try:
                if n:
                    d = PDF.loads(main_file, [n])
                    assert d is not None
                    matches: typing.List[PDFMatch] = n.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                            data.get_y() - Decimal(5),
                                            Decimal(400),
                                            Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                    z=l1.get_text_for_page(0)
                bbb=main_dict['Invoice Date']=z.replace('Invoice Date :', '')
            
            except:
                pass
            

            try:
                if u:
                    d = PDF.loads(main_file, [u])
                    assert d is not None
                    matches: typing.List[PDFMatch] = u.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                        data.get_y() - Decimal(5),
                                        Decimal(400),
                                        Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                ccc = main_dict['Code']=l1.get_text_for_page(0).replace('State/UT Code:', '')
                

            except:
                pass
            try:
                if f:
                    d = PDF.loads(main_file, [f])
                    assert d is not None
                    matches: typing.List[PDFMatch] = f.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(100),
                                    data.get_y() - Decimal(20),
                                    Decimal(400),
                                    Decimal(10))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                    y=l1.get_text_for_page(0)
                    try:
                        main_total=w2n.word_to_num(y)
                    except Exception as e:
                        nex_txt=''
                        for i,letter in enumerate(y):
                            if i and letter.isupper():
                                nex_txt+=' '
                            nex_txt+=letter
                        main_total=w2n.word_to_num(nex_txt)
                ddd =main_dict['Total']=str(main_total)
            except:
                pass
            try:
                if rup:
                    d = PDF.loads(main_file, [rup])
                    assert d is not None
                    matches: typing.List[PDFMatch] = rup.get_matches_for_page(0)
                    assert len(matches) >= 0
                    data=matches[0].get_bounding_boxes()[0]
                    r: Rectangle = Rectangle(data.get_x() - Decimal(100),
                                    data.get_y() - Decimal(10),
                                    Decimal(575),
                                    Decimal(20))
                    l0: LocationFilter = LocationFilter(r)
                    l1: SimpleTextExtraction = SimpleTextExtraction()
                    l0.add_listener(l1)

                    d = PDF.loads(main_file, [l0])

                    assert d is not None
                    z=l1.get_text_for_page(0)
                    new=z.replace('�','')
                eee = main_dict['GST Total']=new.replace('TOTAL:', '')
            except:
                pass
            inv=Plo.objects.latest('id')
            inv.Buyer_data=fff
            inv.In=aaa
            inv.In_date=bbb    
            inv.C=ccc
            inv.T = ddd
            inv.G=eee
            inv.save()
        except:
            inv=Plo.objects.latest('id')
            inv.delete()
        print(main_dict)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    