from django.urls import re_path
from django.contrib import admin
from Remote_User import views as remoteuser
from aComparative_study_onFake_jobPost import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', remoteuser.login, name="login"),
    re_path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    re_path(r'^Search_DataSets/$', remoteuser.Search_DataSets, name="Search_DataSets"),
    re_path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    re_path(r'^Add_DataSet_Details/$', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),

    # Service Provider
    re_path(r'^serviceproviderlogin/$', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    re_path(r'^serviceprovider_home/$', serviceprovider.serviceprovider_home, name="serviceprovider_home"),
    re_path(r'^logout/$', serviceprovider.logout_view, name='logout'),

    re_path(r'^View_Remote_Users/$', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    re_path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts, name="charts"),
    re_path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    re_path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    re_path(r'^Find_Predict_Jop_Post_Type_Details_Ratio/$', serviceprovider.Find_Predict_Jop_Post_Type_Details_Ratio, name="Find_Predict_Jop_Post_Type_Details_Ratio"),
    re_path(r'^logout/$', serviceprovider.logout_view, name='logout'),
    re_path(r'^serviceprovider_home/$', serviceprovider.serviceprovider_home, name="serviceprovider_home"),
    re_path(r'^train_model/$', serviceprovider.train_model, name="train_model"),
    re_path(r'^Predict_Jop_Post_Type_Details/$', serviceprovider.Predict_Jop_Post_Type_Details, name="Predict_Jop_Post_Type_Details"),
    re_path(r'^Download_Trained_DataSets/$', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
