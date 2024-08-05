from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
import random

class HomeView(TemplateView):
    template_name = "home.html"
    
# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the uno home page.")

def buildDeck(request):
    deck = []
    colours = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip"," Reverse"]
    wilds = ["Wild"," Wild Draw Four"]
    for colour in colours:
        for value in values:
            cardVal = "{} {}".format(colour, value)
            deck.append(cardVal)
            if value !=0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    print(deck)
    shuffleDeck(deck)
    return JsonResponse(deck, safe=False)

def shuffleDeck(deck):
    deck_size = len(deck)
    for cardPos in range(deck_size):
        randPos = random.randint(0, deck_size - 1)  # Ensure randPos is within the correct range
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    print('shuffled: ', deck)
    # return deck