Set WshShell = WScript.CreateObject("WScript.Shell")
WScript.Sleep 5000
WshShell.Run "cmd /K cd C:\Users\Me\Documents\POS_OTC\ngposotc-backend-x64" 
WScript.Sleep 500
WshShell.SendKeys "ngposotc-backend-x64.exe"
WScript.Sleep 500
WshShell.SendKeys "{ENTER}"
WScript.Sleep 500
