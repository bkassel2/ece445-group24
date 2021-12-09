# Andrew Situ Notebook

# 9-9-2021 - Discussion with Professor Kwiat

The Team had a meeting with our sponsered professor, Professor Kwiat, about the project to clarify some of the project. Additionally he explained how the educational device would imitate how quantum entangelment would behave in the real world through the zoom whiteboard.

<img src="9-9_Kwiat_Drawing.png" width = "600"/>

# 9-11-2021 - Team meeting for project proposal

We decided to start the project propsal and look for some parts. I was looking up the different types of sensors we could use as input for the two sections of 3 foot LEDs so that there would be inputs at every 2 inches for the prototype. Initally I was looking at already created touch capacitive switches but they were only around 3 inches each at $7 per module which would be much to expensive for the given budget. I also looked at flex sensors and resistive sensors but they had there own problems. Ian ended up finding a capacitive touch board that allowed for 12 capactive touch imputs that we would have to make ourselves out of some conductive material. 

# 9-14-2021 - Meeting with TA
Had a meeting with our TA and got feedback on our Design Document. We needed to fix the Block Diagram that Ian created since it did not include which lines where what and the fixed the coloring for data and eletric lines.

# 9-15-2021 - Finsihed the project proposal for the class
Our group met up at 6 and finished working on the project propsal that was being submitted for the class. I worked on filling out the problem and solution slide in addition to creating some visual aids for the proposal. I also helped fill out the decribtion for the subsustems and block diagram.

# 9-23-2021 - 9-30-2021 - Worked on the design document
Worked on the design documents. After going to the decoument check on 9/24 we modified some of our requirement and verficaitions. In addition we where looking for all the parts we planned on using. Planed on using a microcontroller to process 2 VGA outputs and control the LED and touch capactiors. Looked up ways a microcontroller can process some VGA output. Found some sources such as http://tinyvga.com/ , https://blog.thomaspoulet.fr/bit-banged-vga/. Looked into getting a knob so our device can have some physcial speed control. Evan one of the TAs in the course notified us that driving VGA from a microcontroller might be outside the scope of this course in an email.

# 10-3-2021 - Meeting with a TA about our microcontroller
Had a video meeting with Evan who mentioned some limiations for the touch capcactiros not working after 4 feet of wires and the fact that we should not drive VGA displays with a microcontroller. We talked about alternatives for the display output and the concerns with the touch capcactiros did not affect out intended use case. Some alternatives included using multiple microcontrollers one to process logic and two more for each monitor. We also started talking about using a raspberry pi to drive the displays while processing everything else on the microcontroller. Evan also mentioned that we should probably use ps2 keyboards since their protocal are easier to use.

# 10-5-2021 - Design document flow chart
I created a flow chart to add to our design document for how the software would run. 
PICTURE
We had the design document review with the professor and some of the TAs. We talked to the professor and where allowed to use the raspberry pi to output our display for this project.

# 10-6-2021 - 10-11-2021 - Finding parts and working on the PCB
Found a new microcontroller since we are moving to outputting the display on the raspi. We looked for one that could transmit data to the raspi and process 2 LEDs, two ps2 keyboards, and the capacitive touch breakoutboards which needed a spi and sda pin on the microcontroller. We also started working on the PCB to try and get it in for the first round of PCBs. Ended up not creating the design in time for that.

# 10-13-2021 - Finished PCB
Ian finished the first draft of our PCB and check it with a TA. He also ordered it.

# 10-15-2021 - Ordered parts
We ordered all of our parts that we decided on and messaged our sponsered professor to order the LEDs, raspberry pi and power supply.

# 10-20-2021 - Getting all the parts
I went to professor Kwiat office and grabbed all the parts that came in from Amazon. Additionally the Ian recieved the PCBs and the other parts that we have ordered has arrived in the business office.

# 10-23-2021 - Ordering other parts
Relized we forgot to order some of the resistors and other small parts for the PCB and placed the order.

# 10-27-2021 - Resubmitted design document
We modified our block diagram and tolerance analysis of the previous one since we decided to use a microcontroller to process the video output instead of the original microcontroller idea. For the tolerance analysis I added some analysis on how the copper wire would affect the capacitive touch breakout board. The final result was in line with what Evan mention where the wires stopped being reliable after 3 feet.

# 10-29-2021 - Started working with the parts



