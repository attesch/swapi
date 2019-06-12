from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from resources import views
from resources import schemas
from swapi import views as swapiviews

router = routers.DefaultRouter()

router.register(r"people", views.PeopleViewSet)
router.register(r"planets", views.PlanetViewSet)
router.register(r"films", views.FilmViewSet)
router.register(r"species", views.SpeciesViewSet)
router.register(r"vehicles", views.VehicleViewSet)
router.register(r"starships", views.StarshipViewSet)

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^api/", include(router.urls)),
    url(r"^$", swapiviews.index),
    url(r"^documentation$", swapiviews.documentation),
    url(r"^about$", swapiviews.about),
    url(r"^stats$", swapiviews.stats),
    url(r"^stripe/donation", swapiviews.stripe_donation),
    url(r"^api/people/schema$", schemas.people),
    url(r"^api/planets/schema$", schemas.planets),
    url(r"^api/films/schema$", schemas.films),
    url(r"^api/species/schema$", schemas.species),
    url(r"^api/vehicles/schema$", schemas.vehicles),
    url(r"^api/starships/schema$", schemas.starships),

]
