from django.http import HttpResponse
from django.shortcuts import render
from film_app.models import*
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request,'index.html')

def admin_home(request):
    return render(request,'admin_home.html')
def theater_home(request):
    return render(request,'theater_home.html')

def producer_home(request):
    return render(request,'producer_home.html')

def log(request):
    
    if "sub" in request.POST:
        print("HHH")
        username=request.POST['uname']
        password=request.POST['pwd']
        
        
        
        res=Login.objects.get(username=username,password=password)
        request.session['lid']=res.pk
        
        if res.usertype == 'admin':
            return HttpResponse("<script>alert('login success !');window.location='admin_home'</script>")            
        elif res.usertype == 'theater':
            obj=Theater.objects.get(login_id=request.session['lid'])
            request.session['tid']=obj.pk
            return HttpResponse("<script>alert('login success !');window.location='theater_home'</script>")   
        elif res.usertype == 'producer':
            obj=Production.objects.get(login_id=request.session['lid'])
            request.session['pid']=obj.pk
            return HttpResponse("<script>alert('login success !');window.location='producer_home'</script>")  
        else: 
            return HttpResponse("<script>alert('Invalide Username And Password !');window.location='login'</script>")  
                
                  
        
    return render(request,'login.html')

def admin_view_theater(request):
    n=Theater.objects.all()
    
    return render(request,'admin_view_theater.html',{'data':n})
def theater_view_payment(request):
    
    n=Payment.objects.all()
    
    return render(request,'admin_view_theater.html',{'data':n})

def admin_view_customer(request):
    n=Customer.objects.all()
    
    return render(request,'admin_view_customer.html',{'data':n})


def admin_manage_type(request):
    if 'sub' in request.POST:
        tyname=request.POST['type']
        cc=Type(type_name=tyname)
        cc.save()
        return HttpResponse("<script>alert('Type added');window.location='/admin_manage_type'</script>")
        
    


    n=Type.objects.all()
    return render(request,'admin_manage_type.html',{'data':n})

def type_delete(request,t_id):
    a=Type.objects.get(id=t_id)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_type'</script>")

def type_update(request,id):
    up=Type.objects.get(id=id)
    if 'update' in request.POST:
        tyname=request.POST['type']
        up.type_name=tyname
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_type'</script>")

        
        
    return render(request,'admin_manage_type.html',{'check':up})


def admin_manage_movie(request):
    if 'sub' in request.POST:
        fname=request.POST['film']
        rel=request.POST['date']
        tid=request.POST['type_name']
        des=request.POST['desc']
        dur=request.POST['time']
        post=request.FILES['img']
        k=FileSystemStorage()
        image=k.save(post.name,post)
        cc=Film(film_name=fname,film_release=rel,film_desc=des,duration=dur,type_id=tid,image=image)
        cc.save()
        return HttpResponse("<script>alert('Film added');window.location='/admin_manage_movie'</script>")
        
    

    n=Film.objects.all()

    y=Type.objects.all()
    return render(request,'admin_manage_movie.html',{'data':n,'d':y})

def film_delete(request,f_id):
    a=Film.objects.get(id=f_id)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_movie'</script>")

def film_update(request,id):
    a=Type.objects.all()
    up=Film.objects.get(id=id)
    if 'update' in request.POST:
        fname=request.POST['film']
        rel=request.POST['date']
        des=request.POST['desc']
        dur=request.POST['time']
        post=request.FILES['img']
        k=FileSystemStorage()
        image=k.save(post.name,post)
        up.film_name=fname
        up.film_release=rel
        up.film_desc=des
        up.duration=dur
        up.image=image
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_movie'</script>")

        
        
    return render(request,'admin_manage_movie.html',{'check':up,'d':a})


def admin_manage_timing(request):
    if 'sub' in request.POST:
        tname=request.POST['name']
        ti=request.POST['time']
       

        cc=Timing(timing_name=tname,time=ti)
        cc.save()
        return HttpResponse("<script>alert('Timing added');window.location='/admin_manage_timing'</script>")
        
    

    n=Timing.objects.all()

    
    return render(request,'admin_manage_timing.html',{'data':n})

def timing_delete(request,tid):
    a=Timing.objects.get(id=tid)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_timing'</script>")

def timing_update(request,id):
    up=Timing.objects.get(id=id)
    if 'update' in request.POST:
        tname=request.POST['name']
        ti=request.POST['time']
       
        up.timing_name=tname
        up.time=ti
        
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_timing'</script>")

        
        
    return render(request,'admin_manage_timing.html',{'check':up})


def admin_manage_seat(request):
    if 'sub' in request.POST:
        sname=request.POST['name']
        sdes=request.POST['desc']
       

        cc=Seattype(seat_type=sname,desc=sdes)
        cc.save()
        return HttpResponse("<script>alert('Seat Type added');window.location='/admin_manage_seat'</script>")
        
    

    n=Seattype.objects.all()

    
    return render(request,'admin_manage_seat.html',{'data':n})

def seat_delete(request,sid):
    a=Seattype.objects.get(id=sid)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/admin_manage_seat'</script>")

def seat_update(request,id):
    up=Seattype.objects.get(id=id)
    if 'update' in request.POST:
        sname=request.POST['name']
        sdes=request.POST['desc']
       
        up.seat_type=sname
        up.desc=sdes
        
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/admin_manage_seat'</script>")

        
        
    return render(request,'admin_manage_seat.html',{'check':up})


def theater_reg(request):
    
    if 'submit' in request.POST:
        fname=request.POST['name']
        cityy=request.POST['city']
        pinc=request.POST['pin']
        phn=request.POST['phone']
        emai=request.POST['email']

        us=request.POST['uname']
        pd=request.POST['pwd']
        
        logs=Login(username=us,password=pd,usertype='theater')
        logs.save()
        ureg=Theater(name=fname,city=cityy,pin=pinc,phone=phn,email=emai,login_id=logs.pk)
        ureg.save()
        return HttpResponse("<script>alert('Registered');window.location='/login'</script>")

    return render(request,'theater_reg.html')


def theater_manage_screen(request):
    if 'sub' in request.POST:
        scname=request.POST['name']
        ns=request.POST['seat']
       

        cc=Screen(screen_name=scname,no_seats=ns)
        cc.save()
        return HttpResponse("<script>alert('Screen added');window.location='/theater_manage_screen'</script>")
        
    

    n=Screen.objects.all()

    
    return render(request,'theater_manage_screen.html',{'data':n})

def screen_delete(request,scid):
    a=Screen.objects.get(id=scid)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/theater_manage_screen'</script>")

def screen_update(request,id):
    up=Screen.objects.get(id=id)
    if 'update' in request.POST:
        scname=request.POST['name']
        ns=request.POST['seat']
       
        up.screen_name=scname
        up.no_seats=ns
        
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/theater_manage_screen'</script>")

        
        
    return render(request,'theater_manage_screen.html',{'check':up})


def theater_manage_seating(request,id):
    a=Screen.objects.get(id=id)
    if 'sub' in request.POST:
        rname=request.POST['row']
        se=request.POST['num']
        tid=request.POST['type_name']
        rat=request.POST['rate']
       

        cc=Seating(row_name=rname,seat_number=se,rate=rat,seat_type_id=tid,screen_id=a.pk)
        cc.save()
        return HttpResponse(f"<script>alert('Seating added');window.location='/theater_manage_seating/{id}'</script>")
        
    

    n=Seating.objects.all()

    y=Type.objects.all()
    return render(request,'theater_manage_seating.html',{'data':n,'d':y})

def seating_delete(request,seid):
    a=Seating.objects.get(id=seid)
    a.delete()
    return HttpResponse(f"<script>alert('Deleted');window.location='/theater_manage_seating/{a.screen.id}'</script>")

def seating_update(request,id):
    a=Type.objects.all()
    up=Seating.objects.get(id=id)
    if 'update' in request.POST:
        rname=request.POST['row']
        se=request.POST['num']
        rat=request.POST['rate']
        up.row_name=rname
        up.seat_number=se
        up.rate=rat
       
        up.save()
        
        return HttpResponse(f"<script>alert('updated');window.location='/theater_manage_seating/{up.screen.id}'</script>")

        
        
    return render(request,'theater_manage_seating.html',{'check':up,'d':a})

def theater_allocate_film(request):
    a=Timing.objects.all()
    b=Screen.objects.all()
    c=Film.objects.all()


    if 'sub' in request.POST:
        fname=request.POST['filmname']
        sname=request.POST['screenname']
        tname=request.POST['timing']
        da=request.POST['date']
       
       
        p=Allocate(played_date=da,status='allocated',film_id=fname,screen_id=sname,timing_id=tname,theater_id=request.session['tid'])
        p.save()
        
        return HttpResponse("<script>alert('Allocated');window.location='/theater_home'</script>")

        
        
    return render(request,'theater_allocate_film.html',{'d':c,'o':a,'u':b})



def theater_view_booking(request):
    n=Booking.objects.all()
    
    return render(request,'theater_view_booking.html',{'data':n})

def theater_view_detail(request,id):
    n=Booking.objects.get(id=id)
    
    return render(request,'theater_view_detail.html',{'data':n})

def theater_view_customer(request,id):
    n=Booking.objects.get(id=id)
    
    return render(request,'theater_view_customer.html',{'data':n})


def producer_reg(request):
    
    if 'submit' in request.POST:
        fname=request.POST['name']
        cityy=request.POST['place']
        phn=request.POST['phone']
        emai=request.POST['email']

        us=request.POST['uname']
        pd=request.POST['pwd']
        
        logs=Login(username=us,password=pd,usertype='producer')
        logs.save()
        ureg=Production(team_name=fname,place=cityy,phone=phn,email=emai,login_id=logs.pk)
        ureg.save()
        return HttpResponse("<script>alert('Registered');window.location='/login'</script>")

    return render(request,'producer_reg.html')

def producer_manage_project(request):
    if 'sub' in request.POST:
        pname=request.POST['prj']
        pim=request.FILES['img']
        video=request.FILES['vdo']

        k=FileSystemStorage()
        photo=k.save(pim.name,pim) 
        
        a=FileSystemStorage()
        vdo=a.save(video.name,video)
        
        

        cc=Projects(project_name=pname,images=photo,production_id=request.session['pid'],videos=vdo)
        cc.save()
        return HttpResponse("<script>alert('Project Added');window.location='/producer_manage_project'</script>")
        
    


    n=Projects.objects.all()
    return render(request,'producer_manage_project.html',{'data':n})

def prj_delete(request,pid):
    a=Projects.objects.get(id=pid)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/producer_manage_project'</script>")

def prj_update(request,id):
    up=Projects.objects.get(id=id)
    if 'update' in request.POST:
        pname=request.POST['prj']
        pim=request.FILES['img']
        up.project_name=pname
        up.images=pim
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/producer_manage_project'</script>")

        
        
    return render(request,'producer_manage_project.html',{'check':up})


def producer_manage_oppor(request):
    if 'sub' in request.POST:
        tit=request.POST['title']
        deta=request.POST['det']
        pro_id=request.POST['pro_name']
       

        cc=Opportunities(title=tit,details=deta,project_id=pro_id)
        cc.save()
        return HttpResponse("<script>alert('opportunity added');window.location='/producer_manage_oppor'</script>")
        
    

    n= Opportunities.objects.all()

    y=Projects.objects.all()
    return render(request,'producer_manage_oppor.html',{'data':n,'d':y})

def oppor_delete(request,oid):
    a=Opportunities.objects.get(id=oid)
    a.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/producer_manage_oppor'</script>")

def oppor_update(request,id):
    a=Projects.objects.all()
    up=Opportunities.objects.get(id=id)
    if 'update' in request.POST:
        tit=request.POST['title']
        deta=request.POST['det']
       
        up.title=tit
        up.details=deta
       
        up.save()
        
        return HttpResponse("<script>alert('updated');window.location='/producer_manage_oppor'</script>")

        
        
    return render(request,'producer_manage_oppor.html',{'check':up,'d':a})


def producer_add_pref(request,id):
    a=Opportunities.objects.get(id=id)
    if 'sub' in request.POST:
        pre=request.POST['pref']
        a=Preference(preference=pre,Opportunity_id=id)
        a.save( )
        return HttpResponse("<script>alert('Added');window.location='/producer_manage_oppor'</script>")

    return render(request,'producer_add_pref.html')

def producer_view_request(request):
    n=Request.objects.all()
    
    return render(request,'producer_view_request.html',{'data':n})



#-----------------------Android----------------------------------


from django.http import JsonResponse
from .models import Login

def login(request):
    data = []
    status = "error"
    message = "Invalid credentials"

    androusername = request.GET.get('username')
    andropassword = request.GET.get('password')

    # Validate input
    if not androusername or not andropassword:
        return JsonResponse({'status': status, 'message': 'Username and password are required'})

    try:
        # Query Login table
        queryset = Login.objects.filter(username=androusername, password=andropassword)
        if not queryset.exists():
            return JsonResponse({'status': status, 'message': 'Invalid username or password'})

        # Process each matching login object
        for login_obj in queryset:
            data.append({
                'id': login_obj.id,
                'username': login_obj.username,
                'password': login_obj.password,
                'usertype': login_obj.usertype,
            })

        status = "success"

    except Exception as e:
       
        print(f"Error during login process: {e}")
        message = "An unexpected error occurred"

    # Build response
    response = {'status': status, 'data': data}
    if status == "error":
        response['message'] = message

    return JsonResponse(response)


from django.http import JsonResponse
from .models import Customer, Login

def registration(request):
    if request.method == 'GET': 
        firstname = request.GET.get('firstname')
        lastname = request.GET.get('lastname')
        gender = request.GET.get('gender')
        place = request.GET.get('place')
        district = request.GET.get('district')
        phone = request.GET.get('phone')
        pincode = request.GET.get('pincode')
        dob = request.GET.get('dob')
        username = request.GET.get('username')
        password = request.GET.get('password')

        if not all([firstname, lastname, place, gender, district, phone, pincode, dob, username, password]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)

        try:
          
            print(f"Data to be inserted: {firstname}, {lastname}, {gender}, {place}, {district}, {phone}, {pincode}, {dob}, {username}, {password}")

           
            login = Login.objects.create(username=username, password=password, usertype='cust')

            
            print(f"Login created with ID: {login.id}")

          
            customer = Customer.objects.create(
                login_id=login.pk,
                fname=firstname,
                lname=lastname,
                city=place,
                dist=district,
                pin=pincode,
                phone=phone,
                gender=gender,
                dob=dob  
            )

           
            print(f"Customer created with ID: {customer.id}")

            return JsonResponse({'status': 'success', 'message': 'Customer registered successfully.'})
        except Exception as e:
            
            print(f"Error during registration: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
from django.http import JsonResponse
from .models import Customer, Login

def producer_registration(request):
    if request.method == 'GET': 
        teamname = request.GET.get('name')
        place = request.GET.get('place')
        
        phone = request.GET.get('phone')
        email = request.GET.get('email')
        
        username = request.GET.get('username')
        password = request.GET.get('password')

        
           
        login = Login.objects.create(username=username, password=password, usertype='producer')

            
        print(f"Login created with ID: {login.id}")

          
        customer = Production.objects.create(
                login_id=login.pk,
                team_name=teamname,
                place=place,
                phone=phone,
                email=email,
               
            )

           
        print(f"Customer created with ID: {customer.id}")

           
        

    return JsonResponse({'status': 'success', 'message': 'Invalid request method.'})

from django.http import JsonResponse
from .models import Theater

def view_theaters(request):
    login_id = request.GET.get('login_id')

    
    theaters = Theater.objects.all()

    
    data = []
    for theater in theaters:
        data.append({
            'theater_id': theater.id,  
            'name': theater.name,
            'city': theater.city,
        })

    return JsonResponse({
        'method': 'ViewTheaters',
        'status': 'success',
        'data': data,
    })

    
    

from django.http import JsonResponse
from .models import Allocate, Film, Timing, Screen  




def get_movies_for_theater(request):
    theater_id = request.GET.get('theater_id')

    if not theater_id:
        return JsonResponse({"status": "error", "message": "Theater ID is required"})

    try:
        allocations = Allocate.objects.filter(theater_id=theater_id).select_related('film', 'timing', 'screen')

        if not allocations.exists():
            return JsonResponse({"status": "error", "message": "No movies found for this theater."})

        movie_data = []
        for allocation in allocations:
            movie_details = {
                "screen_id": allocation.screen.id,
                "film_name": allocation.film.film_name,
                "screen_name": allocation.screen.screen_name,
                "timing_name": allocation.timing.timing_name,
                "played_date": allocation.played_date,
                "time": allocation.timing.time,
                "image": allocation.film.image.url  
            }
            movie_data.append(movie_details)

        return JsonResponse({"status": "success", "data": movie_data})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})

 
from django.http import JsonResponse
from .models import Opportunities  


def get_opportunities(request):
    try:
        opportunities = Opportunities.objects.all()
        opportunities_data = []
        for opp in opportunities:
            opportunities_data.append({
                'title': opp.title,
                'details': opp.details,
                'project_id': opp.project_id,  
                 'opportunity_id': opp.id,  
            })

        return JsonResponse({'status': 'success', 'data': opportunities_data})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
from django.http import JsonResponse
from .models import Preference  


def get_preferences(request):
    opportunity_id = request.GET.get('opportunity_id')  
    preferences = Preference.objects.filter(Opportunity_id=opportunity_id)
    preferences_data = []

    for pref in preferences:
        preferences_data.append({
            'id': pref.id,
            'preference': pref.preference,
            'opportunity_id': pref.Opportunity.id,  
        })

    return JsonResponse({'status': 'success', 'data': preferences_data})
    
 





# from django.http import JsonResponse
# from .models import Projects

# def get_project_details(request):
   
        
#         project_id = request.GET.get('project_id')
        
#         project = Projects.objects.get(id=project_id)
        
        
        
#         project_data = {
#             'project_name': project.project_name,
           
#         }

#         return JsonResponse({'status': 'success', 'data': project_data})
    
    
from django.http import JsonResponse
from .models import Projects

def get_project_details(request):
    project_id = request.GET.get('project_id')

    try:
        project = Projects.objects.get(id=project_id)
        return JsonResponse({'status': 'success', 'project_name': project.project_name})
    except Projects.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Project not found'})

    
    
    
    
from django.http import JsonResponse
from .models import Seating

def view_seats(request):
    screen_id = request.GET.get('screen_id')
    
    

    seats = Seating.objects.filter(screen_id=screen_id)
    seat_list = [
        {"seat_number": seat.seat_number, "rate": str(seat.rate),'seat_name':seat.row_name}
        for seat in seats
    ]
    print(seat_list)
    return JsonResponse({"status": "success", "seats": seat_list})



from django.http import JsonResponse
import json
from datetime import datetime
from .models import Booking
from django.utils import timezone


def book_seat(request):
    customer_id = request.GET.get('customer_id')
    rate = request.GET.get('rate')
    screen_id = request.GET.get('screen_id')
    seat_number = request.GET.get('seat_number')
    allocate=Allocate.objects.get(screen_id=screen_id)
    lid=Customer.objects.get(login=customer_id)
    seating=Seating.objects.get(seat_number=seat_number)
    booking =Booking.objects.create(
        total=rate,
        date=timezone.now().date(),
        status="Booked",
        allocate_id=allocate.id,
        customer_id=lid.id
    )
    Bookingchild.objects.create(
        price=rate,
        booking_id=booking.id,
        seating_id=seating.id
    )

    return JsonResponse({"status": "success", "message": "Seat booked successfully"}, status=200)



from django.http import JsonResponse
import json
from datetime import datetime
from .models import Booking
from django.utils import timezone


def sendRequest(request):
    customer_id = request.GET.get('customer_id')
    oppor_id = request.GET.get('opportunity_id')
    lid=Customer.objects.get(login=customer_id)
    Request.objects.create(
        date=timezone.now().date(),
        status="Pending",
        Opportunity_id=oppor_id,
        
        customer_id=lid.id
    )

    return JsonResponse({"status": "success", "message": "Seat booked successfully"}, status=200)


from django.http import JsonResponse

from .models import Booking, Bookingchild, Allocate, Film, Theater, Customer, Seating, Screen

def view_booking(request):
    login_id = request.GET.get('login_id')

    if not login_id:
        return JsonResponse({'status': 'error', 'message': 'Login ID is required'})

    customer =Customer.objects.get(login_id=login_id) 
    print(customer)

    # Fetch all bookings made by the customer
    bookings = Booking.objects.filter(customer_id=customer)

    if not bookings.exists():
        return JsonResponse({'status': 'error', 'message': 'No bookings found.'})

    booking_data = []
    for booking in bookings:
        allocate = booking.allocate  

       
        film_name = allocate.film.film_name if allocate.film else "Unknown Film"
        screen = allocate.screen if allocate.screen else None
        screen_name = screen.screen_name if screen else "Unknown Screen"
        played_date = allocate.played_date if allocate.played_date else "Unknown Date"

        
        theater =allocate.theater.name
        # Fetch booking child details
        booking_children = Bookingchild.objects.filter(booking=booking)
        seat_details = []
        for child in booking_children:
            if child.seating:
                seat_details.append({
                    "seat_number": child.seating.seat_number,
                    "row_name": child.seating.row_name,
                    "rate": child.seating.rate
                })

        booking_data.append({
            'booking_id': booking.id,
            'theater_name': theater,
            'film_name': film_name,
            'played_date': played_date,
            'screen_name': screen_name,
            'seats': seat_details,
            'total': booking.total,
            'date': booking.date,
            'status': booking.status,
        })

    return JsonResponse({
        'method': 'Viewbooking',
        'status': 'success',
        'data': booking_data,
    })
    
    
    
from django.http import JsonResponse

import json
from .models import Payment, Booking
from decimal import Decimal

def make_payment(request):
    if request.method == "GET":  
        booking_id = request.GET.get("booking_id")
        amount = request.GET.get("amount")  

        if not booking_id or not amount:
            return JsonResponse({"status": "error", "message": "Missing booking_id or amount"})

        try:
            booking = Booking.objects.filter(id=booking_id).first()
            if not booking:
                return JsonResponse({"status": "error", "message": "Invalid booking ID"})

            amount = Decimal(amount)

           
            payment = Payment.objects.create(
                booking=booking,
                Amount=amount,
               
            )

            return JsonResponse({"status": "success", "message": "Payment successful!"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Invalid request method"})




from django.http import JsonResponse
from .models import Booking

def cancel_booking(request):
    if request.method == "GET":
        booking_id = request.GET.get("booking_id")

      
        booking = Booking.objects.filter(id=booking_id).first()
        if not booking:
            return JsonResponse({"status": "error", "message": "Booking not found or unauthorized!"})

      
        booking.delete()

        return JsonResponse({"status": "success", "message": "Booking canceled successfully!"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})


from django.http import JsonResponse
from .models import Request, Opportunities 

from django.http import JsonResponse
from .models import Request, Opportunities, Customer

def view_request(request):
    login_id = request.GET.get('login_id')

    if request.method == "GET":
        requests_data = []

        try:
            customer = Customer.objects.get(login_id=login_id)
        except Customer.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Customer not found"})

       
        requests = Request.objects.filter(customer=customer).select_related('Opportunity')

        for req in requests:
            requests_data.append({
                "id":req.id,
                "opportunity_name": req.Opportunity.title, 
                "date": req.date,
                "status": req.status,
            })

        return JsonResponse({"status": "success", "method": "ViewRequests", "data": requests_data})
    
    return JsonResponse({"status": "error", "message": "Invalid request method"})



# def add_images(request):
  
#         req_id = request.GET.get('request_id')
#         print(req_id)
#         image_data = request.FILES.get('image')
#         k=FileSystemStorage()
#         photo=k.save(image_data.name,image_data) 
#         wer=Requestimage(request_id=req_id,Image=photo,Type='pending')
#         wer.save()
        
#         return JsonResponse({"status": "success", "message": "Image uploaded successfully"})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Requestimage, Request

def add_images(request):
    if request.method == "POST":
        request_id = request.GET.get('request_id')
        image_file = request.FILES.get('image')
        k=FileSystemStorage()
        photo=k.save(image_file.name,image_file)
        request_obj = Request.objects.get(id=request_id)
        new_image = Requestimage(request=request_obj, image=photo, type="image")
        new_image.save()
        return JsonResponse({"message": "Image uploaded successfully"}, status=201)

        

    return JsonResponse({"error": "Invalid request method"}, status=405)



from django.http import JsonResponse
from .models import Request, Opportunities, Customer

from django.http import JsonResponse
from .models import Schedule, Request

def view_schedule(request):
    request_id = request.GET.get('request_id')

    if request.method == "GET":
       
            schedule = Schedule.objects.get(request__id=request_id)

            schedule_data = {
                "id": schedule.id,
                "date": schedule.date,
                "time": schedule.time,
                "venue": schedule.venue,
            }

            return JsonResponse({"status": "success", "method": "ViewSchedule", "data": schedule_data})

       

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)





from django.http import JsonResponse
from .models import Requestimage, Request

def manage_project(request):
    if request.method == "POST":
        project = request.GET.get('project_name')
        login_id = request.GET.get('login_id')
        pro_id = Production.objects.get(login=login_id)


        image_file = request.FILES.get('image')
        k=FileSystemStorage()
        photo=k.save(image_file.name,image_file)
        new_image = Projects(project_name=project,images=photo,videos='pending',production_id=pro_id.id)
        new_image.save()
        return JsonResponse({"message": "Image uploaded successfully"}, status=201)

        

    return JsonResponse({"error": "Invalid request method"}, status=405)



from django.http import JsonResponse
from .models import Production, Projects

def view_projects(request):
    login_id = request.GET.get('login_id')
    production = Production.objects.get(login=login_id)
    projects = Projects.objects.filter(production_id=production)
    
    project_list = []
    for project in projects:
        project_list.append({
            "id": project.id,
            "name": project.project_name,
            "image": project.images.url if project.images else None  # Convert FieldFile to URL
        })
    
    return JsonResponse({
        "status": "success",
        "method": "view_projects",  # Added method
        "projects": project_list
    })  
    
    
    
from django.http import JsonResponse
from .models import Projects

def delete_project(request):
    if request.method == "GET":
        project_id = request.GET.get("project_id")

        if not project_id:
            return JsonResponse({"status": "error", "message": "Project ID is required", "method": "delete_project"})

        try:
            project = Projects.objects.get(id=project_id)
            project.delete()
            return JsonResponse({"status": "success", "message": "Project deleted successfully", "method": "delete_project"})
        except Projects.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Project not found", "method": "delete_project"})

    return JsonResponse({"status": "error", "message": "Invalid request method", "method": "delete_project"})



def add_oppor(request):
    if request.method == 'GET': 
        pro_id = request.GET.get('project_id')
        oppor = request.GET.get('name')
        
        detail = request.GET.get('detail')
        

        
           

            

          
        opportunity = Opportunities.objects.create(
                title=oppor,
                details=detail,
                project_id=pro_id,
               
               
            )

           

           
        

    return JsonResponse({'status': 'success', 'message': 'Invalid request method.'})


from django.http import JsonResponse
from .models import Opportunities

@csrf_exempt
def view_oppor(request):
    if request.method == 'GET':
        project_id = request.GET.get('project_id')

        if not project_id:
            return JsonResponse({'status': 'error', 'message': 'Missing project_id'})

        opportunities = Opportunities.objects.filter(project_id=project_id)
        data = [{'id': opp.id, 'name': opp.title, 'detail': opp.details} for opp in opportunities]

        return JsonResponse({'status': 'success', 'method': 'view_opportunities', 'opportunities': data})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def add_pref(request):
    if request.method == 'GET': 
        opp_id = request.GET.get('opportunity_id')
        pref = request.GET.get('preference')
        
        

        
           

            

          
        prefe = Preference.objects.create(
                preference=pref,
                Opportunity_id=opp_id,
               
               
            )

           

           
        

    return JsonResponse({'status': 'success', 'message': 'Invalid request method.'})



from django.http import JsonResponse
from .models import Request

def view_requests(request):
    try:
        requests = Request.objects.select_related('customer', 'Opportunity').all()
        request_list = []

        for req in requests:
            request_list.append({
                "request_id":req.id,
                "fname": req.customer.fname,  
                "title": req.Opportunity.title,  
                "date": req.date , 
                "status":req.status
            })

        return JsonResponse({"status": "success", "data": request_list}, safe=False)
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
    
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Schedule, Request 

@csrf_exempt  
def add_meeting(request):
    if request.method == 'GET': 
        req_id = request.GET.get('request_id')
        date = request.GET.get('date')
        time = request.GET.get('time')
        venue = request.GET.get('venue')

        if not all([req_id, date, time, venue]):
            return JsonResponse({'status': 'error', 'message': 'Missing required parameters'})

        try:
            meeting = Schedule.objects.create(
                date=date,
                time=time,
                venue=venue,
                request_id=req_id
            )

            Request.objects.filter(id=req_id).update(status="Scheduled Meeting")

            return JsonResponse({'status': 'success', 'message': 'Meeting added successfully'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

    # if request.method == 'GET': 
    #     req_id = request.GET.get('request_id')
    #     date = request.GET.get('date')
    #     time = request.GET.get('time')
    #     venue = request.GET.get('venue')

        
        
    #     meeting = Schedule.objects.create(
    #             date=date,
    #             time=time,
    #             venue=venue,
    #             request_id=req_id,


               
               
    #         )
        

    # return JsonResponse({'status': 'success', 'message': 'Invalid request method.'})



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from film_app.models import Community  

def add_community(request):
    if request.method == 'GET':
        community = request.GET.get('community_name')
        login = request.GET.get('login_id')

        try:
            customer = Customer.objects.get(login_id=login)  
            Community.objects.create(
                name=community,
                customer_id=customer.id  
            )
            return JsonResponse({'status': 'success', 'message': 'Community added successfully'})

        except Customer.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Customer not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def view_communities(request):
    try:
        communities = Community.objects.all()
        data = []
        for community in communities:
            data.append({
                "community_id": community.id,
                "name": community.name
            })

        return JsonResponse({"status": "success", "method": "ViewCommunities", "data": data})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
    




from django.http import JsonResponse
from film_app.models import Customer, Community, join_community

from django.http import JsonResponse

from .models import Customer, Community, join_community  # Ensure proper model names


def joincommunity(request):
    try:
        login_id = request.GET.get('login_id')
        com_id = request.GET.get('community_id')

        if not login_id or not com_id:
            return JsonResponse({"status": "error", "message": "Missing login_id or community_id"}, status=400)

        # Check if Customer exists
        try:
            cus = Customer.objects.get(login_id=login_id)
        except Customer.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Customer not found"}, status=404)

        # Check if Community exists
        try:
            community = Community.objects.get(id=com_id)
        except Community.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Community not found"}, status=404)

        # Prevent duplicate join
        if join_community.objects.filter(Community=community, customer=cus).exists():
            return JsonResponse({"status": "error", "message": "Already a member"}, status=400)

        # Add to JoinCommunity table
        join_community.objects.create(Community=community, customer=cus)

        return JsonResponse({"status": "success", "message": "Joined community successfully"}, status=200)

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


def joined_comm(request):
   
        login_id = request.GET.get('login_id')
        cus = Customer.objects.get(login_id=login_id)

        joined_communities = join_community.objects.filter(customer=cus)

        data = []
        for join_entry in joined_communities:
            community = join_entry.Community  
            data.append({
                "name": community.name,
                "community_id": community.id  
            })

        return JsonResponse({"status": "success", "method": "ViewCommunities", "data": data})
# from .models import ChatMessage
# def chatdetail(request):
#     # Ensure sender_id and receiver_id are properly retrieved
#     community = request.GET.get('community_id')  # receiver (counselor)
#     user_id = request.GET.get('sender_id')  # sender (user)

    
   

   
#     try:
#         counselor_login_id = int(counselor_login_id)
#         user_id = int(user_id)
#     except ValueError:
#         return JsonResponse({"status": "error", "message": "Invalid ID format."})

#     # Fetch chat messages between counselor and user
#     chat_messages = ChatMessage.objects.filter(
#         Q(sender_id=counselor_login_id, receiver_id=user_id) | 
#         Q(sender_id=user_id, receiver_id=counselor_login_id)
#     ).order_by('chat_id')  # Ensure 'id' exists in Chat model

#     # Get user details
#     user = get_object_or_404(Customer, login_id=user_id)  # Use 'id' instead of 'login_id' if applicable

#     # Convert chat messages to JSON-friendly format
#     chat_data = [
#         {
#             "id": msg.chat_id,
#             "sender_id": msg.sender_id,
#             "receiver_id": msg.receiver_id,
#             "message": msg.message,
#             "date": msg.date
#         }
#         for msg in chat_messages
#     ]

#     # Return response as JSON
#     return JsonResponse({
#         "status": "success",
#         "chat_messages": chat_data,
#         "user": {
#             "id": user.login_id,
#             "name": user.fname  # Adjust based on actual User model fields
#         },
#         "sender_id": counselor_login_id
#     })   




## views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from film_app.models import ChatMessage
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def chat_user(request):
    """Handle sending a new chat message"""
    logger.info(f"chat_user called with method: {request.method}")

    if request.method in ['POST', 'GET']:  # Allow both GET and POST
        try:
            sender_id = request.GET.get('sender_id')
            community_id = request.GET.get('community_id')
            message_details = request.GET.get('details')

            if not sender_id or not community_id or not message_details:
                return JsonResponse({'status': 'error', 'message': 'Missing required fields'}, status=400)

            # Save message
            chat_message = ChatMessage.objects.create(
                message=message_details,
                sender_id=sender_id,
                community_id=community_id,
                timestamp=datetime.now()  # Use DateTimeField in models
            )
            chat_message.save()
            logger.info(f"Message saved with ID: {chat_message.id}")

            return JsonResponse({'status': 'success', 'message': 'Message sent successfully'})
        except Exception as e:
            logger.error(f"Error in chat_user: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@csrf_exempt
def chatdetail(request):
    """Get chat messages for a community (group chat)"""
    logger.info(f"chatdetail called with method: {request.method}")

    if request.method == 'GET':
        try:
            community_id = request.GET.get('community_id')
            if not community_id:
                return JsonResponse({'status': 'error', 'message': 'Missing community_id'}, status=400)

            # Fetch all chat messages for this community
            chat_messages = ChatMessage.objects.filter(community_id=community_id).order_by('timestamp')

            messages = [{
                'message': chat.message,
                'sender_id': str(chat.sender_id),
                'community_id': str(chat.community_id),
                'time': chat.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp properly
            } for chat in chat_messages]

            return JsonResponse({'status': 'success', 'chat_messages': messages})

        except Exception as e:
            logger.error(f"Error in chatdetail: {str(e)}", exc_info=True)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking, Payment, Allocate

@csrf_exempt
def get_paid_movies(request):
    log_id = request.GET.get("login_id")

    cus=Customer.objects.get(login_id=log_id)
    bookings = Booking.objects.filter(customer=cus)

   
    
    paid_movies = []
    
    for booking in bookings:
        try:
            # Find related payment
            payment = Payment.objects.get(booking_id=booking.id)
            allocate = Allocate.objects.get(id=booking.allocate_id)

            paid_movies.append({
                "film_name": allocate.film.film_name,  # Assuming Allocate links to Film model
                "amount": payment.Amount,
                "date": booking.date,
                "status": booking.status,
                "screen": allocate.screen.screen_name,
                "played_date": allocate.played_date,
                "time": allocate.timing.time,
                "theater": allocate.theater.name,
            })
        except Payment.DoesNotExist:
            continue  # Skip unpaid bookings

    return JsonResponse({"status": "success", "data": paid_movies})

