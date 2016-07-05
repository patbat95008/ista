# Copyright 2016 by Dane Collins
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView


from tc.models import TestSteps, TestSession, Media, Comment
from tc.forms import TestInfoForm, MediaForm, CommentForm

# Global App Name
APP_NAME = 'TestPlanner'
steps = TestSteps().steps
step_sequence = sorted(steps.keys())


def set_current_test(request, test_id):
    print('Setting current test to {}'.format(test_id))
    request.session['current_test_id'] = test_id


def get_current_test(request):
    test_id = request.session.get('current_test_id')
    if not test_id:
        return None

    try:
        ts = TestSession.objects.get(id=test_id)
        print('Found test with id={}'.format(test_id))
        return ts
    except TestSession.DoesNotExist:
        return None


def index(request):
    return TemplateView.as_view(template_name="index.html")(request)


def select_test(request):
    which_test = '3A'
    if request.method == 'POST':
        form = TestInfoForm(request.POST)
        if form.is_valid():
            new_ts = form.save(commit=False)
            new_ts.test = which_test
            new_ts.state = 'in-progress'
            new_ts.save()
            set_current_test(request, new_ts.id)
            return redirect('/tc/step/{}'.format(step_sequence[0]))
    else:
        form = TestInfoForm()

        # find all in-progress test sessions
        ts = TestSession.objects.filter(state='in-progress').order_by('item_name')
        test_list = []
        for test in ts:
            test_list.append(dict(id=test.id, desc='{} ({})'.format(test.item_name, test.user)))

        return render(request, 'tc/select.html', {'form': form,
                                                'test': which_test,
                                                'test_list': test_list,
                                                'name': APP_NAME})


def set_test(request, test_id):
    ts = get_object_or_404(TestSession, id=test_id)
    set_current_test(request, test_id)
    if ts.last_step:
        last_step = ts.last_step
    else:
        last_step = step_sequence[0]
        ts.last_step = last_step
        ts.save()
    return redirect('/tc/step/{}/'.format(last_step))


def overview(request, id):
    ts = TestSession.objects.get(id=id)
    return render(request, 'tc/overview.html', {'test': ts.test, 
                                                'item': ts.item_name,
                                                'name': APP_NAME,
                                                'id': id})


def display_step(request, num):
    global steps, step_sequence, APP_NAME
    ts = get_current_test(request)

    if num in steps:
        i = step_sequence.index(num)
        prev = step_sequence[i-1]
        next = step_sequence[i+1]
        s = steps[num]
        page = "tc/{}.html".format(s.page)
        args = dict(name=APP_NAME, page=page, prev=prev, next=next, step=s, current_test=ts)
        ts.last_step = num
        ts.save()
        return render(request, page, args)
    else:
        raise Http404("Poll does not exist")


def get_image(request):
    global steps, step_sequence, APP_NAME
    ts = get_current_test(request)

    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            new_doc = Media(upload=request.FILES['docfile'], session=ts, step=ts.last_step)
            new_doc.save()
            return redirect('/tc/step/{}'.format(ts.last_step))
    else:
        form = MediaForm()
        return render(request, 'tc/get_image.html', {'form': form})


def get_comment(request):
    global steps, step_sequence, APP_NAME
    ts = get_current_test(request)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_doc = Comment(comment=data['comment'], session=ts, step=ts.last_step)
            new_doc.save()
            return redirect('/tc/step/{}'.format(ts.last_step))
    else:
        form = CommentForm()
        return render(request, 'tc/get_comment.html', {'form': form})