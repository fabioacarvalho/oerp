from django.shortcuts import render
from django.apps import apps


def index(request):
    return render(request, 'base/home.html', locals())


def changelist(request, app, model):
    try:
        _model = apps.get_model(app_label=app, model_name=model)
    except LookupError:
        _model = None

    if _model:
        values = _model.objects.all()
        title = _model._meta.verbose_name_plural


    return render(request, 'base/changelist.html', locals())


def changeform(request, app, model):
    return render(request, 'base/changeform.html', locals())
