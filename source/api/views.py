from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.admin import User
from accounts.models import Friend


class AddFrendsView(APIView):

    def post(self, request):
        data = request.data
        friend = User.objects.filter(pk=int(data))[0]
        friends = Friend.objects.filter(user=request.user, friend=friend)
        if not friends:
            Friend.objects.create(user=request.user, friend=friend)
            return Response({'success': 'добавлен'}, status=status.HTTP_200_OK)
        return Response({'success': 'не добавлен'}, status=status.HTTP_200_OK)


class DeleteFrendsView(APIView):
    def delete(self, request, pk=None):
        friends = get_object_or_404(Friend, user=self.request.user, friend_id=int(pk))
        friends.delete()
        return Response({'success': pk}, status=status.HTTP_200_OK)
        # friend = get_object_or_404(Friend pk=int(pk))
        # frend = User.objects.filter(pk=int(pk)))
        # friends = get_object_or_404(Friend, user=self.request.user, )
        # print(friends)
        # object = self.get_object(notepad_pk)
        # object.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        # Friend(models.Model):
        # if data['serviceexecutor']:
        #     initials = data['serviceexecutor'].split(' ')
        #     service_executor = ServiceExecutor.objects.get(last_name=initials[0])
        #     if int(len(data)) < 2:
        #         return Response({"error": "Заполните все поля"}, status=status.HTTP_400_BAD_REQUEST)
        #     incomes = Incomes.objects.create(services_executor=service_executor,
        #                                      created_by=request.user)
        #     range_product = int((len(data)-1)/4)
        #     for i in range(range_product):
        #         i += 1
        #         title = data[f'title-{i}']
        #         barcode = int(data[f'barcode-{i}'])
        #         qty = int(data[f'qty-{i}'])
        #         purchase_price = Decimal(data[f'purchase-price-{i}'])
        #
        #         new_product = Product.objects.filter(barcode=barcode)
        #         if not new_product:
        #             Product.objects.create(title=title,
        #                                    barcode=barcode)
        #         else:
        #             if new_product[0].title == title and new_product[0].deleted == True:
        #                 new_product[0].deleted = False
        #         product = Product.objects.get(barcode=barcode)
        #         ProductIncomes.objects.create(incomes=incomes,
        #                                       product=product,
        #                                       qty=qty)
        #         product.qty += qty
        #         product.purchase_price = purchase_price
        #         product.save()
        #     return Response({'success': incomes.pk}, status=status.HTTP_200_OK)
        # return Response({"error": "Заполните все поля"}, status=status.HTTP_400_BAD_REQUEST)