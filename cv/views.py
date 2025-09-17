from django.shortcuts import render
from django.conf import settings
import json

def cv_view(request):
    data_file = settings.BASE_DIR / "data" / "cv_data.json"
    with open(data_file, "r", encoding="utf-8") as f:
        context = json.load(f)
    return render(request, "cv.html", context)
