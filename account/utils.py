import smtplib

from django.http import HttpResponse, JsonResponse # type: ignore

class Utils:
    def send_email(data):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('ayushpathak7776@gmail.com', 'inxbkyqhtnavmrjt')  # Use your real app password
            server.sendmail(
                'ayushpathak7776@gmail.com', 
                data['to_email'],
                f"Subject: {data['subject']}\n\n{data['body']}"
            )
            server.quit()
            return JsonResponse("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse(f"Error: {e}")