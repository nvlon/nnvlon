from django . http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . import models , forms

def car_list_view(request):
    car_object = models.Car.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})

def car_detail_view(request, id):
    car_detail = get_object_or_404(models.Car, id = id)
    return render(request, 'car_detail.html', {'car_detail': car_detail})


#Добавление машин через формы
def create_car_views(request):
    method = request.method
    if method == 'POST':
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Машина успешно добавлена!</h2>')

    else:
        form = forms .CarForm()

        return render(request , 'car_list.html', {'form': form})




#Изменение данных о машине

def update_car_view(request, id):
    car_object = get_object_or_404(models.Car , id=id)
    if request.method == 'POST':
        form = forms.CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Машина успешно обновлена!</h2>')
    else:
        form = forms.CarForm(instance=car_object)
        return  render(request, 'update_car_list.html', {
            'form': form,
            'object': car_object
        })

#Удаление из базы
def delete_car_view(request, id):
    car_object = get_object_or_404(models.Car, id= id)
    car_object.delete()
    return HttpResponse('<h2> Машина успешно удалена!<h2>')

