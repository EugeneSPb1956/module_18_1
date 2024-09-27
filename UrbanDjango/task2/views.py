from django.shortcuts import render

# Create your views here.
# from .models import

# Create your views here.
def class_view(request):
    return render(request, 'second_task/class_template.html')

    # artists = list(Artists.objects.all())  #  Получаем QuerySet
    # return render(request, 'index.html', context={'artists': artists,})
    #                                               # 'artist2': artists[1],})  # context={'artists': artists}

# def artist_view(request):
#     pass

def func_view(request):
    return render(request, 'second_task/func_template.html')

    # albums = list(Albums.objects.all())  #  Получаем QuerySet using filter
    # artists = list(Artists.objects.all())  #  Получаем QuerySet

    # name_id = Artists.objects.filter(name=name)
    # name_id = name_id[0].id
    # print(name_id)
    # albums = Albums.objects.filter(artists_id=name_id)
    # return render(request, 'album_view.html', context={'name': name, 'albums': albums,})

