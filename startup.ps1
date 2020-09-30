$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hwinfo2influxdb.lnk")
$Shortcut.TargetPath = "$env:USERPROFILE\scoop\apps\python\current\pythonw.exe"
$Shortcut.Arguments = "$env:USERPROFILE\ghq\github.com\ebith\hwinfo2influxdb\hwinfo2influxdb.py"
$Shortcut.WorkingDirectory = "$env:USERPROFILE\ghq\github.com\ebith\hwinfo2influxdb"
$Shortcut.Save()
