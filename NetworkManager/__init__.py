try:
    from NetworkManagerDbus import DbusNetworkChecker  as NetworkChecker
except expression as identifier:
    pass

try:
    from NetworkManagerHelperWin32 import Win32NetworkChecker  as NetworkChecker
except expression as identifier:
    pass

#from NetworkManagerHelperGio import GioNetworkChecker as NetworkChecker 