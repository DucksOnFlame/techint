from django.shortcuts import render


def index(request):
    person = {
        'name': 'Bartek',
        'surname': 'Styczynski',
        'indeks': 's15397'
    }
    return render(request, 'techintapp/index.html', person)


def form(request):
    return render(request, 'techintapp/form.html')


def show(request):
    if not request.POST or request.POST is None:
        return sendError(request)

    if not 'first_name' or not 'age' in request.POST:
        return sendError(request)

    first_name = request.POST.get('first_name')
    age = request.POST.get('age')

    if not first_name or not age:
        return sendError(request)

    dob = 2018 - int(age)

    return render(request, 'techintapp/show.html', {
        "first_name": first_name,
        "age": age,
        "dob": dob
    })


def sendError(request):
    return render(request, 'techintapp/show.html', {
        "errors": 'BLAD! Niepoprawne zadanie!'
    })
