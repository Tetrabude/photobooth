# README #

# Prevent GPHOTO2 from automount in GUI '

sudo rm /usr/share/dbus-1/services/org.gtk.Private.GPhoto2VolumeMonitor.service

sudo rm /usr/share/gvfs/mounts/gphoto2.mount

sudo rm /usr/share/gvfs/remote-volume-monitors/gphoto2.monitor

sudo rm /usr/lib/gvfs/gvfs-gphoto2-volume-monitor

http://www.instructables.com/id/Raspberry-Pi-photo-booth-controller/step2/Connect-the-Camera/
