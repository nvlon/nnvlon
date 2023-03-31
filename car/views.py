from django . http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . import models , forms
from django. views.generic import CreateView, ListView,  DeleteView, UpdateView,DetailView


#неполная информация о товаре

class CarListView(ListView):
    template_name =  'car_list.html'
    queryset = models.Car.objects.all()
    def get_queryset(self):
        return models.Car.objects.all()


# def car_list_view(request):
#     car_object = models.Car.objects.all()
#     return render(request, 'car_list.html', {'car_object': car_object})

#полная информация об обьектк ро id
class CarDetailView(DetailView):
    template_name = 'car_detail.html'
def get_object(self, **kwargs):
    car_id = self.kwargs.get('id')
    return get_object_or_404(models.Car, id=car_id)


# def car_detail_view(request, id):
#     car_detail = get_object_or_404(models.Car, id = id)
#     return render(request, 'car_detail.html', {'car_detail': car_detail})


#Создание обьектов через формы

class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = forms.CarForm
    queryset = models.Car.objects.all()
    success_url = '/car_list/'

def form_valid(self,form):
    print(form.cleaned_data)
    return super (CreateCarView,self).form_valid(form=form)


# def create_car_views(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>Машина успешно добавлена!</h2>')
#
#     else:
#         form = forms .CarForm()
#
#         return render(request , 'car_list.html', {'form': form})




#редактирование

class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    form_class = forms.CarForm
    success_url = '/car_list/'

def get_odject(self, **kwargs):
    car_id= self.kwargs.get('id')
    return get_object_or_404(models.Car, id=car_id)



def form_valid(self, form):
    return super(CarUpdateView,self).form_valid(form=form)

# def update_car_view(request, id):
#     car_object = get_object_or_404(models.Car , id=id)
#     if request.method == 'POST':
#         form = forms.CarForm(instance=car_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2> Машина успешно обновлена!</h2>')
#     else:
#         form = forms.CarForm(instance=car_object)
#         return  render(request, 'update_car_list.html', {
#             'form': form,
#             'object': car_object
#         })

#Удаление из базы
class CarDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/car_list/'

def get_object(self, **kwargs):
    car_id = self.kwargs
    return get_object_or_404(models.Car , id=car_id)




#def delete_car_view(request, id):
#     car_object = get_object_or_404(models.Car, id= id)
#     car_object.delete()
#     return HttpResponse('<h2> Машина успешно удалена!<h2>')

