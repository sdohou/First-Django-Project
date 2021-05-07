from django.http import JsonResponse

# Create your views here.

data = {
"Name" : "Stephanie Dohou",
"Track" : "Backend",
"Course" : "Python",
"Skills" : "HTML, CSS, Bootstrap, CMS(WordPress)",
"Career Goals" : "QA Analyst, Data Analyst, Fullstack Developer",
"Message" : "Hi, mentors, thank you all so much for all of your help! :)"
}


def data_index(request):
    return JsonResponse(data)