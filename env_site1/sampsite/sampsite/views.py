from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello world")

def root_page(request):
    return HttpResponse("Hello World Root Home Page")

def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))
    msg = "Random Number Between 0 and %s : %d" % (max_rand, random_num)
    return HttpResponse(msg)