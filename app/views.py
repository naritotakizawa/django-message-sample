from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post


class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:post_list')

    def form_valid(self, form):
        self.object = post = form.save()
        messages.info(self.request, f'記事を作成しました。 タイトル:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())


class PostUpdate(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('app:post_list')

    def form_valid(self, form):
        self.object = post = form.save()
        messages.info(self.request, f'記事を更新しました。 タイトル:{post.title} pk:{post.pk}')
        return redirect(self.get_success_url())


class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app:post_list')

    def delete(self, request, *args, **kwargs):
        self.object = post = self.get_object()
        message = f'記事を削除しました。 タイトル:{post.title} pk:{post.pk}'
        post.delete()
        messages.info(self.request, message)
        return redirect(self.get_success_url())
