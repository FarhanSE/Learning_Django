from django.shortcuts import render
from .models import Profiles

# Create your views here.
def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def single_profile(request, pk):
    profile = Profiles.objects.get(id=pk)
    topskills = profile.skills_set.exclude(description__exact="")
    otherskills = profile.skills_set.filter(description="")
    context = {'profile':profile, "topskills":topskills, "otherskills":otherskills}
    return render(request, 'users/single_profile.html', context)