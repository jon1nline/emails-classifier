import fitz
from django.shortcuts import render

from utils.ai_service import classify_email, generate_response


def process_email(request):
    classification = None
    response_suggestion = None
    email_text = ""

    if request.method == "POST":
        # Prioriza o upload de arquivo sobre o texto direto
        if "email_file" in request.FILES:
            uploaded_file = request.FILES["email_file"]

            # Lê o conteúdo do arquivo
            if uploaded_file.name.endswith(".pdf"):
                doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                for page in doc:
                    email_text += page.get_text()
            elif uploaded_file.name.endswith(".txt"):
                email_text = uploaded_file.read().decode("utf-8")
        else:
            email_text = request.POST.get("email_text", "")

        if email_text:
            # Chama a API de AI para processar o texto
            classification = classify_email(email_text)
            response_suggestion = generate_response(classification)

    context = {
        "classification": classification,
        "response_suggestion": response_suggestion,
        "email_text": email_text,
    }
    return render(request, "email_classifier/index.html", context)
