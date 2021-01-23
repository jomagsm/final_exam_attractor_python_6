from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.admin import User
from accounts.models import Friend


class AddFrendsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        friend = User.objects.filter(pk=int(data))[0]
        friends = Friend.objects.filter(user=request.user, friend=friend)
        if not friends:
            Friend.objects.create(user=request.user, friend=friend)
            return Response({'success': 'добавлен'}, status=status.HTTP_200_OK)
        return Response({'success': 'не добавлен'}, status=status.HTTP_200_OK)


class DeleteFrendsView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk=None):
        friends = get_object_or_404(Friend, user=self.request.user, friend_id=int(pk))
        friends.delete()
        return Response({'success': pk}, status=status.HTTP_200_OK)