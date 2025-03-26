from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, nfactorial school!")

def add(request, first: int, second: int):
    return HttpResponse(str(first + second))

def upper(request, text: str):
    return HttpResponse(text.upper())

def palindrome(request, word: str):
    return HttpResponse(str(word == word[::-1]))

def calculator(request, first: int, operation: str, second: int):
    if operation == 'add':
        result = first + second
    elif operation == 'sub':
        result = first - second
    elif operation == 'mult':
        result = first * second
    elif operation == 'div':
        if second == 0:
            return HttpResponse("Error: Division by zero")
        result = first / second
    
    return HttpResponse(str(result))



