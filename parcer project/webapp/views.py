from django.shortcuts import render, redirect
from django.contrib import messages
from config.services.config_service import ConfigService
from config.storage.json_storage import JSONStorage
from webapp.services.parser import Parser


def index(request):
    return redirect("get-config-form")


def get_config_form(request):
    if request.method == "POST":
        url = request.POST.get('url')
        filename = request.POST.get('filename')
        field_names = request.POST.getlist('selector-field-name')
        css_selectors = request.POST.getlist('selector-css-name')
        selectors = dict(zip(field_names, css_selectors))
        req_fields = request.POST.getlist('req-field-name')
        req_ops = request.POST.getlist('req-operator')
        req_vals = request.POST.getlist('req-value-name')
        requirements = [
                {"field": f, "operator": o, "value": v}
                for f, o, v in zip(req_fields, req_ops, req_vals)
            ]
        storage = JSONStorage()
        service = ConfigService(storage=storage)
            
        config = service.create_config(
            url=url,
            selectors=selectors,
            requirements=requirements
        )
        service.save_config(config, filename)
            
        parsed_data = Parser.parse(filename)
        messages.success(request, f"Конфигурация сохранена: {filename}")
        return render(request, 'webapp/create_config.html', {'parsed_data': parsed_data})

    return render(request, 'webapp/create_config.html')