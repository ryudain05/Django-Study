from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        # context = {"user": user, "perms": perms}
        return render(request, 'home.html')

# Create your views here.
