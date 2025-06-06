from django.db import models


class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=60)
    usertype=models.CharField(max_length=70)
    
class Theater(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    city=models.CharField(max_length=70)
    pin=models.CharField(max_length=60)
    phone=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    
class Customer(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=60)
    lname=models.CharField(max_length=70)
    city=models.CharField(max_length=60)
    dist=models.CharField(max_length=70)
    pin=models.CharField(max_length=70)
    phone=models.CharField(max_length=70)
    gender=models.CharField(max_length=70)
    dob=models.CharField(max_length=70)
    resume=models.FileField()

class Type(models.Model):
    type_name=models.CharField(max_length=60)
class Film(models.Model):
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    film_name=models.CharField(max_length=60)
    film_release=models.CharField(max_length=70)
    film_desc=models.CharField(max_length=70)
    duration=models.CharField(max_length=70)
    image=models.FileField()

class Timing(models.Model):
    timing_name=models.CharField(max_length=60)
    time=models.CharField(max_length=70)
class Screen(models.Model):
    screen_name=models.CharField(max_length=60)
    no_seats=models.CharField(max_length=70)
class Seattype(models.Model):
    seat_type=models.CharField(max_length=60)
    desc=models.CharField(max_length=70)
class Seating(models.Model):
    screen=models.ForeignKey(Screen,on_delete=models.CASCADE)
    seat_type=models.ForeignKey(Seattype,on_delete=models.CASCADE)
    row_name=models.CharField(max_length=70)
    seat_number=models.CharField(max_length=70)
    rate=models.CharField(max_length=70)
    
class Allocate(models.Model):
    screen=models.ForeignKey(Screen,on_delete=models.CASCADE)
    film=models.ForeignKey(Film,on_delete=models.CASCADE)
    timing=models.ForeignKey(Timing,on_delete=models.CASCADE)
    theater=models.ForeignKey(Theater,on_delete=models.CASCADE)
    played_date=models.CharField(max_length=70)
    status=models.CharField(max_length=70)
    
class Booking(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    allocate=models.ForeignKey(Allocate,on_delete=models.CASCADE)
    total=models.CharField(max_length=70)
    date=models.CharField(max_length=70)
    status=models.CharField(max_length=70)
class Bookingchild(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    seating=models.ForeignKey(Seating,on_delete=models.CASCADE)
    price=models.CharField(max_length=70)
class Payment(models.Model):
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    Amount=models.CharField(max_length=70)
class Production(models.Model):
    login=models.ForeignKey(Login,on_delete=models.CASCADE)
    team_name=models.CharField(max_length=60)
    place=models.CharField(max_length=70)
    phone=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
class Projects(models.Model):
    project_name=models.CharField(max_length=60)
    production=models.ForeignKey(Production,on_delete=models.CASCADE)
    videos=models.FileField()
    images=models.FileField()
class Opportunities(models.Model):
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    details=models.CharField(max_length=60)
class Preference(models.Model):
    Opportunity=models.ForeignKey(Opportunities,on_delete=models.CASCADE)
    preference=models.CharField(max_length=60)
class Request(models.Model):
    Opportunity=models.ForeignKey(Opportunities,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.CharField(max_length=60)
    status=models.CharField(max_length=60)
class Requestimage(models.Model):
    request=models.ForeignKey(Request,on_delete=models.CASCADE)
    image=models.FileField()
    type=models.CharField(max_length=60)
class Schedule(models.Model):
    request=models.ForeignKey(Request,on_delete=models.CASCADE)
   
    date=models.CharField(max_length=60)
    time=models.CharField(max_length=60)
    venue=models.CharField(max_length=60)
    
    
class Community(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
   
    name=models.CharField(max_length=60)
    
class join_community(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    Community=models.ForeignKey(Community,on_delete=models.CASCADE)
    
class ChatMessage(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Reference to user
    message = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True) 
    community = models.ForeignKey(Community, on_delete=models.CASCADE)  # Reference to user









  
   
    

  


   


    
    