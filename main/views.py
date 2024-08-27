from django.shortcuts import render, HttpResponse
from translate import Translator

# Create your views here.
def home(request):
    if request.method == "POST":
        text_to_translate = request.POST['translate']
        print(text_to_translate)
        language = request.POST['language']
        translator = Translator(to_lang=language)
        translation = translator.translate(text_to_translate)
        return HttpResponse(translation)
    return render(request, "main/index.html")

