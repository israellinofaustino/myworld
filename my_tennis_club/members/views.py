from django.http import HttpResponse
from django.template import loader
from .models import Member


def home(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all().values() #get all the values from Members data
    template = loader.get_template('all_members.html') #load template
    contex = {
        'mymembers': mymembers, # create a object with all the values from mymembers object
    }
    return HttpResponse(template.render(contex, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        'mymembers': mymembers,
        'x': 'Volvo',
        'y': 'Ford',
        'z': 'Fiat',
    }
    return HttpResponse(template.render(context, request)) #create an object named context and fill it with data, and send it as the first parameter in the template.render() function
