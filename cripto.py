import urllib2
import json
import string
import hashlib
import requests

token = 'b300b07b62bb08881c487ad0e70b31c0b87fe098'

# contents = urllib2.urlopen("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=%s" % token).read()

# json_file = open('answer.json', 'w')
# json_file.write(contents)
# json_file.close()

json_file = open('answer.json', 'rb')
content = json.load(json_file)
cypher = content['cifrado']
json_file.close()




multipart_form_data = {
    'answer': ('answer.json', open('answer.json', 'rb')),
}

response = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=%s' % token,
                            files=multipart_form_data)

print(response)

# decript = ''

# # print cypher

# for char in cypher:
#     if char.isalpha():
#         idx = string.ascii_lowercase.index(char)
#         result = idx - content['numero_casas']
#         if result < 0:
#             result += 26
        
#         decript += string.ascii_lowercase[result]
#     else:
#         decript += char

# # print decript

# sha1 = hashlib.sha1(decript.encode('utf-8')).hexdigest()

# # print sha1