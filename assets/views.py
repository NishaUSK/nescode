from django.shortcuts import render


def post_list(request):
    return render(request, 'assets/post_list.html', {})
