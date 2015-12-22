from django.conf.urls import url
from refData import views

urlpatterns = [
    url(r'^articles/untagged/$',views.ArticleNoTagView.as_view()),
    url(r'^articles/tagged/$',views.ArticleWithCrossView.as_view()),
    url(r'^articles/tagged/company/(?P<pk>\d+)/$',views.ArticleWithCrossByCompanyView.as_view()),
    url(r'^articles/new/$',views.NewArticleView.as_view()),
    url(r'^articles/(?P<pk>\d+)/$',views.UpdateArticleView.as_view()),
    url(r'^articles/noData/$',views.ArticleNoDataView.as_view()),
    url(r'^companies/all/$',views.AllCompaniesView.as_view()),
    url(r'^companies/(?P<pk>\d+)/$',views.SingleCompanyView.as_view()),
    url(r'^products/list/$',views.ProductListView.as_view()),
    url(r'^products/fetch/$',views.ProductFetchView.as_view()),
    url(r'^products/new/$',views.ProductNewView.as_view()),
]
