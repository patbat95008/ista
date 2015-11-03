from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView


from tc.models import TestSession
from tc.forms import TestInfoForm

def index(request):
    #log_view(request, 'home_page')
    return TemplateView.as_view(template_name="index.html")(request)


def new_test(request, test_name):
    ts = TestSession(test=test_name)
    ts.save()

    return select_type(request, ts.id)


def select_type(request, id):
    ts = TestSession.objects.get(id=id)
    if request.method == 'POST':
        form = TestInfoForm(request.POST, instance=ts)
        if form.is_valid():
            form.save()
            return redirect('/tc/overview/{}'.format(ts.id))
    else:
        form = TestInfoForm(instance=ts)
        return render(request, 'tc/type.html', {'form': form,
                                                'test': ts.test,
                                                'id': id})


def overview(request, id):
    ts = TestSession.objects.get(id=id)
    return render(request, 'tc/overview.html', {'test': ts.test, 
                                                'item': ts.item_name,
                                                'id': id})


def atm_precon(request, id):
    ts = TestSession.objects.get(id=id)
    return render(request, 'tc/atm_precon.html', {'test': ts.test,
                                                  'item': ts.item_name,
                                                  'id': id})

def atm_con(request, id):
    ts = TestSession.objects.get(id=id)
    return render(request, 'tc/atm_con.html', {'test': ts.test,
                                               'item': ts.item_name,
                                               'id': id})