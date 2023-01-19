import wget, os
from urllib.error import HTTPError


base_url = 'https://distrowatch.com/images/yvzhuwbpy/howtux.png'
image_names = ["SL4P", "Slackel", "Slackintosh", "Slackware", "Slackware ARM", "Slamd64", "SLAMPP", "Slax", "SlaXBMC", "SLED", "SLES", "SliTaz", "SLS", "SME Server", "SmoothWall Express", "SmoothWall GPL", "SMS", "Sn0wL1nuX", "Snowlinux", "SolusOS", "Sorcerer", "SOT", "Source Mage", "Specifix", "SprezzOS", "srvRX live", "Stampede", "StartCom", "StartOS", "Stux", "STUX", "Sun JDS", "Superb Mini Server", "SuperRescue", "SuSE", "SUSE", "Sword OS", "Syllable", "Syllable Server", "Symphony OS", "Synergy", "SystemRescueCD", "T2", "Tails", "TAMU", "Tango Studio", "Tao", "TEENpup", "ThinClientOS", "Thinstation", "Tinfoil Hat", "Tiny", "Tiny Core", "Tiny SliTaz", "TinyMe", "Tirwal", "Tizen", "tomsrtbt", "Toorox", "Topologilinux", "TorBOX", "Trans-Ameritech", "Trisquel", "trixbox", "Trustix", "Tuquito", "Turbolinux", "U-lite", "Uberyl", "Ubuntu eee", "Ubuntu Rescue Remix", "Ubuntu Studio", "Ubuntulite", "UHU", "Ultimate Edition", "UltraPenguin", "Underground Desktop", "Unifix", "United Linux", "Unity", "Ututo", "Ututo XS", "Ututo-e", "VectorLinux", "VENENUX", "Vibuntu", "VidaLinux", "Vine", "VINUX", "Viperr", "Virtual", "Vixta", "VLOS", "Voltalinux", "VortexBox", "Voyage", "Vulnix", "Vyatta", "wattOS", "Weaver", "Webconverger", "webOS", "WGS Linux Pro", "WHAX", "White Box", "Whonix", "Wifislax", "Wifiway", "Wolvix", "Xamin", "Xange", "XBMC Live", "Xdenu", "Xebian", "Xinutop", "Yellow Dog", "Yggdrasil", "Ylmf", "Yoper", "YunoHost", "Zebuntu", "ZENIX", "Zenix OS", "Zentyal", "Zenwalk", "Zeroshell", "ZevenOS", "Zorin OS"]
for image_name in image_names:
  print("\n"+ image_name)

  try:
    if ( not (os.path.isfile(image_name+".png") )):
      wget.download(base_url + image_name.lower()+".png", out = image_name+".png")
  except HTTPError:
    print("\nError: "+ image_name)
    pass



