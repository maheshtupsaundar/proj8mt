from django import forms
class productform(forms.Form):
    pid=forms.IntegerField(label='enter pid')
    pname = forms.CharField(label='enter pname',max_length=20)
    pcost=forms.DecimalField(label="enter pcost",max_digits=10,decimal_places=4)
    pmfdt=forms.DateField(label="enter pmfdt")
    pexpdt=forms.DateField(label="enter pexpdt")