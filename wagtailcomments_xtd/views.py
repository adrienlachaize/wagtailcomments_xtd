from django.contrib import messages
from wagtail.wagtailcore.models import Page
from django.shortcuts import redirect, render
from django_comments_xtd.models import XtdComment
from django.utils.translation import ugettext as _
from wagtailcomments_xtd.utils import cleaned_tree


def pages(request):
    comments = XtdComment.objects.all()
    pages = []
    for comment in comments:
        page_model = comment.content_type.model_class()
        page_id = comment.object_pk
        try:
            page = page_model.objects.get(pk=page_id)
            if not any(d['pk'] == page_id and d['model'] == page for d in pages):
                pages.append({
                    'pk': page_id,
                    'model': page})
        except:
            pass
    return render(request, 'wagtailcomments_xtd/pages.html', {
        'pages': pages,
    })


def comments(request, pk):
    page = Page.objects.get(pk=pk)
    comments = XtdComment.objects.filter(object_pk=pk, level=False)

    return render(request, 'wagtailcomments_xtd/comments.html', {
        'page': page,
        'comments': cleaned_tree(comments),
    })


def comment_thread(request, page_pk, comment_pk):
    page = Page.objects.get(pk=page_pk)
    comments = XtdComment.objects.filter(parent_id=comment_pk).exclude(pk=comment_pk)

    return render(request, 'wagtailcomments_xtd/comments.html', {
        'page': page,
        'comment': XtdComment.objects.get(pk=comment_pk),
        'comments': cleaned_tree(comments),
    })


def update(request, page_pk, comment_pk, action):
    comment = XtdComment.objects.get(pk=comment_pk)
    if action == 'unpublish':
        comment.is_public = False
    elif action == 'publish':
        comment.is_public = True
    elif action == 'hide':
        comment.is_removed = True
    elif action == 'show':
        comment.is_removed = False
    comment.save()
    messages.success(request, _("The comment has been updated successfully!"))

    return redirect(request.META.get('HTTP_REFERER'))
