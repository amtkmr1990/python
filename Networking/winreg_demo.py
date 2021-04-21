import winreg

m = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Skype')
try:
    i = 0
    while True:
        print(winreg.EnumKey(m, i))
        i += 1
except OSError as e:
    pass

# with winreg.OpenKey('HKEY_CURRENT_USER', r'SOFTWARE\Skype\Phone\UI') as r:
#     print(winreg.EnumKey(r))
