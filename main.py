from flask import Flask, request
import vk_api, random, json

app = Flask(__name__)

vk = vk_api.VkApi(token='')
vk._auth_token()

owner_id = -168002791

data_answers = []
data_words = []

with open("/home/botcomment/mysite/data_answers.txt", "r", encoding='utf-8', errors='ignore') as read_file:
    for line in read_file:
        data_answers.append(line.strip('\n'))

with open("/home/botcomment/mysite/data_words.txt", "r", encoding='utf-8', errors='ignore') as read_file:
    for line in read_file:
        data_words.append(line.strip('\n'))

def comment(post_id, text):
    vk.method('wall.createComment', {'owner_id':owner_id, 'post_id':post_id, 'message':text, 'from_group':-owner_id})

def create_comment(post_id, text, reply_to_comment):
    vk.method('wall.createComment', {'owner_id':owner_id, 'post_id':post_id, 'message':text, 'reply_to_comment':reply_to_comment, 'from_group':-owner_id})

@app.route('/', methods=['POST'])
def index():
    data = json.loads(request.data)
    if(data["type"] == "confirmation"):
        return "77be30ef"
    elif(data["type"] == "wall_reply_new"):
        if(data['object']['from_id'] != owner_id):
            create_comment(data['object']['post_id'], data_answers[random.randint(0, len(baza1))], data['object']['id'])
        return "ok"
    elif(data["type"] == "wall_post_new"):
        comment(data['object']['id'], "Сможешь написать слово " + data_words[random.randint(0, len(baza2))] + " по буквам, чтобы тебя никто не перебил? 😃")

if __name__ == "__main__":
    app.run()
