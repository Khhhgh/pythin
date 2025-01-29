import os
os.system("pip install fastapi")
os.system("pip install uvicorn")
os.system("pip install requests")
os.system("pip install user_agent")
os.system("pip install pydantic")
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import re
import random
from user_agent import generate_user_agent as n

app = FastAPI()

# قائمة الحروف لاستخدامها في مولد العشوائية
a = 'qwertyuiopasdfghjklzxcvbnm'

# وظيفة لتوليد المعلومات العشوائية وإجراء الطلب الأول
def to():
    try:
        s1 = "".join(random.choice(a) for _ in range(random.randrange(6, 9)))
        s2 = "".join(random.choice(a) for _ in range(random.randrange(6, 9)))
        s3 = "".join(random.choice(a) for _ in range(random.randrange(15, 30)))

        cookies = {
            '__Host-GAPS': s3,
        }

        headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'upgrade-insecure-requests': '1',
            'user-agent': str(n()),  
        }

        r = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',
            cookies=cookies,
            headers=headers,
        )

        match = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', r.text)
        if not match:
            return None

        tok = match.group(2)

        headers.update({
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?continue=https://www.google.com/search&q=dhduud&hl=ar',
        })

        data = {
            'f.req': f'["{tok}","{s1}","{s2}","{s1}","{s2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }

        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )

        try:
            tl = str(response.text).split('",null,"')[1].split('"')[0]
        except IndexError:
            return None

        host = response.cookies.get('__Host-GAPS', '')

        return tl, host
    except Exception as e:
        return None

# وظيفة للتحقق من توفر البريد الإلكتروني
def S1(tl, host, em):
    try:
        cookies = {
            '__Host-GAPS': host,
        }

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Ddhduud%26oq%3Ddhduud%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzU2OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&hl=ar&parent_directed=true&ddm=1&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tl}',
            'user-agent': str(n()),  
        }

        params = {
            'TL': tl,
        }

        if '@' in em:
            em = em.split('@')[0]

        data = f'continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Ddhduud%26oq%3Ddhduud%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBBzU2OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&ddm=1&flowEntry=SignUp&hl=ar&f.req=%5B%22TL%3A{tl}%22%2C%22{em}%22%2C0%2C0%2C1%2Cnull%2C0%2C4244%5D&at=AFoagUVsrVfPNg-a8rn4W680UeR-MWyEuA%3A1736097014549&azt=AFoagUUrcmcr8XBhg_vKXr4N_weEu2kZlg%3A1736097014549&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A639&checkedDomains=youtube&pstMsg=1&'

        r = requests.post(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )

        if '"gf.uar",1' in r.text:
            return f'Good Email in Gmail: {em}'
        else:
            return f'Bad Email in Gmail: {em}'
    except Exception as e:
        return 'Error'

# مخطط لتحديد شكل البيانات المطلوبة من المستخدم
class EmailRequest(BaseModel):
    email: str

# نقطة النهاية للتحقق من البريد الإلكتروني
@app.get("/Check/Email-Gmail")
async def check_email(email: str):
    if not email:
        raise HTTPException(status_code=400, detail="No email provided")
    
    result = to()
    if result:
        tl, host = result
        status = S1(tl, host, email)
        return {"status": status}
    else:
        raise HTTPException(status_code=500, detail="Error processing email")

# تشغيل التطبيق باستخدام uvicorn
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)