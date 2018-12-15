from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Project, Task, DeveloperForm, Developer


def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'techintapp2/index.html',
                  {'action': 'Wyswietl projekty', 'all_projects': all_projects})


def projects_select(request):
    action = 'Projekty dla klienta "Ja"'
    all_projects = Project.objects.filter(client='Ja')
    return render(request, 'techintapp2/index.html', locals())


def project_details(request, project_id):
    action = 'Projekt o ID = ' + str(project_id)
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'techintapp2/detail.html', locals())


def new_dev(request):
    action = 'Nowy deweloper'
    # jeśli jest to żądanie typu POST, musimy przetworzyć dane z formularza
    if request.method == 'POST':
        # utwórz instancję formularza i zapełnij ją danymi z żądania:
        form = DeveloperForm(request.POST)
        # sprawdź, czy formularz został wypełniony prawidłowo:
        if form.is_valid():
            # przetwarzaj dane w postaci cleaned_data zgodnie z wymaganiami
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            birth_date = form.cleaned_data['date_of_birth']
            dev_supervisor = form.cleaned_data['dev_supervisor']
            height = form.cleaned_data['height']
            new_dev = Developer(
                name=name, email=email, date_of_birth=birth_date, dev_supervisor=dev_supervisor, height=height)
            new_dev.save()
            # przekieruj na nowy adresu URL
            return HttpResponseRedirect('/techintapp2/thanks')

    # jeśli jest to żądanie typu GET (lub jakakolwiek inna metoda) stworzymy pusty formularz
    else:
        form = DeveloperForm()
    return render(request, 'techintapp2/form.html', locals())


def thanks(request):
    action = 'Dziękujemy za wypełnienie formularza ! :-)'
    return render(request, 'techintapp2/thanks.html', locals())

