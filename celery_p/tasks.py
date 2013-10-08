from celery.task import task
from urllib import urlopen
from django.core.mail import send_mail
from celery_p.settings import EMAIL_HOST_USER

@task
def send_pars(url, email):
    try:
        source = urlopen(url).read()
        send_mail('html-source', source, EMAIL_HOST_USER, [email])
        return True

    except:
        return False


