from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from datetime import date, timedelta, datetime


@login_required
def req_new(request):
    context = {}
    sent = False

    adminemail = "gnandy@unomaha.edu"
    email_r = request.user.email
    if request.method == "POST":

        uid_r = request.user.id
        category_type = request.POST.get('category_type')
        dt = request.POST.get('request_date')
        request_date = datetime.strptime(dt, '%Y-%m-%d').date()
        location_type = request.POST.get('location_type')
        full_description = request.POST.get('full_description')
        created = Request.objects.create(username_id=uid_r, category_type=category_type, request_date=request_date,
                                         location_type=location_type,
                                         full_description=full_description, status='New')
        subject: str = "Lakeview Apartment Maintainence Request"
        message = f"Your maintainence request has been submitted \nOnce your request is processed you should recieve another email.\n\nThank you, LAM Staff. "
        message2 = f"New maintainence request has been submitted. Please take necessary action."
        msg1 = (subject, message, 'lakeviewapartment1@gmail.com', [email_r])
        msg2 = (subject, message2, 'lakeviewapartment1@gmail.com', [adminemail])
        send_mass_mail((msg1, msg2), fail_silently=False)
        sent = True

        return render(request, 'submit_request.html', {'sent': sent, 'email_r': email_r})
    else:
        form = RequestForm()
    return render(request, 'add_req.html', {'form': form})


@login_required
def req_list(request):
    username_r = request.user.id
    reqs = Request.objects.filter(username=username_r)
    return render(request, 'req_list.html', {'reqs': reqs})


@login_required
def admin_req_list(request):
    reqs = Request.objects.filter()
    return render(request, 'admin_req_list.html', {'reqs': reqs})


@login_required
def req_approve(request, pk):
    reqs = get_object_or_404(Request, pk=pk)
    reqs.status = 'In-progress'
    reqs.save()
    reqs = Request.objects.filter()
    return render(request, 'admin_req_list.html', {'reqs': reqs})


@login_required
def req_delivered(request, pk):
    reqs = get_object_or_404(Request, pk=pk)
    reqs.status = 'Completed'
    reqs.save()
    reqs = Request.objects.filter()
    return render(request, 'admin_req_list.html', {'reqs': reqs})


@login_required
def req_edit(request, pk):
    reqs = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=reqs)
        if form.is_valid():
            reqs = form.save()
            reqs.save()
            reqs = Request.objects.filter()
            return render(request, 'req_list.html', {'reqs': reqs})
    else:
        # print("else")
        form = RequestForm(instance=reqs)
    return render(request, 'req_edit.html', {'form': form})


@login_required
def req_delete(request, pk):
    reqs = get_object_or_404(Request, pk=pk)
    reqs.delete()
    return redirect('req_list')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'update_password_confirmation.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
