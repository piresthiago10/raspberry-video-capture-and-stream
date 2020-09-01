# Raspberry Video Capture and Stream

https://codecalamity.com/raspberry-pi-hardware-accelerated-h264-webcam-security-camera/

instalar rtp server

curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs git
sudo npm install -g coffeescript

cd ~ 
git clone https://github.com/iizukanao/node-rtsp-rtmp-server.git --depth 1
cd node-rtsp-rtmp-server
npm install -d

sudo coffee server.coffee

Create rtsp server service

# /etc/systemd/system/rtsp_server.service
[Unit]
Description=rtsp_server
After=network.target rc-local.service
[Service]
Restart=always
WorkingDirectory=/home/pi/node-rtsp-rtmp-server
ExecStart=coffee server.coffee
[Install]
WantedBy=multi-user.target

Compile FFMPEG with Hardware Acceleration

sudo apt-get install libomxil-bellagio-dev libfreetype6-dev libmp3lame-dev checkinstall libx264-dev fonts-freefont-ttf libasound2-dev -y
cd ~
git clone https://github.com/FFmpeg/FFmpeg.git --depth 1
cd FFmpeg
sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-omx --enable-omx-rpi --enable-nonfree --enable-libfreetype --enable-libx264 --enable-libmp3lame --enable-mmal --enable-indev=alsa --enable-outdev=alsa

Real Time Encoding

Only for cameras that support h264 natively!

ffmpeg -input_format h264 -f video4linux2 -video_size 1920x1080 -framerate 30 -i /dev/video0 -c:v copy -an -f rtsp rtsp://localhost:80/live/stream