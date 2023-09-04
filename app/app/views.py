"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

class TemplateView:

    def home(self, request):
        """Renders the home page."""
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )
