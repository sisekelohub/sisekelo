from django.shortcuts import render
from .forms import ApplicationForm
from django.contrib.auth.decorators import login_required


@login_required
def post_new(request):
    form = ApplicationForm()
    return render(request, 'application/application.html', {'form': form})

 #
# def application(request):
# 	context = {
# 		"hello" = "hello"
# 	}
# 	render (request, "application/application.html" context )


# def post_new(request):
#     form = ApplicationForm()
#     return render(request, ', {'form': form})'
