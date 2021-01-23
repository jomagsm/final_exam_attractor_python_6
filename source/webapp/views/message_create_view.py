from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import MessageCreateForm
from webapp.models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'message_create.html'
    form_class = MessageCreateForm
    model = Message

    def form_valid(self, form):
        recipient = self.kwargs.get('pk')
        Message.objects.create(author=self.request.user,
                               recipient_id=recipient,
                               description=form.data['description'])
        return super().form_valid(form)

    # def get_success_url(self):
        # return reverse('products:product_list')