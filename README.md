# waterbot
code for controlling a Raspberry-Pi-controlled boat

Starting with a Raspberry Pi with a camera and a pan/tilt mechanism (see 
https://learn.sparkfun.com/tutorials/setting-up-the-pi-zero-wireless-pan-tilt-camera/all )

I added an L293D dual H-bridge controlling a reversible propulsion motor and a rudder toggle (electrically identical to a reversible motor) for a small plastic boat, which the Rasperry Pi 
could then control.  I added buttons to the pan/tilt camera control page to control the propulsion and steering of the boat,
making the basis for a "first person" remote piloted watercraft.   

The code for all this ends up in the root of /var/www/[whatever location your pan/tilt camera ended up in, often 'html'].

To do:  make the rudder and propulsion systems proportional with slider UI interfaces and PWM.
