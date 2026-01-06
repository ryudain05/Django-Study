from django.core.management.base import BaseCommand, CommandError
from utils import send_str_email, send_html_email

# python manage.py send_email 'html' recipient@example.com
class Command(BaseCommand):
    def add_arguments(self, parser): # 명령어에 인자를 추가할 때 사용하는 메서드
        parser.add_argument("format", type=str) # str 형식의 format 인자 추가
        parser.add_argument("email_to", type=str) # str 형식의 email 인자 추가

    def handle(self, *args, **options): # 실제로 명령어가 실행될 때 호출되는 메서드
        match options["format"]:
            case "str":
                send_str_email(email_to=options["email_to"])
            case "html":
                send_html_email(email_to=options["email_to"])
            case _:
                raise CommandError("잘못된 포맷입니다. 'str' 또는 'html'만 허용합니다.")