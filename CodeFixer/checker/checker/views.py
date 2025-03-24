from django.shortcuts import render
from .forms import CodeForm
from .utils import analyze_code

def check_code(request):
    output, errors, fixed_code = "", "", ""

    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            output, errors, fixed_code = analyze_code(code)

    else:
        form = CodeForm()

    return render(request, "checker/code_form.html", {"form": form, "output": output, "errors": errors, "fixed_code": fixed_code})
