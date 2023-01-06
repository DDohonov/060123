from django.shortcuts import render, redirect
from .models import *
# Create your views here.

# def main(request):
#     forms = Form.objects.all()
#     # print(forms.students)
#     context = {
#         'forms': forms,
#     }
#     return render(request, 'app1/base.html', context)

def main(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        return redirect(f'/{link}') # '/' + link
    forms = Form.objects.all()
    forms_list = []
    for i in forms:
        forms_list.append({'form': i, 'students': i.students.all()})
    # print(forms.students)
    context = {
        'forms': forms_list,
    }
    return render(request, 'app1/base.html', context)