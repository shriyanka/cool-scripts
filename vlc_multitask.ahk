'''
Dividing the screen in two halfs one for vlc media and other any other application.
The two screens are fixed and can be multitasked simultaneously.
'''

#v::
IfWinExist ahk_pid %PID%
{
	WinGet active_pid,PID
    WinActivate ahk_pid %PID%
    WinWait ahk_pid %PID%    
    WinMove,,,A_ScreenWidth/2,0,A_ScreenWidth/2,A_ScreenHeight-40
    ;MsgBox The newly launched VLC PID is %PID%
}
else
{
	Run C:\Program Files\VideoLAN\VLC\vlc.exe,,,PID
    WinActivate
    WinMove,,,A_ScreenWidth/2+15,0,A_ScreenWidth/2,A_ScreenHeight-40
    ;MsgBox The newly launched VLC PID is %PID%
}
return
#a::
WinGet, id, list,,, Program Manager
Loop, %id%
{
    this_id := id%A_Index%
    WinGetClass, this_class, ahk_id %this_id% 
    if(this_class=="TkTopLevel" or this_class=="AcrobatSDIWindow" or this_class=="PX_WINDOW_CLASS" or this_class=="MozillaWindowClass" or this_class=="ConsoleWindowClass" or this_class=="CabinetWClass" or this_class=="HH Parent" or this_class=="Notepad")
    {
    WinActivate, ahk_id %this_id%
    WinWait, ahk_id %this_id%
    WinMove,,,0,0,A_ScreenWidth/2,A_ScreenHeight-40
    }
}
return 
