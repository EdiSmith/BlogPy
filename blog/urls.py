from django.urls import path
from django.conf.urls import url
from .views import (
    IndexPage,
    AllArticleAPIView,
    ContactPage,
    SingleArticleAPIView,
    SearchArticleAPIView,
    SubmitArticleAPIView,
)


urlpatterns = [
    path('contact/', ContactPage.as_view(), name='contact'),
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^article/$', SingleArticleAPIView.as_view(), name='single_article'),
    url(r'^article/search/$', SearchArticleAPIView.as_view(), name='search_article'),
    url(r'^article/submit/$', SubmitArticleAPIView.as_view(), name='submit_article'),
    url(r'^article/all/$', AllArticleAPIView.as_view(), name='all_articles'),
]
