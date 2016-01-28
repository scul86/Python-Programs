import urllib, re, gnupg, smtplib, datetime
from email.mime.text import MIMEText

# Gnupg Home
gpg = gnupg.GPG(gpgbinary='gpg2', gnupghome='/home/pi/.gnupg')

# Get current time/date
time = str(datetime.datetime.now())
#print time

# Your own accounts' information.
to = 'xxxxx@comcast.net' # Email to send to. Assumes a matching PGP public key in your keyring.
gmail_user = 'xxxxx@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'xxxxx' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

# Gets current IP address
url = "http://checkip.dyndns.org"
m = re.search('[0-9.]+', urllib.urlopen(url).read())
curr_ip = m.group()

with open('/home/pi/ip_handler/stored_ip', 'r+') as f: # Open file storing current ip
#    f.seek(1, 0)
    f.readline()
    l = f.readline() # Read the second line
#    print l
    if l == curr_ip: # Compares line 2 (old IP) and the new IP
#        print "Match, exiting" # Exits if the IP matches
        exit()
#    print "Writing new IP to file"
    f.seek(0)
    f.write(time+"\n")
    f.write(curr_ip) # Writes the new IP to the file

# Create a message with the new IP included
to_encrypt = "Your current IP is: " + curr_ip+".\n\n-Raspberry Pi"

# Sign and Encrypt the message
sign_by = "xxxxx" #Fingerprint of the signature key
sign_password = "xxxxx" #Password of the signature key
encrypted_data = gpg.encrypt(to_encrypt, to, sign=sign_by, passphrase=sign_password)
encrypted_string = str(encrypted_data)

# Open connection to SMTP server
smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server

msg = MIMEText(encrypted_string)
msg['Subject'] = "Public IP Updated"
msg['From'] = gmail_user
msg['To'] = to
# Send the message.
smtpserver.sendmail(gmail_user, [to], msg.as_string())
#print "Email sent"
# Close connection to the SMTP server.
smtpserver.quit()
