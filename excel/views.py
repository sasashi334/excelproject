from django.shortcuts import render, redirect
from .models import History
from .forms import FileUploadForm
from .exec import edit
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


# Create your views here.


@login_required
def index(request):
    file_obj = History.objects.filter(user=request.user).order_by("-date")
    return render(request, "excel/index.html", {"file_obj": file_obj})


@login_required
def edit_file(request):

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            print(form.instance.file.url)
            form.save()
            if request.POST["removestr"]=="":
                edit("/home/masas/django/excel/excelproject"+form.instance.file.url, request.POST["num"], request.POST["RowOrCol"], None)
            else:
                edit("/home/masas/django/excel/excelproject"+form.instance.file.url, request.POST["num"], request.POST["RowOrCol"], request.POST["removestr"])
            return redirect("excel:index")
    else:
        form = FileUploadForm()
    return render(request, "excel/edit.html", {"form": form})


def delete_func(request, pk):
    file = History.objects.filter(pk=pk)

    if file[0].user != request.user:
        raise PermissionDenied

    if request.method == "POST":
        file.delete()
        return redirect("excel:index")
    else:
        return render(request, "excel/delete.html", {"file": file})
