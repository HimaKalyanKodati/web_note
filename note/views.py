from django.shortcuts import render,redirect

from . import models
from .forms import dataForm

#importing classbasedviews
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here.
# def showNote(request):
#     data = models.Note.objects.all()
    
#     # if request.method == "GET":
#     #     form_data = dataForm(request.POST or None)
#     #     return render(request,'index.html',form_data)
    
#     # if request.method == "POST":
#     #     data_from = dataForm(request.POST or None)
#     #     if dataForm.is_valid():
#     #         data_from.save()
#     #         return redirect('noteapp:show')
    
#     context = {'notes':data}
#     return render(request,'index.html',context)

class showNote(ListView):
    model = models.Note
    template_name = 'index.html'
    context_object_name = 'notes'

# def editNote(request,note_id):
#     data = models.Note.objects.get(id=note_id)
    
#     data_form = dataForm(request.POST or None, instance=data)
    
#     if data_form.is_valid():
#         data_form.save()
#         return redirect('noteapp:show')
    
#     return render(request,'edit_note.html',{'data_form':data_form})

class editNote(UpdateView):
    model = models.Note
    template_name = 'edit_note.html'
    form_class = dataForm
    success_url = '/'
    
    def form_valid(self, form):
        form
        return super().form_valid(form)
    
# def createNote(request):
#     data_form = dataForm(request.POST or None)
    
#     if data_form.is_valid():
#         data_form.save()
#         return redirect('noteapp:show')
    
#     return render(request,'edit_note.html',{'data_form':data_form})

class createNote(CreateView):
    model = models.Note
    template_name = 'edit_note.html'
    form_class = dataForm
    success_url = '/'
    
    def form_valid(self, form):
        form
        return super().form_valid(form)
    

# def deleteNote(request,note_id):
#     data = models.Note.objects.get(id=note_id)
    
#     if request.method == 'POST':
#         data.delete()
#         return redirect('noteapp:show')
    
#     return render(request,'delete.html',{'data':data})

class deleteNote(DeleteView):
    model = models.Note
    template_name = 'delete.html'
    success_url = '/'