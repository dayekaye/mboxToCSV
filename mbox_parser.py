import mailbox
import csv
import sys

def more_payloads(message):
	body = ""
	if message.is_multipart():
		for payload in message.get_payload():
			body += more_payloads(payload)
	else:
		if message.get_content_type() == 'text/plain':
			body = message.get_payload(decode=True)
	return body
def date_splitter(message):
    if message.get_all('date'):
        message_string = ''.join(message.get_all('date'))
        splits = message_string.split(",")
        newline = []
        day = ""
        newline.append(splits)
    return newline

writer = csv.writer(open("clean_mail.csv", "wb"))
for message in mailbox.mbox('mailbox2.mbox'):
        body = more_payloads(message)
        #date = date_splitter(message)
        #date[0][0], date[0][1], <-place this in writerow() for date parser
	writer.writerow([message['subject'], message['from'], message['to'],message['x-gmail-labels'],message['x-autoreply'],body])
