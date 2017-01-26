# Wallpaper_Changer

This program changes your desktop's background picture when executed.
It searches in the site http://wallpaperswide.com/ for pictures with the thematic tags you select.

The data.txt file is used as configuration file, but stores the links of the downloaded images as well.
The images will be stored in a folder called "images". 

###Configuration parameters in data.txt
- Thematic tags: here you write separated by commas the tags which you are interested in. The program will select randomly one of these and will search matching pictures
- Forbidden tags: here you write separated by commas the tags which you want to avoid. If a matching image is as well tagged with at least one of the forbidden tags, it will be automatically dismissed.
- Resolution: here you write the resolution you want for your wallpapers. The available resolutions are listed below 


####Available resolutions
* **Wide 16** 10960x600	1152x720	1280x800	1440x900	1680x1050	1920x1200	2560x1600 2880x1800	3840x2400	5120x3200	7680x4800	
* **Wide 5:3** 800x480	1280x768	
* **UltraWide** 21:9 2560x1080	3440x1440	5120x2160	
* **UltraWide** 24:10 3840x1600	
* **HD** 16:9 960x540	1024x576	1280x720	1366x768	1600x900	1920x1080	2048x1152 2400x1350	2560x1440	2880x1620	3554x1999	
* **UHD** 16:9 3840x2160	5120x2880	7680x4320	
* **Standard 4:3** 800x600	1024x768	1152x864	1280x960	1400x1050	1440x1080	1600x1200 1680x1260	1920x1440	2048x1536	2560x1920	2800x2100	3200x2400	4096x3072	6400x4800	
* **Standard 5:4** 1280x1024	2560x2048	3750x3000	5120x4096	
* **Standard 3:2** 1152x768	1440x960	1920x1280	2000x1333	2160x1440	2736x1824	3000x2000	
* **Smartphone 16:9** 540x960	720x1280	1080x1920	1440x2560	
* **Smartphone 5:3** 768x1280
* **Tablet 1:1** 1024x1024	1280x1280	2048x2048	
* **iPad 1/2/Mini** 768x1024	1024x768
* **Mobile VGA 4:3** 240x320	480x640	320x240	640x480
* **Mobile WVGA 5:3** 240x400	480x800	400x240	800x480
* **Mobile HVGA 3:2** 320x480	640x960	480x320	960x640
* **Mobile WXGA 16:9** 272x480	360x640	480x854	480x272
* **Mobile XGA 5:4** 176x220	220x176
* **Dual Wide 16:10** 1920x600	2304x720	2560x800	2880x900	3360x1050	3840x1200	5120x1600 7680x2400	
* **Dual Wide 5:3** 1600x480	2560x768	
* **Dual HD 16:9** 1920x540	2048x576	2560x720	3200x900	3840x1080	4096x1152	4800x1350 5120x1440	
* **Dual UHD 16:9** 7680x2160	
* **Dual Standard 4:3** 1600x600	2048x768	2304x864	2560x960	2800x1050	2880x1080	3200x1200 3360x1260	3840x1440	4096x1536	5120x1920	5600x2100	6400x2400	8192x3072	
* **Dual Standard 5:4** 2560x1024	5120x2048	7500x3000	
* **Dual Standard 3:2** 2304x768	2880x960	3840x1280	4000x1333	4320x1440	5472x1824	6000x2000	
* **Triple Wide 16:10** 3840x800	4320x900	5040x1050	5760x1200	7680x1600	8640x1800	
* **Triple Wide 5:3** 2400x480	3840x768	
* **Triple HD 16:9** 3840x720	4098x768	4800x900	5760x1080	6144x1152	7200x1350	7680x1440 8640x1620	
* **Triple Standard 4:3** 3072x768	3456x864	3840x960	4200x1050	4320x1080	4800x1200	5040x1260 5760x1440	6144x1536	7680x1920	8400x2100	9600x2400	
* **Triple Standard 5:4** 3840x1024	7680x2048	
* **Triple Standard 3:2** 3456x768	4320x960	5760x1280	6000x1333	6480x1440	8208x1824	9000x2000	
