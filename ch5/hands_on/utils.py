from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_str_email(email_to):
    send_mail(
        '새로운 이메일이 도착했습니다',
        '안녕하세요. Django에서 보낸 이메일입니다.',
        settings.EMAIL_HOST_USER,
        [email_to], # list 형식, 여러명에게 보낼 때도 사용 가능
    )

def send_html_email(email_to):
    subject = "새로운 이메일이 도착했습니다."
    html = render_to_string("email.html") # 이메일을 읽어서 String 형태로 할당
    message = EmailMessage(
        subject,
        html,
        settings.EMAIL_HOST_USER,
        [email_to],
    )
    message.content_subtype = "html" # HTML 형식으로 보내기 위해 설정
    message.send()