from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from .forms import PostForm



def feedback(request):
  template = loader.get_template('feedback.html')
  if request.method == "POST":
    form = PostForm(request.POST)
    form.save()
    return HttpResponseRedirect("/")
  else:
    form = PostForm()
  contex = {
    'form': form
  }
  return HttpResponse(template.render(contex, request))



def homepage(request):
  template = loader.get_template('master.html')
  return HttpResponse(template.render())



def members(request):
    mymembers = Member.objects.all().values() #get all the values from Members data
    template = loader.get_template('all_members.html') #load template
    contex = {
        'mymembers': mymembers, # create a object with all the values from mymembers object
    }
    return HttpResponse(template.render(contex, request))



def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))



def testing(request):
    mymembers = Member.objects.all().values()
    membersfirstname = Member.objects.values_list('firstname')
    user1 = Member.objects.filter(id='2').values()
    startwith = Member.objects.filter(firstname__startswith='L').values()
    order = Member.objects.all().order_by('firstname').values()
    template = loader.get_template("template.html")
    context = {
        'order': order,
        'startwith': startwith,
        'user1': user1,
        'membersfirstname': membersfirstname,
        'mymembers': mymembers,
        'x': 'Volvo',
        'y': 'Ford',
        'z': 'Fiat',
        'emptytestobject': [],
    }
    return HttpResponse(template.render(context, request)) #create an object named context and fill it with data, and send it as the first parameter in the template.render() function
