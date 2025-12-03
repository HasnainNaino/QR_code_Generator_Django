from django.shortcuts import render
from .forms import qr_code
import qrcode
from django.conf import settings
import os


def index(request):
    if request.method == 'POST':
        form = qr_code(request.POST)
        if form.is_valid():
            name = form.cleaned_data['qr_code_name']
            url = form.cleaned_data['url']

            qr = qrcode.make(url)
            file_name = name.replace(" ", "_").lower() + '.png'

            # Save QR code inside STATICFILES_DIRS
            save_path = os.path.join(settings.STATICFILES_DIRS[0], file_name)
            qr.save(save_path)

            context = {
                'name': name,
                'file_url': settings.STATIC_URL + file_name,  # URL for template
            }
            return render(request, "naino_QR_code/qr_result.html", context)
    else:
        form = qr_code()
    return render(request, 'naino_QR_code/index.html', {'form': form})
