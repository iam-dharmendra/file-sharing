from django.db import models


class testserial(models.Model):

    field1=models.CharField(default='',max_length=12)
    field2=models.CharField(default='',max_length=12)
    field3=models.CharField(default='',max_length=12)

    def __str__(self) -> str:
        return str(self.field1)

class showdata(models.Model):

    name=models.CharField(default='',max_length=50,verbose_name='Your_Name')
    email=models.CharField(default='',max_length=50,verbose_name='Your_Email')

    def __str__(self) -> str:
        return str(self.id)


class InvoiceToDB(models.Model):
    cmpname= models.CharField(null=True,blank=True, max_length=50, verbose_name = "company Name")
    invoiceNo= models.CharField(null=True,blank=True, max_length=50, verbose_name = "Invoice Number")
    date= models.DateField(null=True, blank=True, verbose_name = 'Invoice Date')
    gstRegistrationNo = models.CharField(null=True,blank=True, max_length=50, verbose_name = "GST Registration No")
    
    def __str__(self):
        return str(self.cmpname)


class Comp(models.Model):
    cn = models.CharField(max_length=50, verbose_name='Company_Name')
    def __str__(self) -> str:
        return self.cn

class Plo(models.Model):
    company = models.ForeignKey(Comp, on_delete=models.CASCADE,null=True,blank=True)
    Buyer_data = models.CharField(max_length=50)
    In = models.CharField(max_length=50, verbose_name="Invoice Number", unique=True)
    In_date = models.CharField(max_length=50, verbose_name="Invoice Date")
    C = models.CharField(max_length=50, verbose_name="State Code")
    T = models.CharField(max_length=50, verbose_name="Total")
    G = models.CharField(max_length=50, verbose_name="GST Toal")
    file = models.FileField(upload_to='in/',default='', null=True)
  
    def __str(self):
        return(self.Buyerdata)
