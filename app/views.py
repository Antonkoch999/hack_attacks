from django.shortcuts import render


def xss(request):
    """Use <script>alert("This is not secure")</script> in query."""

    if 'q' in request.GET:
        q = request.GET['q']
        return render(request, 'xss_form.html', {'query': q})
    return render(request, 'xss_form.html')
