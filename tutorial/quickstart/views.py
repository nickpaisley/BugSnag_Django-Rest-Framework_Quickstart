from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


import bugsnag


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

    # don't want to check in local dev e.g. if using Postman...
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["post"])
    def notify_bugsnag(self, request):
        bugsnag.notify(TypeError("Button clicked"))
        return Response("Bugsnag notified")


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # don't want to check in local dev e.g. if using Postman...
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get", "post"])
    def notify_bugsnag(self, request):
        bugsnag.notify(TypeError("Button clicked"))
        return Response("Bugsnag notified")
