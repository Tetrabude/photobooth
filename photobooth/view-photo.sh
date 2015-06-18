#!/bin/sh

self=`basename $0`
ARGUMENT="photos/$(date +%Y-%m-%d--%H-%M-%S)--PhotoBox.cr2" 

case "$ACTION" in
    init)
	echo "$self: INIT"
	# exit 1 # non-null exit to make gphoto2 call fail
	;;
    start)
	echo "$self: START"
	;;
    download)
	echo "$self: DOWNLOAD to $ARGUMENT"
	mv capt*.cr2 $ARGUMENT
	( cmdpid=$BASHPID; (sleep 10; killall eog) & exec eog --fullscreen $ARGUMENT  )
	;;
    stop)
	echo "$self: STOP"
	;;

    *)
	echo "$self: Unknown action: $ACTION"
	echo "=================================="
	;;
esac

exit 0
