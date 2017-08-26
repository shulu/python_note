# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'sl19911202329@hotmail.com'
#input('from: ')
pwd = 'SHU1202LU'
#input('password: ')
to_addr = '1586356520@qq.com'
#input('To: ')
#smtp_server = 'smtp.163.com'
smtp_server = 'smtp.live.com'
#smtp_server = 'smtp.qq.com'
#input('SMTP server: ')

#'Content-Type: text/plain; charset="utf-8"\r\n' \
#'MIME-Version: 1.0\r\n' \
#'Content-Transfer-Encoding: base64\r\n' \
#'From: =?utf-8?b?UHl0aG9uIOeIseWlveiAhQ==?= <sl19911202329@hotmail.com>\r\n' \
#'To: =?utf-8?b?566h55CG5ZGY?= <1586356520@qq.com>\r\n' \
#'Subject: =?utf-8?b?5p2l6IeqU01UUOeahOmXruWAmS4uLi4=?=\r\n\r\naGVsbG8sIHRoaXMgaXMgc2VuZCBmcm9tIHB5dGhvbg==\r\n.\r\n
#邮件对象
msg = MIMEMultipart()

msg['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....', 'utf-8').encode()
#邮件正文是MIMEtxt
#msg.attach(MIMEText('hello, this is send from python', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
'<p>send by <a href="http://www.python.org">Python</a>...</p>' +
'<p><img src="cid:0"></p>'
'</body></html>', 'html', 'utf-8'))
with open('attach.jpg', 'rb') as f:
    # 设置附件的MIME和文件名
    mime = MIMEBase('image', 'jpeg', file = 'attach.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename = 'attach.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)



# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.starttls()
server.login(from_addr, pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()




