

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required
def profile_update(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'update_profile_confirm.html', {'form': form})
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})
