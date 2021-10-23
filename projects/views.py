from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import InvestCalcForm, ProjectForm
from .models import Project


def index(request):
    template_name = "index.html"
    form = InvestCalcForm()
    qs = Project.objects.filter(is_active=True)
    context = {"object_list": qs, "form": form}
    return render(request, template_name, context)


def create_project(request):
    template_name = "projects/create-update.html"
    form = ProjectForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        obj = form.save()
        if request.htmx:
            headers = {"HX-Redirect": obj.get_absolute_url()}
            return HttpResponse("Criado", headers=headers)
        return redirect(obj.get_absolute_url())
    else:
        return render(request, template_name, context)
    return render(request, template_name, context)


@login_required
def update_project(request, id=None):
    obj = get_object_or_404(Project, id=id)
    form = ProjectForm(request.POST or None, instance=obj)

    context = {
        "form": form,
        "object": obj,
    }
    if form.is_valid():
        form.save()
        context["message"] = "Atualizado com sucesso!"
        return redirect(obj.get_absolute_url())
    return render(request, "projects/create-update.html", context)


@login_required
def delete_project(request, id=None):
    try:
        obj = Project.objects.get(id=id)
    except Exception as e:
        print(e)
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Não Encontrado")
        raise Http404
    if request.method == "POST":
        obj.is_active = False
        obj.save()
        success_url = reverse("projects:index")
        if request.htmx:
            headers = {"HX-Redirect": success_url}
            return HttpResponse("Deletado", headers=headers)
        return redirect(success_url)
    context = {"object": obj}
    return render(request, "projects/delete.html", context)


@login_required
def calculate_project_risk(request, id=None):
    if request.is_ajax():
        response = {"success": False}
        input_value = request.GET.get("input_value")
        input_value = float(input_value)
        obj = Project.objects.filter(id=id)[0]
        if obj:
            value_obj = obj.value
            if value_obj > input_value:
                response[
                    "lower_value"
                ] = "Valor do investimento não pode ser inferior ao valor do projeto"
                return JsonResponse(response, safe=False)
            else:
                risk_obj = int(obj.risk)
                if risk_obj == 5:
                    percent_risk = f"0.0{risk_obj}"
                else:
                    percent_risk = f"0.{risk_obj}"
                return_investment = input_value * float(percent_risk)
                response[
                    "return_investment"
                ] = f"Retorno R$ {return_investment:.2f}"
                response["success"] = True
        return JsonResponse(response, safe=False)
