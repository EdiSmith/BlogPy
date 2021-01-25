from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Article
from .serializers import SingleArticleSerializer

class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        # QuerySet
        article_list = Article.objects.all().order_by('-created_at')[:9]

        for article in article_list:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url if article.cover else None,
                'category': article.category.title,
                'created_at': article.created_at.date(),
            })
        
        promote_data = []
        # QuerySet
        article_all_promote = Article.objects.filter(promote=True)

        for promote_article in article_all_promote:
            promote_data.append({
                'title': promote_article.title,
                'cover': promote_article.cover.url if promote_article.cover else None,
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


class AllArticleAPIView(APIView):

    def get(self, request, format=None):
        try:
            # QuerySet
            all_articles = Article.objects.all().order_by('-created_at')[:10]
            data = []

            for article in all_articles:
                data.append({
                    "title": article.title,
                    "cover": article.cover.url if article.cover else None,
                    "content": article.body,
                    "created_at": article.created_at,
                    "category": article.category.title,
                    "author": article.author.user.first_name + ' ' + article.author.user.last_name,
                    "promote": article.promote,
                })

            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticleAPIView(APIView):
    
    def get(self, request, format=None):

        try:
            article_title = request.GET['article_title']
            # QuerySet
            article = Article.objects.filter(title__contains=article_title)
            serializered_data = SingleArticleSerializer(article, many=True)
            data = serializered_data.data

            return Response({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
