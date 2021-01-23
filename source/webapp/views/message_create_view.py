from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
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
        Message.objects.create(author_id=self.request.user.pk,
                               recipient_id=recipient,
                               description=form.data['description'])
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:message_out')