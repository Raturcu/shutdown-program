import os 

shutdown = input("Do you want to shutdown/sleep/restart your computer?")

if shutdown == 'shutdown' :
    print("Shutdown !")
    os.system("shutdown /s /t 3600");
elif shutdown=='restart':
    print("Restart")
    os.system("shutdown -r -t 3600")
elif shutdown=="sleep":
    print("Sleep")
    os.system("powercfg -h off")
    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')