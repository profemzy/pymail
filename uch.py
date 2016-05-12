import csv

emails_file = open('/home/femzy/emails.txt').read().split(',')
emails = emails_file[0].lower()


email_list = emails.split()
password_list = ['password123'] * 3202

email_dict = dict(zip(email_list, password_list))
email_tuple = email_dict.items()

print email_tuple

with open('email_adds.csv', 'w') as out:
    csv_out = csv.writer(out)
    for row in email_tuple:
        csv_out.writerow(row)



