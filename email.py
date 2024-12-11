import smtplib

sender_email = 'testautoemail@gmail.com'
password = 'pasword'

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    
    connection.starttls()  
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email
        to_addrs=sender_email
        msg='Subject:Hello Developer...\n\nDue to budget cuts we have to let go some people soon please get ready for the up incoming weeks if you dont see someone in the office you know why most likely dropped form the team')