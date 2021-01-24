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
        
        promote_data = []
        article_all_promote = Article.objects.filter(promote=True)

        for promote_article in article_all_promote:
            promote_data.append({
                'title': promote_article.title,
                'cover': promote_article.cover.url,
                'category': promote_article.category.title,
                'created_at': promote_article.created_at.date(),
                'author': promote_article.author.user.first_name + " " + promote_article.author.user.last_name ,
                'avatar': promote_article.author.avatar.url,
            })

        
        context = {
            'article_data': article_data,
            'promote_data': promote_data,
        }
        return render(request, 'index.html', context)

class ContactPage(TemplateView):
    template_name = 'page-contact.html'
