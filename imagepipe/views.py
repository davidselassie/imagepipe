"""imagepipe Views."""
from django.shortcuts import render
from django.http import JsonResponse

from . import logic


def render_mashup_index(request):
    """Render the template that lists all recent Mashups."""
    template_args = {
        'mashups': logic.get_mashups(),
    }
    return render(request, 'imagepipe/mashup_index.html', template_args)


def render_mashup(request, mashup_id):
    """Render the template that shows a single Mashup by ID."""
    mashup_id = int(mashup_id)
    template_args = {
        'mashup': logic.get_mashup(mashup_id),
    }
    return render(request, 'imagepipe/mashup.html', template_args)


def render_src_index(request):
    """Render the template that lists all recent Sources."""
    template_args = {
        'srcs': logic.get_srcs(),
    }
    return render(request, 'imagepipe/src_index.html', template_args)


def render_upload(request):
    """Render the upload form template."""
    return render(request, 'imagepipe/upload.html')


def return_upload_submit(request):
    src_image_file = request.FILES['src-image-file']
    src_title = request.POST['src-title']

    src_model = logic.create_src_model(src_image_file, src_title)
    logic.attempt_create_mashup()

    return JsonResponse({'id': src_model.id})
