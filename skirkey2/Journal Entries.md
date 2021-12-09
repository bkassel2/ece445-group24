# Meeting 9/9/21 With Professor Kwiat
The team met with Professor Kwiat over a Zoom call which was around an hour in length, and wherein he illuminated his vision for the final product and explained basic principles of quantum entanglement and its practicality as it relates to computer cryptography.

<img src="9-9_Kwiat_Drawing.PNG" width = "900"/>

# Meeting 9/11/21 With Professor Kwiat
The team once again met with Professor Kwiat with the aim of discussing the budget-quality balance of the project, and to what extent the physics depatment may be able to subsidize the project in order to produce a higher quality product. All the while keeping in mind the end goal of holding a public educational display in Loomis Laboratory.

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

# 10-28-2021 - First Day in the Lab
Picked up parts from the business office and began initial work on the project build. I began soldering the microcontroller onto the PCB while Andrew and Ben loaded the OS onto the Raspberry Pi and began testing out the LED strips with their provided integrated controller modules. Also burned out one of our LED strips.

# 11-2-2021 - Finishing up Soldering Microcontroller and Testing LEDs
I finished soldering the microcontroller to the PCB and began soldering the ISP programming header to the PCB along with its diode to prevent reverse power flow. Andrew and Ben used the Raspberry Pi to control an LED strip, animating it in a way specified to us by our sponsor.

# 11-3-2021 - Setting up the Arduino IDE for our Microcontroller
Ben and I went into the lab and set up the Arduino IDE on a lab computer in order to program our microcontroller, however we realized that we needed access to a USBasp programmer, which we could not get because there was not a TA in the lab with us.

# 11-7-2021 - Testing Two LED strips and Capacitive Touch Breakout Boards
Andrew and I went into the lab and tested out our ability to animate two LED strips at a time with the Raspberry Pi, which was successful. I soldered header pins onto the capacitive touch boards so that we could test them with the AdaFruit provided libraries on the Raspberry Pi. We were able to get two capacitive touch boards to be recognized independently on the same I2C bus, and we also found that the touch lines are only reliable up to around 4 feet in length. Additionally, Andrew got some code working which stopped the LED animation when one of the capacitive touch boards registered a touch.

# 11-9-2021 - Ordered a PS/2 Keyboard from Amazon
Ordered a miniature PS/2 keyboard from Amazon in order to test with the microcontroller.

# 11-11-2021 - Reinstalling Raspberry Pi OS and Soldering
Andrew and I went into the lab and Andrew did a fresh install of the Raspberry Pi OS and redownloaded the coding libraries since it had crashed earlier this week, and I soldered wires to the touch sensing input lines of one of the capacitive touch breakout boards, and after some testing realized that we had not picked the best wire since it was too rigid, and the touch sensing also became inconsistent.

# 11-12-2021 - Soldering on Crystal Oscillator and Programming Microcontroller
Ben and Andrew found out earlier in the week that we needed an oscillator in order to program the microcontroller, and had ordered one, which came in today. All of us went into the lab and I soldered the oscillator to the PCB and we were able to successfully program the microcontroller and get it to blink a single LED.

# 11-14-2021 - Soldering Touch Boards and Coding
All of us went into the lab and I soldered touch lines to two additional capacitive touch breakout boards while Andrew and Ben wrote some code to handle LED animations in reaction to touches from the breakout boards.

# 11-16-2021 - Capacitive Touch Breakthrough
We all went into the lab and after much testing, we found that if we soldered copper tape to the ends of the touch sensing lines from the breakout boards instead of having just the stripped end of a wire to touch, that the erratic behavior of the touch sensing boards was completely eradicated.

# 11-17-2021 - Preparing for the Mock Demo
We all went into the lab and I soldered copper strips to all of the ends of the touch sensing lines for two capacitive touch breakout boards (24 lines total). We then set up two strips of cardboard each with an LED strip and a capacitive touch board, where the copper strips were aligned parallel with the LED strip to act as a mock-up of our final product so that we could test our LED animation code combined with our capacitive touch code, which worked just as we intended to achieve our sponsors vision for the project.

# 11-20-2021 - Working on PS/2 keyboard as Input for the Microcontroller 
Andrew and I went into the lab and I soldered PS/2 headers onto the PCB and we both looked for libraries which supported PS/2 keyboards on our microcontroller with little luck. After finding a library, we loaded some code onto the microcontroller and plugged the keyboard into the PCB. The code was set to blink an LED when a certain key had been pressed. However, it seemed that the microcontroller could not recognize the keyboard, and after hours of combing through header files and online forums, we gave up for the day.

# 11-21-2021 - Getting Capacitive Touch and LED Strips to Work on Microcontroller
Andrew and I went into the lab and found some libraries for the microcontroller which supported our LED strips and our capacitive touch boards. Andrew was able to write some code to fuse the two libraries while I connected an LED strip and a capacitive touch board to the microcontroller. We then uploaded the code to the microcontroller and were able to animate the LEDs as well as detect touches from the breakout boards using only the microcontroller.

# 11-22-2021 - UART Communication Between Microcontroller and Raspberry Pi
Andrew and I went into the lab and researched UART serial communication between our microcontroller and the Raspberry Pi. Andrew was able to write some code in order to send data serially from the microcontroller to the Raspberry Pi, and it worked for a short period of time. We were able to keep a serial communication stream between the two devices briefly before our software terminated unexpectedly. After hours of trying to debug the code and find online forums discussing the issue to no end, we decided to stop work for the day.

# 11-28-2021 - Shopping for Parts Locally
We all went to Home Depot and Walmart and bought two planks of wood, some plumbing tube to put the LEDs inside and some plastic containers to house the electronics, all for the construction of our final demonstration setup.

# 11-29-2021 - Building the Final Demonstration
We all went into the lab and built our final demonstration setup, and I soldered some quick connect headers onto two capacitive touch breakout boards and extended some wires to be appropriate lengths for the final demonstration layout. After building the demonstration setup, we tested the code and all of the components were working.

# 11-30-2021 - Issues with Capacitive Touch
We all went into the lab to find that our capacitive touch sensors were no longer working with the Raspberry Pi, we inspected solder joints and checked for loose connections, and after finding none we decided to test the capacitive touch with the microcontroller which ended up working, so we reinstalled the Raspberry Pi OS only to find the issue to be that the capacitive touch boards did not share a ground connection with the Raspberry Pi, which solved the issue. We are now ready for our demonstration.
