from django.http import HttpResponse
from django.core.validators import email_re, URLValidator
from celery_p.tasks import send_pars


def parse(request, url, email):
    url = 'http://' + url
    url_re = URLValidator.regex

    if url_re.match(url) and email_re.match(email) is not None:
        send_pars.delay(url = url, email = email)
        return HttpResponse('Data send success')

    else:
        return HttpResponse('Input problem, try again')


