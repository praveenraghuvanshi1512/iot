# Step-by-step: Object detection on a Fresh/New Raspberry pi 4 using TensorFlow Lite

I recently bought a Raspberry pi 4(4GB) which is an amazing board with diverse set of capabilities and features available. It's kind of a mini-computer. I wanted to leverage Raspberry pi to detect objects in a live cam. Tensorflow Lite has made is very simple to perform this. 

This is a step-by-step tutorial right from opening a new Raspberry pi 4 till a working prototype.

Tutorial is divided into 4 stages

1. Hardware and Software
2. Setup new Raspberry pi 4
3. Setup Camera
4. Deploy Image Classification Model

**Note:** 

- The Instructions are preformed on Windows 10 Machine
- Commands are in *italics* and needs to be executed on terminal

## Hardware and Software

### Hardware

- [Raspberry pi 4 (1GB, 2GB or 4GB)](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)

  <img src=".\assets\raspberrypi4.jpg" alt="Raspberry pi 4" style="zoom:50%;" />

- Micro SD Card >= [8GB](https://www.amazon.in/Sandisk-Class-MicroSDHC-Memory-SDSDQM-008G-B35/dp/B001D0ROGO/ref=asc_df_B001D0ROGO/?tag=googleshopdes-21&linkCode=df0&hvadid=396988876275&hvpos=1o2&hvnetw=g&hvrand=3687353551310445927&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062010&hvtargid=pla-309497947842&psc=1&ext_vrnc=hi)

- Micros SD card Reader OR Adapter 
  - [Reader](https://www.amazon.in/SanDisk-MobileMate-microSD-Card-Reader/dp/B07G5JV2B5/ref=asc_df_B07G5JV2B5/?tag=googleshopdes-21&linkCode=df0&hvadid=397079596700&hvpos=1o1&hvnetw=g&hvrand=4300042664159472398&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062010&hvtargid=pla-564041082624&psc=1&ext_vrnc=hi)
  - [Adapter](https://www.amazon.in/Zeffcon-MicroSD-Memory-Adapter-Converter/dp/B0774VLSGM/ref=asc_df_B0774VLSGM/?tag=googleshopdes-21&linkCode=df0&hvadid=397007861728&hvpos=1o4&hvnetw=g&hvrand=15641611762920535917&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062010&hvtargid=pla-839019803235&psc=1&ext_vrnc=hi)

### Software

- [Raspian OS image](https://www.raspberrypi.org/downloads/raspbian/)
- [SD Association’s Formatting Tool](https://www.sdcard.org/downloads/formatter_4/eula_windows/)
- [OS Image burning software - Balena](https://www.balena.io/etcher/)
- [Remote access to Raspberry Pi - MobaXterm](https://mobaxterm.mobatek.net/)

## Setup new Raspberry pi 4

- **Non-Headless setup:** Follow Official setup page in case Monitor, Keyboard and mouse is present [Setup Raspberry pi - Raspberry website](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)

- **Headless Setup:** This is followed when external Monitor, Keyboard and Mouse is not present. A PC/Laptop is present. 

  - **References**: 

    - [Headless Raspberry pi ssh wifi setup](https://desertbot.io/blog/headless-raspberry-pi-4-ssh-wifi-setup)
    - [Raspberry Pi Headless Setup With WiFi and SSH Enabled](https://www.gngrninja.com/code/2019/3/10/raspberry-pi-headless-setup-with-wifi-and-ssh-enabled)

  - **PC/Laptop**

    - Raspian OS: Download from [link](https://www.raspberrypi.org/downloads/raspbian/) 

        - Raspbian Buster with desktop and recommended software
            - Size(img file) ~ 6 GB
            - Full featured, supports Remote desktop, VNC
            - Used in this tutorial
        - Raspbian Buster Lite
            - Size(img file) ~ 400 MB
            - Minimal features, no Remote desktop or VNC

    - Micro SD Card

      - Attach Micro SD card to Its reader/adapter and plug it to PC/Laptop
      - For old Micro SD card, take backup and format it using [SD Association’s Formatting Tool](https://www.sdcard.org/downloads/formatter_4/eula_windows/)
      - Micro SD card will appear as a USB drive in the PC.
      - Note down the letter of drive(E:\). Double click to open the drive

    - Burn Raspian image to Micro SD card

      - Download [Balena(Image burning software)](https://www.balena.io/etcher/)

      - Launch application: 

        - Select raspian os image (2019-09-26-raspbian-buster-full.img)
        - Select MicroSD drive(E:\)
        - Click Flash

      - In-Progress

        <img src=".\assets\balena-raspian-os-inprogress.jpg" alt="Burning os image to SD card-Balena" style="zoom:50%;" />

      - Completed

        <img src=".\assets\balena-raspian-os-completed.JPG" alt="Burning os image to SD card-Balena - Completed" style="zoom:50%;" />

        - **Failure**: In case there is a failure due to checksum error, please follow steps in below link
        - [How to prevent creation of “System Volume Information” folder in Windows 10 for USB flash drives?](https://superuser.com/questions/1199823/how-to-prevent-creation-of-system-volume-information-folder-in-windows-10-for)
          - [Checksums do not match](https://forums.balena.io/t/checksums-do-not-match/36537/48)

      - Re-insert the MicroSD card

        - A drive might have been created with name as 'boot'
      - Double click to navigate to this drive
      
    - Enable SSH for remote login
      
        - Create an empty file by name 'ssh', and put it in the root folder of SD card. No extension to file
        
      - Enable Wifi
      
        - Create a file with name 'wpa_supplicant.conf' and place it in the boot root folder
      
        - Give proper country, ssid and password
      
          ```powershell
          ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
          update_config=1
          ap_scan=1
          fast_reauth=1
          country=IN
          
          network={
              ssid="NETWORK-NAME"
              psk="NETWORK-PASSWORD"
          	id_str="0"
          	priority=100
          }
          ```

    

  - **Raspberry Pi**

    - Boot Raspberry Pi with SD card

      - Eject MicroSD card from PC
      - Connect Raspberry Pi to Router through LAN cable
      - Plug it into Raspberry Pi and wait for 2 minutes

    - Router

      - Login to router such as 192.168.1.1
      - In the device list, a device containing 'raspberry pi' should appear
      - Get the IP of the this device such as 192.168.1.11

    - Login Remotely over Wi-Fi

      - [Download](https://mobaxterm.mobatek.net/) and install MobaXterm

      - Click on session and type pi IP(192.168.1.11) in Remote Host under Basic Settings. Click ok

      - Enter username: pi and password: raspberry

        <img src=".\assets\MobaXterm-login.jpg" alt="MobaXterm Login" style="zoom: 50%;" />

    - Remote desktop vnc

      - Enter *sudo raspi-config*

        ![Raspi config home](.\assets\raspi-config-home.jpg)

      - Select Option 5: Interfacing Options

        ![Raspi config - VNC](.\assets\raspi-config-vnc.jpg)

      - Select P3-VNC and Press Yes

        <img src=".\assets\raspi-config-vnc-confirm.jpg" alt="Raspi-config-VNC-confirm" style="zoom:50%;" />

      - Pres Y to continue

        ![Raspi-VNC-Confirm-2](.\assets\raspi-config-vnc-confirm-2.jpg)

      - Enter *sudo reboot now* to reboot in order the settings to take into effect

      - Now start VNC and enter the IP of raspberry pi. It should display the Raspberry pi desktop.

        <img src=".\assets\vnc-desktop.jpg" alt="VNC-desktop" style="zoom:50%;" />

        - In case black screen with message 'Cannot currently show the desktop' is displayed, follow below steps

          ![VNC-Desktop-Error](.\assets\vnc-desktop-error.jpg)

          - Connect raspberry pi through SSH
          - Enter *sudo raspi-config*
          - Select 7 - Advanced Operations
          - Select 5 - Resolution
          - Select last option and press OK
          - Restart Raspberry pi
          - Start VNC and desktop will be displayed

      - **[Optional] Installing On-screen keyboard**

        - [Matchbox Keyboard - Raspberry Pi Touchscreen Keyboard](https://thepihut.com/blogs/raspberry-pi-tutorials/matchbox-keyboard-raspberry-pi-touchscreen-keyboard)

          - *sudo apt-get install matchbox-keyboard*

          - Enter *sudo matchbox-keyboard* to open keyboard

          - Launch keyboard through double click
      
            - Create a file on the Desktop 'keyboard.sh'

            - Write below statement in the file 

              ```bash
          #!/bin/bash
              matchbox-keyboard
              ```
      
        - Open terminal and enter below commands
      
          - *cd Desktop*
              - *chmod +x keyboard.sh*

            - Double click to launch keyboard

      - **[Optional] Setting Static IP**

        - Reference
      
          - [How to Set Static IP for Raspberry Pi in Raspbian Jessie](https://www.youtube.com/watch?v=dfZlMvzQVsI)
          - [2016: Assign a Static IP Address to Raspberry Pi](https://www.youtube.com/watch?v=D1eD60_jhKI)
          - [Raspberry Pi - Tutorial 12 - Networking - How to Configure a Static IP Address & Setup Wifi](https://www.youtube.com/watch?v=D-s8Uj0uZoA)
      
        - Execute *ifconfig* and note down the IP address (inet)
      
          <img src=".\assets\ifconfig.jpg" alt="ifconfig" style="zoom: 67%;" />
      
        - Execute *netstat -nr* . Note down Gateway IP : 192.168.1.1, it will be used to set static_routers
      
        <img src=".\assets\netstat.jpg" alt="netstat" style="zoom: 67%;" />
      
        - Execute *sudo nano /etc/dhcpcd.conf*. File will be opened in edit mode. Add top four lines at the beginning of file. Ctrl+X and Y to save the file.
      
        ![image-20200112181004304](.\assets\dhcpconfig.jpg)
      
        
      
        - Execute *sudo reboot* to reboot Raspberry Pi
      
        - Execute *ifconfig* and check the inet address, it must be the one given above.
    
  - References

    - https://magpi.raspberrypi.org/articles/set-up-raspberry-pi-4
    - https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
    - https://www.instructables.com/id/How-to-Setup-a-Raspberry-Pi/

- **Setup Camera**
	
	- Reference: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
		
	- Enable Camera 
	
	  - Open Raspberry Pi Configuration
	
	  - Go to 'Interfaces' tab and select Camera 'Enabled'
	
	    <img src=".\assets\camera-enable.jpg" alt="Camera-enable" style="zoom: 50%;" />
	
	  - Reboot *sudo reboot now*
	
	  - Attach camera to Raspberry pi 
	
	  - Enter *raspistill -o Desktop/image.jpg* to take an image from raspberry pi. It gets saved on Desktop
	
	  - Check image
	
- **Deploy image classification model** 
	
	- Reference: [Part 2 - How to Run TensorFlow Lite Object Detection Models on the Raspberry Pi (with Optional Coral USB Accelerator)](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md#step-1e-run-the-tensorflow-lite-model)
		
	- TensorFlow Lite	
	  - Followed step by step instructions in the tutorial and it worked without any issue. Summarized steps/commands. 
	
	    1. *sudo apt-get update*
	
	    2. *sudo apt-get dist-upgrade* (Time consuming)
	    3. Download code from github
	       1. *git clone https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi.git*
	       2. Move code to tflite1 directory *mv TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi tflite1*
	       3. Change directory *cd tflite1*
	    4. Create Virtual Environment for isolation
	       1. Install virtual environment *sudo pip3 install virtualenv*
	       2. Create virtual environment *source tflite1-env/bin/activate*
	    5. Install dependencies *bash get_pi_requirements.sh*
	    6. Google's sample TFLite model
	       1. Download *wget https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip*
	       2. Unzip *unzip coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip -d Sample_TFLite_model*
	    7. Run model to start webcam and start making predictions
	       1. *python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model*
	    8. Awesome!!! 
	
	  
	
	  ## References
	
	  - [How to Set Static IP for Raspberry Pi in Raspbian Jessie](https://www.youtube.com/watch?v=dfZlMvzQVsI)
	  - [2016: Assign a Static IP Address to Raspberry Pi](https://www.youtube.com/watch?v=D1eD60_jhKI)
	  - [Raspberry Pi - Tutorial 12 - Networking - How to Configure a Static IP Address & Setup Wifi](https://www.youtube.com/watch?v=D-s8Uj0uZoA)
	  - https://magpi.raspberrypi.org/articles/set-up-raspberry-pi-4
	  - https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up
	  - https://www.instructables.com/id/How-to-Setup-a-Raspberry-Pi/
	  - https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
	  - https://www.youtube.com/watch?v=aimSGOAUI8Y
	  - https://www.techrepublic.com/article/raspberry-pi-and-machine-learning-how-to-get-started/
	  - https://www.youtube.com/watch?v=npZ-8Nj1YwY
	  - https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md#step-1e-run-the-tensorflow-lite-model
	  - https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Raspberry_Pi_Guide.md
	  - https://www.pyimagesearch.com/2017/10/02/deep-learning-on-the-raspberry-pi-with-opencv/
	  - https://www.pyimagesearch.com/2017/10/16/raspberry-pi-deep-learning-object-detection-with-opencv/
	  - [Matchbox Keyboard - Raspberry Pi Touchscreen Keyboard](https://thepihut.com/blogs/raspberry-pi-tutorials/matchbox-keyboard-raspberry-pi-touchscreen-keyboard)
