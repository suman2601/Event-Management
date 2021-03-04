from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Eventlist, EventBook

# from event.form import EventForm
# from django.views.generic.edit import FormView
# from  django.views.generic import ListView

# Create your views here.


def home(request):
    context = {
        'eventlist': Eventlist.objects.all().order_by('StartingDate')
    }
    return render(request, 'event/home.html', context)


@login_required
def event_view(request):
    if request.method == 'POST':
        postby = request.user
        event_title = request.POST['event_title']
        category = request.POST['Category']
        description = request.POST['description']
        organizer = request.POST['organizer']
        venue = request.POST['venue']
        starting_date = request.POST['starting_date']
        ending_date = request.POST['ending_date']
        duration = request.POST['duration']
        fee = request.POST['fee']
        price = request.POST['price']
        numberofparticipants = request.POST['numberofparticipants']
        link = request.POST['link']
        numberofseats = request.POST['numberofseats']

        obj = Eventlist(postby=postby, title=event_title, description=description, organizer=organizer, joiningfees=fee, pricemoney=price, members=numberofparticipants,
                        link=link, Eventtime=duration, venue=venue, StartingDate=starting_date, Endingdate=ending_date, Category=category, numberofseats=numberofseats)

        obj.save()
        return redirect('/')
    else:
        requser = request.user
        obj1 = Eventlist.objects.filter(postby=requser)
        # # print(obj1)
        return render(request, 'event/event_view.html', {'obj': obj1})


@login_required
def event_add(request):
    return render(request, 'event/event_add.html', {})


@login_required
def event_update(request, my_id):
    if request.method == 'POST':
        obj = Eventlist.objects.get(id=my_id)
        return render(request, 'event/event_update.html', {'obj': obj})


@login_required
def event_updated(request, my_id):
    if request.method == 'POST':
        Eventlist.objects.filter(pk=my_id).update(postby=request.user, title=request.POST['event_title'], Category=request.POST['Category'], description=request.POST['description'], organizer=request.POST['organizer'], joiningfees=request.POST['fee'], venue=request.POST[
            'venue'], StartingDate=request.POST['starting_date'], Endingdate=request.POST['ending_date'], Eventtime=request.POST['duration'], pricemoney=request.POST['price'], members=request.POST['numberofparticipants'], link=request.POST['link'], numberofseats=request.POST['numberofseats'])
        return redirect('/event_view')
    else:
        requser = request.user
        obj1 = Eventlist.objects.filter(postby=requser)
        return render(request, 'event/event_view.html', {'obj1': obj1})


@login_required
def event_delete(request, my_id):
    obj = get_object_or_404(Eventlist, id=my_id)
    obj1 = get_object_or_404(EventBook, eventid=my_id)
    obj.delete()
    obj1.delete()
    return redirect('/event_view')


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def event_details(request, my_id):
    obj = Eventlist.objects.get(id=my_id)
    uid = request.user.id
    try:
        obj1 = EventBook.objects.get(eventid=my_id, userid=uid)
    except EventBook.DoesNotExist:
        obj1 = None

    return render(request, 'event/event_details.html', {'obj': obj, 'obj1': obj1})


def user_details(request, username):
    obj = User.objects.get(username=username)
    return render(request, 'event/userdetail.html', {'obj': obj})


@login_required
def book_request(request, e_id):
    requsrid = request.user.id
    obj = EventBook.objects.filter(userid=requsrid, eventid=e_id)
# if empty then and then add new obj
    if obj:
        return redirect('/')
    else:
        eventid = e_id
        book = True
        obj = EventBook(userid=requsrid, eventid=eventid, booking=book)
        obj.save()
        return redirect('/')


def event_user(request, event_id):
    obj = EventBook.objects.filter(eventid=event_id)
    eventdetail = Eventlist.objects.filter(id=event_id)
    userdetail = User.objects.filter()
    eventid = event_id
    return render(request, 'event/manageEventUser.html', {'obj': obj, 'eventdetail': eventdetail, 'userdetail': userdetail, 'eventid': eventid})


def event_user_conformation(request, event_id, user_id):
    EventBook.objects.filter(
        userid=user_id, eventid=event_id).update(booking_confirmed=True)
    return redirect('event_user', event_id=str(event_id))


def event_user_unbooked(request, event_id, user_id):
    EventBook.objects.filter(
        userid=user_id, eventid=event_id).update(booking=True, booking_confirmed=False, attended=False, certificate='')
    return redirect('event_user', event_id=str(event_id))


def event_user_attended(request, event_id, user_id):
    EventBook.objects.filter(
        userid=user_id, eventid=event_id).update(attended=True)
    return redirect('event_user', event_id=str(event_id))


def event_user_certified(request, event_id, user_id):
    # after 1hr this query get solved !!!!! hahahha
    img = request.FILES['myfile']
    obj = EventBook.objects.get(
        userid=user_id, eventid=event_id)
    obj.certificate = img
    obj.save()
    return redirect('event_user', event_id=str(event_id))


def my_event(request):
    return render(request, 'event/myevent.html')


def my_event_requested(request):
    uid = request.user.id
    obj = EventBook.objects.filter(userid=uid, booking=True)
    objl = []
    for i in obj:
        temp = Eventlist.objects.get(id=i.eventid)
        objl.append(temp)

    return render(request, 'event/my_event_requested.html', {'objl': objl})


def my_event_conformed(request):
    uid = request.user.id
    obj = EventBook.objects.filter(userid=uid, booking_confirmed=True)
    objl = []
    for i in obj:
        temp = Eventlist.objects.get(id=i.eventid)
        objl.append(temp)

    return render(request, 'event/my_event_conformed.html', {'objl': objl})


def my_event_attended(request):
    uid = request.user.id
    obj = EventBook.objects.filter(userid=uid, attended=True)
    objl = []

    for i in obj:
        temp = Eventlist.objects.get(id=i.eventid)
        objl.append(temp)
    mylist = zip(objl, obj)
    for x in obj:
        print(x.certificate.url)
    return render(request, 'event/my_event_attended.html', {'mylist': mylist})
