from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ImageForm
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def ServicesPageView(request):
    template_name = 'services.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template_name, context)

def NewPostView(request):
    template_name = 'newpost.html'
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = ImageForm()

    return render(request, template_name, {'form': form})
