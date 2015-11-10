from refData.models import Article, Product, Company
from tags.models import EthicsType
from refData.serializers import ArticleSerializer, ProductSerializer, ProductSimpleSerializer, \
       ArticleEthicsTagsSerializer, ArticleMetaTagsSerializer, CompanySerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.db.models import Count, Prefetch
import django_filters

class ArticleNoTagView(generics.ListAPIView):
    queryset = Article.objects.annotate(c=Count('ethicstags',distinct=True),
            d=Count('metatags')).filter(c=0,d=0)
    serializer_class = ArticleSerializer

class ArticleWithCrossView(generics.ListAPIView):
    queryset= Article.objects.prefetch_related(
        'ethicstags__company',
        Prefetch('ethicstags__tag_type', queryset=EthicsType.objects.select_related('subcategory'))
        ).annotate(c=Count('ethicstags')).filter(c__gte=1)
    serializer_class = ArticleEthicsTagsSerializer;

class UpdateArticleView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset= Article.objects.all()
    permission_classes = (IsAuthenticated,)    

class NewArticleView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    queryset= Article.objects.all()
    permission_classes = (IsAuthenticated,)    

    def create(self, request, *args, **kwargs):
        request.data['added_by'] = request.user.id
        return super(NewArticleView,self).create(request,*args,**kwargs)

class ArticleNoDataView(generics.ListAPIView):
    serializer_class = ArticleMetaTagsSerializer
    queryset = Article.objects.filter(metatags__tag_type=1)
        
class AllCompaniesView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class ProductListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Product
        fields = ['name']

class ProductListView(generics.ListAPIView):
    model = Product
    serializer_class = ProductSimpleSerializer
    queryset = Product.objects.all()

    # Filter tools
    filter_class = ProductListFilter
    filter_backends = (filters.DjangoFilterBackend,)
