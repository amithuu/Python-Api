what is Django:
CGI: common gate way intefrace..

[pip install django]

    this is an open source web development framework,,hwich is mainy used to web-framework..

# some of the admin classes/function  of django:django-admin
t
check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver


# to start the project we use
<!-- django-admin startproject django_project -->

# to change the directory we use:
<!-- cd filename -->

# change directory to project/filename:
<!-- cd django_project/ -->

# after this got the file and view there will be a project present in file..

<!-- add that entire file to code editor.. -->
<!-- and in that we have settings/init/url/wsgi/manage files.. -->

# Some of the files we find once the directory is found.

<!-- init: this is the file where it shows it is pyhton file project..

settings : this is the file that where our security and some predefined application given by django is stored..

url: this is the section where our all page urs will be stored..[admin/], where we can use the admin section using "www.our.application.admin/"

wsgi: this is the file which is used to connect the python and the web appilication.. -->


# once after this we need to run:

<!-- python manage.py runserver -->
# which gives us the localhost server 127:0:0:1:8000 port

where we can acces this link and check..
we can change the link to

<!-- 127:0:0:1:8000 -->

we can check for admin block as we have in url-file,

<!-- localhost:8000/admin -->

# to set any new url of the page we can use url_py;

eg:

<!-- urlpatterns=[
    path('dashboard/', dashboard.site.urls),
] -->


after the use we can close our local host we can use:

<!-- CTRL C: to stop the server. -->

# to start the  django app we use command:

 <!-- python manage.py startapp blog -->  [we can check these command are available in help command]
        [BLOG is the file name u want to create..]

# once the file blog is created now we start building our application home page function
[ i am writing function to handle the traffic of the home page when user logins.. ]

for that we need to take responces from user, so we need to request for the user.

we need to import:
<!-- from django.http import HttpResponce --> this import will collect the respoce from the users..

# Creating the function home(request) which is used sen dthe request and collect the responce..

<!-- def home(request):
        return HttpResponse("<h1> hi this is home page </h1>") -->

Here we are handling the user when he comes to home page.

To redirect user we are creating a "urls.py" file, where we  map the function for each view/page user view.

# This "blog/urls.py" file will be same as "urls.py" in django_project.

# Create a file called "urls.py" under blog and add the path to Home page.

# to add the path we need to import files from "views.py" and "path" as well
<!-- from . import views
from django.urls import path -->

# we create a constructer as same as in "urls.py" in django_project.
<!-- 
urlpatterns = [
    path('',views.home, name='blog-home')
] --> 
# here '' is the extension path for the home page. and we are calling the home function from here.

# Then we need to connect "blog/urls.py" file into  "urls.py" in django_project.
<!-- we need to include import it comes with path as well.
    in urlpatterns constructer we can add another path. -->

<!--path('blog/', include('blog/urls)), -->

# once after this run the server and check.

# further if we need to add  more function's ex: about, we can just keep on adding in "blog/urls.py" and in the functions in "views.py" file.

in views:
<!-- def about(request):
        return HttpResponse("<h1> hi this is about page </h1>") -->

in urls.py:
    path('about/', views.py,name='about-page'),

# if we run trhe server we get both the page.[localhost:8000/blog/about] //for about page and [localhost:8000/blog/] //for home page.


<!-- ################################################################################ -->
# end of basics:
from line 200 advance:



















































# we cant keep creating functions for all so we are adding a single page to every single templates and the using the templates we are accesing each and every file.

# Create a folder under blog names "templates" and under templates create another folder "blog"
blog -> temaplates -> blog 

# create a file for each of the functions under blog folder.
blog -> temaplates -> blog ---// home.html


# once this is created go to "views.py" file 
# previosly we used to use HttpResponce for the accessing of the file, we can sue another function as we are rendering the file from another folder.. we use 
<!-- from django.shortcuts import render -->

# In ther created function home, change the return statement as 

<!-- return render(request,'blog/home.html') -->
        <!-- return HttpResponse("<h1> hi this is home page </h1>") -->
        <!-- return render(request, 'path of the file located')-->


# Lets try to access some dummy created by cerating a dummy data form the dictonary//
# we are passing the dummy data inside the list/dictornary so that using key:value we can access the data easily..

    ex: posts=[
       {
        'author': 'amith',
        'title': 'blog1',
        'dateposted': 'january'
    },
    {
        'hi':'hello',
        'wfh':'yes'
    }
    ]

# to access this data we need to create a list and an obj which is easier to access the above dummy data.

inside the function
ex: def home(request):
        context={
           #obj 'storealldata'=posts # dummy data list name.[all the data will be stored in the object]
        }
        return render(request, 'file path name', context)[render function accepts only 3 parameters so we are passing the context through ehich we can access the data.]

# the another thing in here we need to access the data in html file.// for that we use 
<!-- <body>
            {% for post in storealldata %}   # storealldata is the variable dictonary where we have stored our data
                <h1> {{post.author}}</h1>
                <p> {{post.title}}</p>
                <p>on {{post.dateposted}}</p>
            {% endfor %}  # ending of this very important
        </body> -->

# This is the another method, as we are writing the same lines of code several times we can make a static file where we can store a similary code and change once for all, when we needed.
# that is done by cerating an another file called "base.html" under "blog" 
        <!-- "templates->blog->base.html" -->

# once the file is created we add the repeated code to that file, and logic og each page in a "{block}"
for ex:
<!-- <!DOCTYPE html>
<html>
    <head>

        {% if title %}
            <title> learning {{title}}</title>
        {% else %}
            <title> started learning</title>
        {% endif %}

        <body>
            {% block content%} {% endblock content%}
        </body>

    </head>
</html> -->

# As in the home.html and the about.html there is an logic difference between the body so we are making it as block and all the other things as static.

# now in home page
# * first we need to extend the base.html file to home.html, so for that we use 
<!-- {% extends 'blog/base.html'%} -->
# * and next create a block where the logic has to be. {block}

for home page
<!-- {% extends 'blog/base.html'%} -->
<!-- {% block content%}
        {% for post in store %}
            <h1> {{post.author}}</h1>
            <p> {{post.title}}</p>
            <p>on {{post.dateposted}}</p>
        {% endfor %} 
      {% enbdblock content %}  -->

for about page
<!-- {% extends 'blog/base.html'%}
{% block content %} 
    <h1> this is about page </h1>
{% endblock content %} -->

# THE BIG USE OF THIS IS, WE NO NEED TO WRITE ALL THE THINGS JUST WE NEED TO MAKE CHNAGES IN BLOG WHERE IT WILL CHANGE IN ALL THE PAGES.

# To make our project little intresting  added some "html nav bar code" inside body and "main html" as well,  and  AS WE NEED CSS WHICH IS STATIC SO  CREATE A FOLDER CALLED :STATIC: INSIDE STATIC CREATE ANOTHER FOLDER CALLED :BLOG: AS IT IS OUR APP NAME, INSIDE THAT CREATE A MAIN.CSS FILE 

"BLOG -> STATIC -> BLOG -> .CSS FILE"

# after that run the server again so that css gets load..

# In main file that is "basic.html" we have given .about, /blog[which is not correct if anything chnages we need to chnage in all place]  so change the path to [url 'name of the file given in "views.html"] 
ex:

<!--   <a class = "navbar-item nav-link" href="{% url 'blog-home'%}">Home</a>
        <a class = "navbar-item nav-link" href="{% url 'blog-about' %}">About</a> 
-->

# [##################################################################################]
# continue from line 330
# creating a :admin-user: "Super User"













# We are creating the admin user for the admin acces which is Super User
<!-- To Create Super User we have a command "createsuperuser" -->
<!-- python manage.py createsuperuser -->
# Run the command by stopping the server

* Error[ an error will be generated beacuse of teh below reason.] 

    <!-- django.db.utils.OperationalError: no such table: auth_user -->

    # why error??
    # Since we havn't created a database that we user for this project!!

# creating a database is simple here, just we need to run few "Migration" command.

# ":migration": is basicly used to apply the changes to database.

Once we use migration as we haven't created databsed it adds some tables to the database , and then it allows "createsuperuser"

<!-- python manage.py makemigrations -->

# after running the command o/p will be "No Changed Detected" [as the migration is  creating database] !!! [if user have created database user will get changed displayed.!! ]


# To apply the changes in migrations need to run this command:
 <!--python manage.py migrate  -->
# [which helps the migrations to update]

# once after running above command now you can create your super-user:

<!-- python manage.py createsuperuser
Username (leave blank to use 'chiku'): amith
Email address: amithtalentplace@gmail.com
Password: New@1234
Password (again): New@1234
Superuser created successfully. -->


# After this run the server again

# [ U will be able to watch the admin blof try login , once you enter click on users and username which u created!!]

U will get to see the Password: with some [#labels] which is the added more security in Django.

<!-- ex:
password: algorithm: pbkdf2_sha256 iterations: 600000 salt: MSw5ES**************** hash: Sp5B1i************************************** -->

[we can add users there /delete users / can provide the permission there itself.]



# Creting own Database:
 # [To work with the data base, jango has the excellent advantage which is "ORM" in it..]

 ORM: "OBJECT RELATIONAL MAPPER": 
# We can access database easily using the objects, and we can access other database as well without changing the code.

# Using SQLlite for the devlopment and Postgres database for the production..

# any changed in the database or updation , will be done in "blog/model.py" file..


# In "models.py" where we wanna think what need to store in our database.[ can  create a user from here as well and add some more fields than in amdin page for the users]
# [to do all these we need a databse model, which is already created by the Django, can     inherit the models class.]
# [Can create our owm model as well.]]


# now we are creating a class/ which is Table called :Post: in which we are giving the column names we need.

class Post(models.Model):                     <!--[models.Model]-> using this we create a table in the database [for models we need to "import from django.db import models"] -->
    title=models.Charfeild(max_length=100)                   -> <!-- there are the attributes that we are adding to the table Post..-->
     author=models.TextFeild()                                -> <!--Charfeild and TextFeild are same but text feild doesnt has any limit.. -->
    date_posted = models.DateTimeField(default=timezone.now) -> <!-- For the date attribute provide date format, for "default" we need to "import timezone from django.utils" -->
    author = models.Foreignkey(User, on_delete=models.CASCADE) -> <!-- author name we are taking form the "User" database table, so making it as ForignKey, and on_delete, means if the author gets delete in "User" table then just delete the name of the author from the Post table , dont delete the data form database. -->

ex:
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# after creating the file adding/creating the above database table

# We need to add it to the database , so for that we need to run the migrations

<!-- python manage.py makemigrations --> [which means make the changes in database.]

# after running this the Django, creates it folder as "migrations" under blog.
<!-- Migrations for 'blog':
  blog/migrations/0001_initial.py  
    - Create model Post -->
    blog -> migrations -> 00001_initial.py

# to get the sql query for t5he above table need ti run the command.

<!-- python manage.py sqlmigrate blog 0001 -->[blog 0001]-> is the app name and file name

BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;

<!--  Then save it to database using python manage.py migrate -->

# To access the data we need to run in "python shell"
so, 
<!-- python manage,py shell -->

# now we need to import the files to shell soo,

<!-- from blog.models import Post 
     from django.contrib.auth.models import User -->

<!-- To print the data from User or Post we use, "Tablename.objects.all()"-->
ex:
<!-- User.objects.all()
    Post.objects.all() -->

# We can use the filter as well to get the data

ex:
<!-- User.objects.all()  -> which return all the record -->
<QuerySet [<User: amith>, <User: Sudeshdas>]>
<!-- User.objects.first() -> which gives the first record -->
<User: amith>
<!-- User.objects.last()  -> which gives the last user from the table. -->
<User: Sudeshdas>

<!-- User.objects.filter(username='amith') -> Gets the name with amith from the db  -->
<User: amith>
<!-- User.objects.filter(username = 'amith').first()  gets the name with amith with the first matching record from the db..-->
<User: amith>

# by using variable as well we can store and gets the data:
<!-- user = User.objects.filter(username = 'amith').first() -->
<!-- user -->

# As the migration file we saw, the id has been created for every user incrementally, we can access the user using ID as well.

<!-- user.id --> [as in user amith is stired where his id :1]
1

<!-- user.pk --> [we can get the id using primary key as well]
1

<!-- user = User.objects.get(id=1)  -> using this filter as well can fetch the data. -->
<!-- user -->
<User: amith>

# Without adding any data when we try to access we get like
<!-- Post.objects.all() -->
<QuerySet []>

 # To add the data
<!-- post_1 = Post(title='django',author= user,content='learning django it is awesome') 
        -> as already in user variable we have the 'amith' so in field of author we used "user", and as default function gives the date base don current date, so no nned to add that attribute..-->

# save the data
<!-- post_1.save() -->

# when we try to view the data 
<!-- Post.objects.all() -->
<QuerySet [<Post: Post object (1)>]>


# As we have only addedd attributes in "Post" function there is no return statement so we get like the above thing..

# exit from the shell 
<!-- exit() -->

# Need to create a dunder STR method in "models.py file" [any data we need to print on shell]

<!-- def __str__(self):
        return self.title -->


#  to get the updated files, re-open all the "import files" then access.

<!-- pyhton manage.py shell -->

 <!--  from blogs.models import Post 
       from django.contib.auth.models import User-->

<!-- Post.objects.all() -->
<QuerySet [<Post: Django>]>

<!-- user1 = User.objects.filter(username='sudeshdas').firstname()
user1 -->
<User: Sudeshdas>

<!-- post_2 = Post(title='ReactJs', author='user1',content='good in react') -->
<!-- post_2.save() -->
# we can sue user1.id as well for author name!
<!-- post_2 = Post(title='ReactJs', author='user1.id',content='good in react') -->
<!-- post_2.save() -->

<!-- Post.objects.all() -->
<QuerySet [<Post: Django>, <Post: ReactJs>]>

<!-- post = Post.objects.first() -> stroing all the details of the first user in post variable, so that we can accces all theb data using the variable itself.  -->

<!-- post.content -->
'learning django it is awesome'

<!-- post.id -->
1

<!-- post.author -->
<User: amith>

<!-- post.email  -> here as we are not storing the email in "Post" class but still we are able to get the all data of teh user[because of the foreign key.] -->
'amithtalentplace@gmail.com'

<!-- post.date_posted  -->
datetime.datetime(2023, 8, 8, 8, 41, 18, 611145, tzinfo=datetime.timezone.utc)


# to get all the posts posted by the user we can view like.
[Syntax: modelname/variablename.post_set.all()]

<!-- user.post_set.all() -> to get all the posts for the user-->
<QuerySet [<Post: Django>]>

<!-- user1.post_set.all() -> to get all the posts for the user1-->
<QuerySet [<Post: ReactJs>]>

# Can create a post using the post_set() function as well!!
ex:
# We have a user which has one post[whose author is amith]

<!-- user.post_set.create(title='Python', content='this is post created using post_set fucntion') -> we are not adding the author here bcz, we have a default authir how is user.-->
<Post: Python>
<!-- user.post_set.all() -->
<QuerySet [<Post: Django>, <Post: Python>]>

# Prevously we used to get the posts from the dummy data that was created in "views.py", but now can access through database, for that,

<!-- in views.py impot the models and Post
from .models import Post
def home(request):
    context = {
            'posts': Post.objects.all()  -> this is fecth all the Posts from the Post class..![which we stored in db.] 
    }
    return render(request, 'blog/home.html', context) -->

    posts = [
    {
        'author': 'Amith',
        'title': 'Learning Django',
        'date_posted': 'Today',
        'content': 'this is Django learning time!!!'
    },
    {
        'author': 'Sudesh',
        'title': 'Learning Django',
        'date_posted': 'Dont Know',
        'content': 'this is Django learning time!!!'
    }
][the dummy data whoch we have provided the attributes name should be same in db as well, beacuse we have used these database names to fetch the data in home/about .html file soo.]

# Aswe are getting the date in [ Aug. 8, 2023, 8:41 a.m.] in posts we can filter using the [|date: "format"]
ex: we are using date in home page, so lets change it there,
<small class ="text-muted">{{post.date_posted}}</small>
Aug. 8, 2023, 8:41 a.m.
<small class ="text-muted">{{post.date_posted|date:"F d, Y"}}</small>
 August 08, 2023

 # we dont need the dummy data now as we have the database.

# ADDING THE POST DATA TO ADMIN PANEL AS WELL..

# Need to do it in "admin.py" under "blogs" 
<!-- from .models import Post 
      admin.site.register(Post) -> we are regitering the Post class to admin page!!!
      -->


# [#######################################################################]
# Now adding the users an trying to get there data as well..

# Not to merge the superuser data and real users data , create a neww "app" under the project, so that finding will be easy..

# Create an new app for the usres
<!-- python manage.py startapp users -->
 # A new folder will be created.!

# Once the app is created go to settings of main app, and add the app in "INSTALLED APPS"['users.apps.UsersConfig',] 
<!-- 'users.apps.UsersCOnfig', -->

 # Inside the folder in "views.py" crete a form..
 [To create a form in Django we can create it easily by impoting the UserCreationForm]

 <!-- from django.contrib.auth.froms import UserCreationForm -->

 # create a function which renders the "page".

 <!-- def register(request):
        form = UserCreationForm() --> 
         [this will create an instance for the inbuild-form in django]
<!--    return render(request, 'users/register.html', {'form':form}) --> 
# still we have not created the "users/register.html" file its the next step.
        [as in the blog  created the context and added the context in parameter, so here now creating the "form" and rendering through its :instance:form  ]
    
<!-- def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form}) -->

# Create a file under "users" as folder "templates" in it folder "users" in it "register.html"
users-> templates -> users -> register.html

# In this .html file {% add the block and content needed. to be dislayed on the screen%}

# To get the {% block fiest we need the "basic.html" page that we have not creted yet, so we are importing from "blog"%} 
<!-- {% extends 'blog/base.html' %} -->
{% block content%}
    <div class = content-section>
        <form method='POST'>
            {% csrf_token %} -> this the security path for the forms from peach attacks
            <fieldset class = 'form-group'>
                <legend class = 'border-botton mb-4'>Join today </legend>
                {{form.as_p}} -> to get the form in para format we use this.
                {{form}} -> if we take only form we might not get the items in the proper spacing
            </fieldset>

            <div class = 'form-group'>
                <button class = 'btn btn-putline-info' type='submit'> Sign Up</button>
            </div>
        </form>

        <div class = border-top pt-3>
            <small class = 'text-muted'> Already have an account? 
                <a class = ml-2 href="#>Sign In</a>
            </small>
        </div>
    </div>
{% endblock content%}


# Which gives us the form on the "register", when we run the server

<!-- localhost:8000/register -->
    
# [Now after taking the input and click on sign-up there is save of responce in amin panel]

<!-- def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form}) -->

 <!-- def register(request): -->
  <!-- if request.method == 'POST': -->
    we are checking if user is poting the data or not.

  <!-- form = UserCreationForm(request.POST) --> 
        if user is posting the data then we are creating a new form here.

  <!-- if form.valid(): -->
        checking whether the form is valid or not, 
   <!-- form.save() -->
        if from is valid then save it.

# we are taking username form the feild to print the success message here.
   <!-- username = form.cleaned_data.get('username')
        messages.successs(request, f'account created for {username}!') -->
            taking username and priting the message with name of the user
            [cleaned_data-- is a dictonery where it store the value of the data.]
   <!-- return redirect('blog-home') -->
            Once after saving the form we are redirecting to home page
            [to get into home page we are using "name of the home page"]

   <!-- else: -->
   <!-- form = UserCreationForm() -->
        if it is not post method then blank all the feilds.
   <!-- return render (request, 'users/register.html', {'form':form}) -->
            
# To validate the form and save the details and redirecting to home page, if not validated   resetting to blank page.

ex:
<!-- def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # -> it will create a new form with the data in it.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for the {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()  #-> if it is not post we create a blank form
    return render(request, 'users/register.html', {'form':form}) -->
 
# after creation of "view.py" page, we need to add to the "urls." ['previoulsy.we.used.to.add.it.into.the.new."urls.py".page.but.can.add.it.directly.into.the."django"."urls.py".file']

# for that we need to import "views.py" from users 
<!-- from users import views as user_views -->

<!-- path('register/', users_views.register, name='register'),-->

# In the form there is no email id , try adding it.

# So to add that we need to create a new class/form from where we can add the features into the existing from["UserCreationForm"].

For that we need to import the form from the django.
# from django import forms
We need the user model as well
# from django.contrib.auth.models import User
we need to import UserCreationForm as creatinga  new from.
# from django.contrib.auth.forms import UserCreationForm

Create a class to add the new fields, which inherits the UserCreationForm
<!-- class UserRegisterForm(UserCreationForm):
        [now inside the class we can add all the fields needed. ]
    email = forms.EmailFeild() --> 
            email = forms.EmailField(request=true)
    [by default request=true, means mandatory,if request=false, the it is not mandatory]

# for the same class additing an another class called ["Meta"]:

<!-- class UserRegisterForm():
    field-name: forms.datatypes()

    class Meta:
        model = User -> for which model/db ur adding this details.
        fields = ['we need to add the attributes that need to show in the form-fields'] -->


# This Meta class combines our class with the forms.

# Once the adding of  "UserRegisterForm():" class, Go back to "views.py" and change the form to "UserRegisterForm():" rather than "UserCreationForm()" in POST all changes.

# after this run the server again
<!-- python manage.py runserver -->

# as the application is not much designed, for that django has his in inbuilt auto "css" designing.

# Need to add "crispy-forms" in the app ij settings.
<!-- 'crispy_forms', -->
<!-- 'crispy_bootstrap4' -->

# At the end of the "settings.py" file in "main-project"
<!-- CRISPY_TEMPLATES_FORM = 'bootstrap4' -->

# once the above setting is done, back to "register.py" 
<!-- {% load crispy_form_tags %} -->

in the form we have used {{forms.as_p}} instead if this use 
<!-- {{ forms|crispy }} -->

# NOW WE CAN SEE THE CHANGES IN THE CSS STYLING OF THE REGISTER PAGE..

# go to "basic.html" in body where <a> with register link, change the href->{% url register%}  [as we have given the name of url as register while linking.]

# [#########################################################################]#
 
 # AS register page is done, now create a login page so that users an get into home page/
Continue from line 790



# [Login_page_for_User]

# As the Django has own login and logout forms as well, Just need to import from the "auth"."views".. 

<!--'from django.contrib.auth import views as auth_views' -->
# as django has inbuild "views.py" for logina and logout page.

# In the main project "urls.py" import it and add the path as well.

<!-- from django.auth import views as auth_views -->

# Adding the path as we have the "views.py" by default.

<!-- path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login') -->
<!-- path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', name='logout')) -->

# create a login.html and logout.html in "users"

# [Create a file "login.html"]

copy paste the same code from "register.html" and make some changes..

 <!-- <button class="btn btn-outline-info" type="submit">Login</button> -->

 <!-- Do You Want To Create An Account? <a class="ml-2" href="{% url 'register'%}">Sign Up Now</a> -->


# after this when we enter the login by entering correct details, we get the ['404error/http://127.0.0.1:8000/accounts/profile/'] 

To Avoid this Issue, we can redirect the page to blog-home page,
To do this need to change the seeting of the [login_redirect_url] 

# [settings.py->lastline->LOGIN_REDIRECT_URL='blog-home']
# Here redirecting after the user clicks on login to home page.

# Once the user gets Login , he watches the Home which page which is "base.html"[we have a login link in that page], [even after the user has logged in it is showing login link], [so need to chnnge that, if user is logged in it has to show "logout" else "login"]

# How to check whether the user is logged in or not!!

# For that as well Django has this own functionality [user.is_authenticated]

<!-- {% if user.is_authenticated %} 
            then show Logout.
    else:
            then show login/register
    {% endif %} -->

 # [Need to make the changes in "base.html" file]
 <div class =nav_bar>
    {% if user.is_authenticated %}
        <a href="{% url 'logout'%}">Logout</a>

 </div>
 else:
 Home page with Login/register..




# [######################################################################]
 now on creating a user profile page.

 once the user login's he will be redirected to users profile, instead og home page.
# Create a file called "profile.html" under "users"[add some content to show into it.]

# [profile.html]

<!-- {% extends 'blogs/base.html'%}
{% load_crispy_tags %}
{% block content%}
    <h1> {{user.username}}</h1>  -> if the user is logged in it will display the username..
{% endblock content%} -->


# In "views.html" create a function to access the "profile.html" page.
<!-- def profile(request):
        return render(request, 'users/profile.html') -->
    [ here we are rendering the file from users.]

# Add the link/path to "profile.html" page in settings.
path=['profile/', users_views.profile, name='profile']

# add the link to base.html to display the link when the user is logged-in
[ in navigation bar]

<!-- <a class = 'nav-item nav-link', href = "{% url 'profile'%}" >Profile</a> -->

# After logged in User will get to see the 2 links profile and logout, if user has logged out and if user redirects to profile page using tab menu "localhost/profile/", then [usre willnot get his username displayed, as he has logged out, there is no user in the username db as of now.]

# TO SOLVE THIS.
# we need to add the decoraters for the checking of "users behavior"

# In "view.py" 
<!-- from django.contrib.auth.decorators import login_required -->

@ the top of the function[def profile] add the decorater, 

<!-- @login_required -> 

    This decorater will check whether the user has loggin in or not, if the user is not logged in, then redirectes to the loginpage. -->

# Try to access the "profile/" without logging in 
[GET404ERROR]
    <!-- [Page not found (404)
    Request Method:	GET
    Request URL: http://127.0.0.1:8000/accounts/login/?next=/profile/] -->

# As the django is trying to access this link[accounts/login/?next=/profile/] after the accessing profile page, we need to send the django to login page,

# to redirect in settings 
<!-- LOGIN_URL ='login' -->

# Now works perfect.[login/?next=/profile/]-> this indicates that if the user is logged in next, send user to profile page.

# Now as it is displaying only the username of the user, lets make it little intresting showing images as well.

# So build an model, where can add attributes for the "profile.py" page, to db.
<!-- from django.contrib.auth.models import User -->

<!-- class Profile(models.Model)
         user = models.OneToOneField(User, on_delete=models.CASCADE)->OneToOneField(this function matches the records from User db)image = models.ImageField(default='default.jpg',upload_to='profile_pics')
         
        def __str__(self):
            return f'{self.user.username} Profile'-->[with this name the profile will be saved in db[admin panel as well]]

# Now make changes in the database to maike changes, we need to add it to database. i.e-migrations

<!-- python3 manage.py make migrations -->
<!-- python3 manage.py migration -->

# run the server after changes.

# Adding the profile content to Admin Page[in "admin.py" file register the page]
<!-- from .models import Profile
        admin.site.register(Profile) -->
# Now to Check for the details or to run query make shell terminal
<!-- python3 manage.py shell -->
>> from django.contrib.auth.models import User
>> user = User.objects.filter(username='amith')
>> user
>> user.profile
>> user.profile.image
>> user,profile.image.width

# AS PROFILE GETS MORE ,STORING IMAGES IN A DIRECTCY WILL BE NOT EFFICIENT SO, MAKING IT A SINGLE DIRECTORY UNDER THE PROJECT   WHICH MAKES MORE EFFICIENT TO GET THE IMAGES WHEN NEEDED.

# [To get the images to be stored in a static file for all the user,[IN-SETTINGS]]
# [MEDIA_ROOT=os.path.join(BASE_DIR,'media')] -> which creates the new directory under the main projects and all the images will be saved under this directory.[NO MATTER WHAT OS USER ID USING, HE GETS THE IMAGES DISPLAYED WITH THE FULL PATH JOINED.]

# [MEDIA_URL='/media/'] -> the link for the websites to store the images.[IT IS AN PUBLIC URL]


# MAKING SOME CHANGES IN THE "PROFILE.PY" AS DISPLAYING THE IMAGE ON THE PAGE.
<!-- {% extends 'blog/base.html'%} 
     {% load crispy_forms_tags %}
     {% block content %}
        <div class = 'content-section'>
            <div class = 'media'>
                <img class = 'rounded-circle account-img', src='{{user.profile.image.url}}'>
                <div class = 'media-body'>
                    <h2 class = 'account-heading'> {{user.username}}</h2>
                    <p class = 'text-secondary'> {{user.email}}</p>
                </div>
            </div>
        </div>
    {% endblock content %}-->

# This bootstarp page will give the viewable look for the user profile.

# AS THE [MEDIA_URL] IS BEEN ADDED IN SETTINGS, NEED TO ADD THAT IN URLS. AS WELL TO WORK,

<!-- from django.cong import settings           -> [from settings getting the media_url and path]
     from django.conf.urls.static import static --> [getting the static images from media_root]

# [THIS-WORKS-ONLY-WHEN-THE-SETTINGS-IS-IN-DEBUG-MODE]

<!-- if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) -->[Adding the link to save the images]

# As we dnt have any "default.jgp" images, add the default image in the media file.[named=default.jpg]

# Everytime a suer login in need to create the profile from teh admin page, to avoid that making it automate is simpler way.

# [SIGNALS]->    USING THE SIGNALS FETCH THE DATA IN THE BACKEND AND CREATING A PROFILE AUTOMATICAALY.

 # [LOGIC-> IF profile is posted and saved[POST_SAVE]], 
 <!-- from django.db.models.signals import post_save -->[a signal gets fired/generated once the post is saved.]
 <!-- from django.contrib.auth.models import User -->   [a signal to fetch the data of the current user][it also acts a [Sender]]
<!--  from django.dispatch import receiver -->          [dispatch function dispathes the content throug receiver.]
<!--  from .models import Profile -->                   [to get the data from the profile to diplay]

<!-- @receiver(post_save, sender=User)  -->
         -> this decorations sends the signal as created when the post is saved by the user.[which is createdin next argumnet]
<!-- def create_profile(sender,created,instance, **kwargs): -->
         -> [sender=User,instance=object-created-for-profile,created=a-boolen-which-tells-profile-is-created-or!not]
<!--    if created:
            Profile.objects.create(user=instance) -->
    -> [instance created by the User is added to user]["instance is like": user=User.objects.filter(username='instance/object')]
 
 # Full Code of function
 <!-- @receiver(post_save,sender=User) 
      def create_profile(sender, created,instance, **kwargs)
                if created:
                    Profile.objects.create(user=instance) -->

# To save the profile
<!-- @receiver(post_save, sender=User)
      def save_profile(sender, instance, **kwargs) [as we are just saving we dnt need created.]
        instance.profile.save() -->  -> For Saving the profile in admin panel.[instance=user]
    
# In the "apps.py" we need to  import the signals 

<!-- def ready(self):
        import users.signals --> [this is done because of some safety as per "django.document"]
        




[# update the existing details]
# [########################################################################]
# Now lets try to update the user information in the profile page itself.
# To update the details we need form, so already we a form for the "register.py"[UserRegisterForm], There it self add the 2 more function.

[There attributes and the fields.]
# [User Details Updations]
<!-- def UserUpdateForm(forms.ModelForms) -> "inheriting the ModelForms[which gives the default forms structure]"
        email=forms.EmailField()
        phone_number=forms.Charfield()
        
        class Meta: -> this is part of the function which creates a link with the original-form and our-form
            model = User  -> we get the attributes required from the User DataBase
            fields = ['username', 'phone_number']-->

# [User Profile Picture Updation]
<!-- def UserProfileForm(forms.ModelForms)

        -> as there is no extra attributes that we need to add for , so we are geting from "Profile model" 

        class Meta:
            model = Profile
            fields = ['image'] -->

[Once this Forms are done we need to linki this to "views.py", from views--> we will be linking to respected "page.html", page[profile.html]]

# in "views.py"

# As we have added the register page we need to add these 2 forms as well

<!-- from .forms import UserRegisterForm, UserUpdateForm,UserProfileForm -->

# [ In the profile function we need to pass these functions as an context]

<!--@login_required
    def profile(request):
        u_form =UserUpdateForm()
        p_form - UserProfileForm()

        context ={
            'u_form':u_form, -> throgh the context passing the attributes 
            'p_form':p_form    -> as preivously we are sending the direct attibutes to the context, instead we are passing the entire form to the context.
        }

        return render(request,'users/profile.html', context)  -->

# As we are passing the context, the context has to be displayed in thr profile form, so create a <div> with<form> add the context into it.
 
 # in "profile.html" page

 <!-- <form method='post' enctype='multipart/form-data'> -> "enctype is use to store the image safely"
            <fieldset class = 'form-group'>
                <legend class='border-bottom mb-4'>Update Profile</legend>
                {{u_form}} -> here the form attributes gets displayed
                {{p_form}} -> here also the image will add option will be displayed
            </fieldset>
            <div class = 'form=group'>
                <button class = 'btn btn-outline-info' type='submit'>Update</button>
            </div>
        </form> -->

# ["The above form should be after the display of user-profile"].

# [Run-Server_Now] # pyton3 manage.py runserver

# here once we are click on update button, there is no place where the data is being updated, right..
# to update the data in the back-end, how we did for registration page, same like, nut here we use [instance] of the [user] to update the data.

<!-- if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user) ->[need to post the data, user will the instance]
        p_form=UsaerProfileForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()
            message.success(request,'details updated successfulyy') 
            return redirect('profile')
    else:
        u_form=UserUpdateFrom(instance=request.user) ->if user is not posting anything,then old data will be displayed.
        p_form=UserProfileForm(instance=request.user.profile) ->f user is not posting anything,then old data will be displayed.
--> 

# IMAGE RESIZE:
# as we are saving our users profile image, if the size of the image is more then application gets less perfomance speed, to resize the users image

<!-- from PIL import Image -->

<!-- def save(self):
        super().save() -> firstly it will save the image and then while storing gets resized.
        img = Image.open(self.image.path)
        if img.height>300 and img.width>300:->we are explicitly checking that image hei and wid is>300 then resize,
            resize_img = (300,300)
            img.thumbail(resize_img)
            img.save(self.image.path) -->

# An extra feature
# if u need to add an image at the home page, beside the user profile, then add an image at the "home.html" page.

<img class = 'circle_rounded article-img' scr='{{post.author.profile.image.url}}'>

# [add this inside the arcticle and before the body of the every div.]
