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
    info.script.AppendExtra('ui_print("Pixel Experience 11+ // OnePlus 5 Series");')
    info.script.AppendExtra('ui_print("Maintained by xLexip");')
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("For support and further information,");')
    info.script.AppendExtra('ui_print("visit: lexip.dev/pe");')
    info.script.AppendExtra('ui_print("                                             -");')
    info.script.AppendExtra('ui_print("Enjoy Pixel Experience! :]");')
