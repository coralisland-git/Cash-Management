"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url,include

from django.contrib import admin

from mydemo import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', views.login, name="login"),

    url(r'^home/$', views.home, name="home"),

    url(r'^signup/$', views.signup, name="signup"),

    url(r'^logout/$', views.logout, name="logout"),

    url(r'^changePwd/$', views.changePwd, name="changePwd"),
    
    url(r'^forgot/$', views.forgot, name="forgot"),
    
    url(r'^invoice_board/$', views.invoice_board, name='invoice_board'),
    
    url(r'^invoice_simple_board/$', views.invoice_simple_board, name='invoice_simple_board'),
    
    url(r'^timecard_board/$', views.timecard_board, name='timecard_board'),
    
    url(r'^timecard_hb_board/$', views.timecard_hb_board, name='timecard_hb_board'),

    url(r'^reconkeys_board/$', views.reconkeys_board, name='reconkeys_board'),
    
    url(r'^reconkeys_hb_board/$', views.reconkeys_hb_board, name='reconkeys_hb_board'),
    
    url(r'^payment_board/$', views.payment_board, name='payment_board'),
    
    url(r'^generated_invoice/$', views.generated_invoice, name='generated_invoice'),
    
    url(r'^imported_payment/$', views.imported_payment, name='imported_payment'),
    
    url(r'^unused_paymenet/$', views.unused_payment, name='unused_payment'),

    url(r'^unused_invoice/$', views.unused_invoice, name='unused_invoice'),
    
    url(r'^matching_by_recon_key/$', views.matching_by_recon_key, name='matching_by_recon_key'),
    
    url(r'^report/$', views.report, name='report'),
    
    url(r'^clear_data/$', views.clear_data, name='clear_data'),
    
    url(r'^remove_data/$', views.remove_data, name='remove_data'),
    
    url(r'^search_batch_no/$', views.search_batch_no, name='search_batch_no'),

    url(r'^cash_post/$', views.cash_post, name='cash_post'),

    url(r'^save_comment/$', views.save_comment, name='save_comment'),

    url(r'^calculate/$', views.calculate, name='calculate'),

]
