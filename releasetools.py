# Maintainer Note
# @xLexip 2021

def FullOTA_Assertions(info):
    OTA_MaintainerSection(info)
    return

def IncrementalOTA_Assertions(info):
    OTA_MaintainerSection(info)
    return

def OTA_MaintainerSection(info):
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("     __  ");')  
    info.script.AppendExtra('ui_print("    / /  ");')
    info.script.AppendExtra('ui_print("   / /   ");')
    info.script.AppendExtra('ui_print("  / /___ ");')
    info.script.AppendExtra('ui_print("  \____/ ");')
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("Pixel Exeprience 11+ // OnePlus 5 Series");')
    info.script.AppendExtra('ui_print("Maintained by xLexip");')
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("Get help and important information on Telegram");')
    info.script.AppendExtra('ui_print("Channel: t.me/lexipc");')
    info.script.AppendExtra('ui_print("Group:   t.me/lexipg");')
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("Source Code");')
    info.script.AppendExtra('ui_print("github.com/xlexip/pe");')
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("Have fun with Pixel Experience! :]");')
    info.script.AppendExtra('ui_print("                                             -");')
