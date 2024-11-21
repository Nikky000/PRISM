from celery import Celery
from celery import shared_task
app = Celery('django_app')

app.config_from_object('django.cong:settings',namespace="CELERY")

from home.utils.github import analyze_pr

@shared_task
def analyse_repo_task(repo_url,pr_number,github_token = None):
    result =  analyze_pr(repo_url,pr_number,github_token)
    return result