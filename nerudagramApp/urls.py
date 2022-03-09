from django.urls import path
from nerudagramApp.views import (NerudagramHomePage,
                                NerudagramComoFuncionaView,
                                NerudagramPoemListView,
                                NerudagramPoemDetailView,
                                NerudagramCreateView,
                                NerudagramUpdateView,)

app_name = 'nerudagramApp'

urlpatterns = [
    path('', NerudagramHomePage.as_view(), name='nerudagram'),
    path('crear-poema', NerudagramCreateView.as_view(), name='create'),
    path('<int:pk>/', NerudagramPoemDetailView.as_view(), name='detail'),
    path('editar/<int:pk>/', NerudagramUpdateView.as_view(), name='update'),
    path('como-funciona', NerudagramComoFuncionaView.as_view(), name='como-funciona'),
    path('poemas-creados', NerudagramPoemListView.as_view(), name='poemas-creados')
]
