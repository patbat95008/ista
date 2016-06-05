# Copyright 2016 by Dane Collins
from django.db import models


class TestSession(models.Model):
    standard = 'standard'
    small = 'small'
    flat = 'flat'
    elongated = 'elongated'
    type_choices = (
        (standard, 'standard'),
        (small, 'small'),
        (flat, 'flat'),
        (elongated, 'elongated')
    )

    item_name = models.CharField(max_length=50)
    user = models.CharField(max_length=50, default='anonymous')
    package_type = models.CharField(max_length=9, choices=type_choices, default=standard)
    test = models.CharField(max_length=10)
    state = models.CharField(max_length=15, default='')
    last_step = models.CharField(max_length=10, default='')


class Media(models.Model):
    """
    Stores images that were captured during a TestSession

    Attributes:
        :upload: the file name of the saved file
        :session: a link to the test session the image belongs to
        :time: a date/time stamp on when the image was captured
        :step: which step during the test session the image was captured
    """
    upload = models.FileField(upload_to='ts_img/%Y/%m/%d/')
    session = models.ForeignKey(TestSession)
    time = models.DateTimeField(auto_now_add=True)
    step = models.CharField(max_length=15, blank=True)


class Comment(models.Model):
    comment = models.CharField(max_length=1024, blank=True)
    session = models.ForeignKey(TestSession)
    time = models.DateTimeField(auto_now_add=True)
    step = models.CharField(max_length=15, blank=True)


class TestStep:
    @classmethod
    def from_csv(cls, line):
        self = cls()

        line = line.strip().split('\t')
        if len(line) == 11:
            (proc, step, standard, flat, small, elongated, min_wt, max_wt, mi, page, desc) = line
            skip = False
        elif len(line) == 12:
            (proc, step, standard, flat, small, elongated, min_wt, max_wt, mi, page, desc, skip) = line
        else:
            print('wrong number of items on line')
            for i, v in enumerate(line.split('\t')):
                print(i, '-', v)
            exit(1)

        pt = dict(standard=standard, flat=flat, small=small, elongated=elongated)
        self.procedure = proc
        self.step = step
        self.package_type = pt
        self.min_wt = min_wt
        self.max_wt = max_wt
        self.more_info = mi
        self.page = page
        self.desc = desc
        self.skip = skip
        return self


def read_test_steps(fn):
    test_steps = {}
    with open(fn, 'U') as fp:
        fp.readline()  # skip header
        for line in fp.readlines():
            ts = TestStep.from_csv(line)
            test_steps[ts.step] = ts
    return(test_steps)


class TestSteps:
    __steps__ = False

    def __init__(self):
        if not TestSteps.__steps__:
            TestSteps.__steps__ = read_test_steps('static/3a_data_table.txt')
        self.steps = TestSteps.__steps__


