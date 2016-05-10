import csv

hey = open('/home/femzy/emails.txt').read().split(',')
emails = hey[0]
mail_list = emails.split()
password = ['password123'] * 40

email_dict = dict(zip(mail_list, password))
email_tuple = email_dict.items()

with open('email_adds.csv', 'w') as out:
    csv_out = csv.writer(out)
    for row in email_tuple:
        csv_out.writerow(row)
