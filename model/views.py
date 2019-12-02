from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from . import forms
from . import c
from django.core.files.storage import FileSystemStorage
flag = False
obj = c.checker()
def index(request):
	global flag
	if not flag:
		obj.run()
		flag =True
	form = forms.uploadform()
	if request.method=='POST':
		form = forms.uploadform(request.POST,request.FILES)
		if form.is_valid():
			myfile = form.cleaned_data['file']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			#uploaded_file_url = fs.url(filename)
        	#return render(request, 'model/index.html', {'uploaded_file_url': uploaded_file_url})
			ans = obj.testing()
			fs.delete(myfile.name)
			if ans[0][0]>0.5:
				return HttpResponse('<html><body bgcolor="RED"><div><style>div {position: fixed;top: 40%;left: 40%;}</style><h1>MALIGNANT</h1></div></body></html>')
			else:
				return HttpResponse('<html><body bgcolor="GREEN"><div><style>div {position: fixed;top: 40%;left: 40%;}</style><h1>BENIGN</h1></div></body></html>')
		return render(request, 'model/index.html', {'form': form, 'error': 1})
	return render(request,'model/index.html',{'form':form,'error':0})

