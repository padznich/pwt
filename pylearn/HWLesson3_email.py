def send_email():
    import argparse
    import smtplib

    parser = argparse.ArgumentParser()
    parser.add_argument("--to", type=str, required=True, help="Enter the adress of the recipient.")
    parser.add_argument("--user", type=str, required=True, help="Enter the adress of the sender.")
    parser.add_argument("--pw", type=str, required=True, help="Enter the password of the sender.")
    parser.add_argument("--msg", type=str, required=True, help="Enter message content")
    parser.add_argument("--sbj", type=str, help="Enter message subject", default='Never mind.')
    parser.add_argument("--host", type=str, help="Enter SMTP HOST", default='smtp.yandex.ru')
    parser.add_argument("--port", type=int, help="Enter SMTP PORT", default=587)
    args = parser.parse_args()

    smtp_obj = smtplib.SMTP(args.host, args.port)
#    print('DEBUG:', smtp_obj.ehlo())
    smtp_obj.starttls()
    smtp_obj.login(args.user, args.pw)
    smtp_obj.sendmail(args.user, args.to, 'Subject: {}\n\n{}'.format(args.sbj, args.msg))
    smtp_obj.quit()

if __name__ == '__main__':
    send_email()