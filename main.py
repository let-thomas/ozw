import urllib.request
import urllib.parse
import json

if __name__ == '__main__':
    url =  'http://192.168.0.4'
    SerialNr='005A000153B5'
    print("ty wole\n")
    from pprint import pprint

    with urllib.request.urlopen(url + '/api/auth/login.json?user=pycha&pwd=heslopychy') as response:
        sessionResp = json.loads(response.read().decode("utf-8"))
        print(sessionResp)

    if sessionResp['Result']['Success'] == 'true':
        print('mame')
    else:
        print('nemame, padame')
    assert sessionResp['Result']['Success'] == 'true'
    sesId = sessionResp['SessionId']

    # menu nalevo
    with urllib.request.urlopen(url + '/api/menutree/list.json?SessionId=' + sesId) as response:
        listResp = json.loads(response.read().decode("utf-8"))
        print('listResp')
        print(listResp)

    # list pripojenych devices
    with urllib.request.urlopen(url + '/api/devicelist/list.json?SessionId=' + sesId) as response:
        devResp = json.loads(response.read().decode("utf-8"))
        print('devResp')
        print(devResp)

    #SerialNr =  devResp:
    # {'Devices': [
    #     {'TreeDate': '03.01.2018', 'Addr': '0.5', 'TreeGenerated': 'true', 'Name': 'OZW672.01', 'Type': 'OZW672.01',
    #      'SerialNr': '00FD00FF4399', 'TreeTime': '00:00'},
    #     {'TreeDate': '04.11.2015', 'Addr': '1.1', 'TreeGenerated': 'true', 'Name': 'RVS63.283/109',
    #      'Type': 'RVS63.283/109', 'SerialNr': '005A000153B5', 'TreeTime': '12:40'}
    #   ],
    #   'Result': {'Success': 'true'}
    #  }

    # device root
    with urllib.request.urlopen(url + '/api/menutree/device_root.json?SessionId=' + sesId + '&SerialNumber=' +SerialNr+  '&TreeName=Mobile' ) as response:
        devResp = json.loads(response.read().decode("utf-8"))
        print('devResp')
        print(devResp)


    #nejaky point - zadana, korigovana ... + 803
    with urllib.request.urlopen(url + '/api/menutree/datapoint_desc.json?SessionId=' + sesId + '&Id=744') as response:
        ptResp = json.loads(response.read().decode("utf-8"))
        print('ptResp')
        print(ptResp)
    #datum
    with urllib.request.urlopen(url + '/api/menutree/datapoint_desc.json?SessionId=' + sesId + '&Id=918') as response:
        ptResp = json.loads(response.read().decode("utf-8"))
        print('ptResp')
        print(ptResp)

    # 468 - provoz
    # 469 - komfotni zadana
    # 470 - utlumova zadana
    # 502 - cerp tuv
    # 811 - aktual zadana temp
    # 918 - datum cas
    # 502 - vyp
    # 838 - becka dolni + 712
    # 839 - becka stred + 711
    # 907 - becka vrch + 710
    # 901 - venkovni temp + 793
    # 904 - tuv temp, 708
    # 797 - (vyp)
    # 800 - temp pokoj
    # 796 - (vyp)
    # 802 - nabeh + 708
    # 906 - kotel iride = 778 ~ 713
    # 874 - (vyp)
    # 803 - --- `C
    # 837 - zadana tepl akumulace
    # 798 - (zap) asi 3cest topeni smes zavirani
    # 546 - --- `C
    #
    # 414 - pondeli
    # 415 - ut
    # 416 - st
    # 417 - ct
    # 418 - pa
    # 419 - so
    # 420 - ne
    # casy na pondeli
    # with urllib.request.urlopen(url + '/api/menutree/datapoint_desc.json?SessionId=' + sesId + '&Id=414') as response:
    #     ptResp = json.loads(response.read().decode("utf-8"))
    #     print('ptResp')
    #     print(ptResp)

    with urllib.request.urlopen(url + '/api/menutree/datapoint_desc.json?SessionId=' + sesId + '&Id=800') as response:
        ptResp = json.loads(response.read().decode("utf-8"))
        print('ptResp')
        print(ptResp)
    with urllib.request.urlopen(url + '/api/menutree/datapoint_desc.json?SessionId=' + sesId + '&Id=793') as response:
        ptResp = json.loads(response.read().decode("utf-8"))
        print('ptResp')
        print(ptResp)
    with urllib.request.urlopen(url + '/api/menutree/datapoint_desc.json?SessionId=' + sesId + '&Id=901') as response:
        ptResp = json.loads(response.read().decode("utf-8"))
        print('ptResp')
        print(ptResp)
