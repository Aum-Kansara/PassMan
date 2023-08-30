from flask import Flask,render_template
from dotenv import load_dotenv
from os import getenv

load_dotenv()
class Credential:
    id=1
    def __init__(self,title,link,cred_id,passwd):
        self.id="cred"+str(Credential.id)
        Credential.id+=1
        self.link=link
        self.title=title
        self.cred_id=cred_id
        self.passwd=passwd

creds=[Credential("Make.com","https://www.make.com/en",getenv("MAKE_EMAIL"),getenv("MAKE_PASS")),Credential("Voiceflow","https://www.voiceflow.com/",getenv("VOICEFLOW_ID"),getenv("VOICEFLOW_PASS")),Credential("Botpress","https://botpress.com/",getenv("BOTPRESS_ID"),getenv("BOTPRESS_PASS")),Credential("Stripe","https://stripe.com/",getenv("STRIPE_ID"),getenv("STRIPE_PASS")),Credential("Render.com","https://render.com/",getenv("CLICKS_GYM_RENDER_ID"),getenv("CLICKS_GYM_RENDER_PASS"))]

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",creds=creds)


if __name__=="__main__":
    app.run(debug=True)