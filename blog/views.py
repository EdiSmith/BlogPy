from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Article


class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        article_list = Article.objects.all().order_by('-created_at')[:9]

        for article in article_list:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at.date(),
            })

        context = {
            'article_data': article_data,
        }
        return render(request, 'index.html', context)