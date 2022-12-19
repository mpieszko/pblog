from django.shortcuts import render
from django.views.generic import ListView
from apps.noticia.models import Noticia


def Nosotros(request):
    return render(request,'nosotros.html')

#-----View de la pág con el formulario para contactos:
from apps.noticia.forms import ContactoForm
def Contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            #post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
#-----


#    form = ContactoForm()
#    return render(request,'contacto.html', {'form' : form})

#   data = {
#       'form' : ContactoForm()
#   }
#   return render(request,'contacto.html', data)

class NoticiaListView(ListView):
    model = Noticia
    template_name = 'index.html'

#class NoticiaListView(ListView):
 #   model = Noticia
  #  template_name = 'index.html'




#def Index(request):
#   return render(request, 'index.html')
#
#def Nosotros(request):
#    return render(request, 'nosotros.html')-->