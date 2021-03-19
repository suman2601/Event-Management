from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from event.models import Eventlist, EventBook

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} registered successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        p_form = ProfileUpdateForm()
    return render(request, 'users/register.html', {'form': form, 'p_form': p_form})


# numberofupdates
check = False
@login_required
def profile(request):
    global check
    u = request.user
    num = int(u.profile.numberofupdates)
    if request.method == 'POST':
        num = num+1
        if num == 1:
            check = True
        s = str(num)
        u.profile.numberofupdates = s
        u.profile.save()
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():

            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        if num < 1:
            check = False
        else:
            check = True
# MAIN
    uid = request.user.id
    # def my_event_requested(request):
    obj = EventBook.objects.filter(userid=uid, booking=True)
    objl = []
    for i in obj:
        temp = Eventlist.objects.get(id=i.eventid)
        objl.append(temp)

    # def my_event_conformed(request):
    objc = EventBook.objects.filter(userid=uid, booking_confirmed=True)
    obj2 = []
    for i in objc:
        temp = Eventlist.objects.get(id=i.eventid)
        obj2.append(temp)

    # def my_event_attended(request):
    obja = EventBook.objects.filter(userid=uid, attended=True)
    obj3 = []

    for i in obja:
        temp = Eventlist.objects.get(id=i.eventid)
        obj3.append(temp)
    mylist = zip(obj3, obja)
    for x in obja:
        print(x.certificate.url)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'check': check,
        'objl': objl,
        'obj2': obj2,
        'mylist': mylist,
    }
    return render(request, 'users/profile.html', context)
