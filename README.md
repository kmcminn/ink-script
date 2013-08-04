ink-script
==========

## Notes
* Didn't see ad graphite web interface running on this box so I couldn't test this end to end
* I'm just hacking through these
* If I was implementing this in real world I would be doing something with testing and a battle proven file observer library. 
* I am mid thought whether its a good idea to keep state on tailed files or not. Pro for state is sending the whole file when you start a program.
* Didn't test these a whole lot, esp the bash one. Python one should work.

## grab-stats.sh
Quick dirty few lines of bash to do the job. The c tail implementation is fairly robust but yeah, this is a hack. I thought about initially sending this over and then decided to do something a little nicer in python.

## grab-stats.py
Saw the tail pattern using a generator mentioned in some slides from a pycon. It feels fairly pythonic to me.

The carbon message construction needs to be broken out into its own function as well as use a better way to match someting like status codes to a graph key. Typically you use a dictionary in python when you need a switch statement but yeah this is just a fizbuzz so I tossed the dry bits to the side. 

I could have made this a fancy python script with argparse too but I think this'll do. :)

Night guys!
