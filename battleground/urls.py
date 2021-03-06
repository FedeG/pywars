from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail


urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^.*$', TemplateView.as_view(template_name='now_playing.html'), name='now_playing'),
    url(r'^accounts/register$', RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    url(r'^$', 'game.views.index', name='index'),
    url(r'^(?P<match_id>\d+)$', 'game.views.index', name='view_match'),
    url(r'^scoreboard$', 'game.views.scoreboard', name='scoreboard'),
    url(r'^tournament$', 'game.views.tournament', name='tournament'),
    url(r'^mybots$', 'game.views.mybots', name='mybots'),
    url(r'^about$', 'game.views.about', name='about'),
    url(r'^challenge$', 'game.views.challenge', name='challenge'),
    #url(r'^update_bot', 'game.views.update_bot', name='upload'),
    url(r'^main-match$', 'game.views.main_match', name='main_match'),
    url(r'^my-matches$', 'game.views.my_matches', name='my_matches'),
    url(r'^test-match$', 'game.views.random_test_match', name='test_match'),
    url(r'^get_match/(\d+)$', 'game.views.get_match', name='get_match'),
    url(r'^bot_code/(\d+)$', 'game.views.bot_code', name='bot_code'),
    url(r'^get_playlist$', 'game.views.get_playlist', name='get_playlist'),
    url(r'^get_bot_status/(\d+)$', 'game.views.get_bot_status', name='get_bot_status'),

    # Uncomment the next line to enable the admin:
    (r'^accounts/', include('registration.backends.default.urls')),
)
