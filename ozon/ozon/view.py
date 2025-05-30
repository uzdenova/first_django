from django.http import HttpResponse

def hello_page(self):
    return HttpResponse("<h1>Hello world!</h1>")