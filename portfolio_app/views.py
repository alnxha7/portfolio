from django.shortcuts import render, redirect
from .models import DownloadCV, Projects, Languages, Skills, Awards, Experiences, Educations, Icons
from sib_api_v3_sdk.rest import ApiException
import sib_api_v3_sdk
from django.contrib import messages
from django.conf import settings

def home(request):
    cv = DownloadCV.objects.filter().first()
    personals = Projects.objects.filter(category='personal')
    productions = Projects.objects.filter(category='production')
    academics = Projects.objects.filter(category='academic')
    languages = Languages.objects.all()
    skills = Skills.objects.all()
    awards = Awards.objects.all()
    educations = Educations.objects.all()
    experiences = Experiences.objects.all()
    icons = Icons.objects.all()
    context = {
        'cv': cv, 
        'personals': personals, 
        'productions': productions, 
        'academics': academics, 
        'languages': languages,
        'skills': skills, 
        'awards': awards, 
        'educations': educations, 
        'experiences': experiences,
        'icons': icons,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = "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"
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

        subject = "New Message from Portfolio Visit"

        # Sender must be your verified email
        sender = {
            "name": "Alansha",
            "email": "alns4rha@gmail.com"  # VERIFIED sender email
        }

        to = [{"email": "alns4rha@gmail.com", "name": "Alansha"}]  # where you receive the message

        html_content = f"""
        <h3>Contact Form Message</h3>
        <p><strong>Name:</strong> {request.POST.get("contact_name")}</p>
        <p><strong>Email:</strong> {request.POST.get("contact_email")}</p>
        <p><strong>Phone:</strong> {request.POST.get("contact_phone")}</p>
        <p><strong>Service:</strong> {request.POST.get("contact_subject")}</p>
        <p><strong>Message:</strong> {request.POST.get("contact_message")}</p>
        """

        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            sender=sender,
            subject=subject,
            html_content=html_content
        )

        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')  
        except ApiException as e:
            messages.error(request, f"Something went wrong: {e}")
            return redirect('error')
        
def error(request):
    return render(request, 'error.html')
