from django.shortcuts import render, redirect
from .models import Text
import hashlib
# Create your views here.



def create_sha256_hash(input_text):
    input_bytes = input_text.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_bytes)
    return sha256_hash.hexdigest()

def main(request):
    if request.method == "POST":
        content = request.POST.get('text')
        new_entry = Text(
            content = content,
            url = create_sha256_hash(content)
        )
        new_entry.save()
        return render(request, 'index.html', {'url': new_entry.url})
    return render(request, 'index.html')


def share_text(request, sha):
    item = Text.objects.get(url=sha)
    return render(request, 'shared.html', {'content': item})

def edit_text(request, sha):
    item = Text.objects.get(url=sha)
    if request.method == "POST":
        content = request.POST.get('text')
        item.content = content
        item.save()
        return redirect('index')
    else:
        return render(request, 'edit.html', {'content': item})