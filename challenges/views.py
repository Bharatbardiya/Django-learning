from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })
        
def monthly_challenge_by_month(request, month:int):
    months = list(monthly_challenges.keys())
    if( month > len(months)):
        return HttpResponseNotFound("invalid month number")
    # print(months)
    redirect_month = months[month-1]
    # print(redirect_month)
    
    redirect_path = reverse("month_challenge", args=[redirect_month])
    # print(redirect_path)
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    
    # print(month)
    
    try:
        
        # challenge_text = render_to_string("challenges/challenge.html")
        # return HttpResponse(challenge_text)
        # or
        challenge = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text":challenge,
            "month": month,
        })
    except:
        return HttpResponseNotFound("month not sported")
    
        