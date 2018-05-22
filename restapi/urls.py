from django.urls import path
from .views import ProposalView

urlpatterns = [
    path('proposals/', ProposalView.as_view())
]
