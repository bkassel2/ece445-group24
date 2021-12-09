# 9-9-2021 - Meeting With Professor Kwiat
The team met with Professor Kwiat over a Zoom call which was around an hour in length, and wherein he illuminated his vision for the final product and explained basic principles of quantum entanglement and its practicality as it relates to computer cryptography.

<img src="9-9_Kwiat_Drawing.PNG" width = "900"/>

# 9-11-2021 - Meeting With Professor Kwiat
The team once again met with Professor Kwiat with the aim of discussing the budget-quality balance of the project, and to what extent the physics depatment may be able to subsidize the project in order to produce a higher quality product. All the while keeping in mind the end goal of holding a public educational display in Loomis Laboratory.

# 9-14-2021 - Meeting with TA
Met with our TA and she gave us feedback on our project proposal. I modified our block diagram in accordance with her suggestions.

# 9-15-2021 - Finished Project Proposal
We all met in a voice chat and finished our project proposal. I worked mostly on the details of the subsystem overview which described the block diagram that I also created.

# 9-23-2021 - 9-30-2021 - Design Document Progress
We all worked on our design document in a voice chat. We modified our document in accordance with the advice given during our DDC. We also looked for some parts for our PCB and researched some ways of controlling a VGA display from a microcontroller. One TA informed us via email that VGA from a microcontroller was likely outside of the scope of the class.

# 10-3-2021 - TA Meeting on Microcontrollers
We all met with Evan in a video conference during which he informed us that our options for operating VGA displays were either to use multiple microcontrollers where a single microcontroller was dedicated to each display, and a separate microcontroller for the rest of our project, or to use a Raspberry Pi to drive the displays and a single microcontroller for the rest of our project. He also told us that it may be easier to opt for the use of PS/2 keyboards as opposed to USB ones, and that we may struggle to get capacitive touch sensors work at transmission distances over four feet. 

# 10-5-2021 - Design Document Review
We all attended our design document review and talked with TAs and Professors about the use of a Raspberry Pi for the display aspect of our project, which they informed us would be a reasonable design choice.

# 10-6-2021 - 10-11-2021 - PCB Design and Parts Search
I worked on completing the PCB design and decided on the microcontroller which we will use, the ATMega328P-PU because of its in-depth documentation, and ability to interface with the Arduino IDE. I was not able to finish the PCB design in time for the first round of orders.

# 10-13-2021 - Finished PCB
I met with a TA and he gave me some advice for the PCB design and approved of it after some small modifications. I then ordered the PCB through PCBWay with an estimated delivery time of five days.

# 10-15-2021 - Ordered Parts
We filled out order forms for all of our parts including the microcontroller, capacitive touch boards, PS/2 sockets, knob, and copper tape, and also emailed our sponsor a list of some parts to order from Amazon such as a power supply, a Raspberry Pi starter kit, and some high-density LED strips.

# 10-20-2021 - Getting all the Parts
Andrew picked up the parts from our sponsor, I received the PCBs, and we got notice that our parts arrived to the business office.

# 10-23-2021 - Ordering More Parts
We noticed that we needed some additional surface mount components for the PCB such as resistors and capacitors, and filled out order forms for them.

# 10-27-2021 - Design Document Resubmission
I modified the block diagram to reflect our new design plan which included the Raspberry Pi to drive the LED displays, and UART communication from the microcontroller to the Raspberry Pi. Andrew added a section to the tolerance analysis outlining the effects of transmission distance on the accuracy of capacitive touch sensors.

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

# 11-30-2021 - Finished Building Final Demonstration
We all went into the lab to find that our capacitive touch sensors were no longer working with the Raspberry Pi, we inspected solder joints and checked for loose connections, and after finding none we decided to test the capacitive touch with the microcontroller which ended up working, so we reinstalled the Raspberry Pi OS only to find the issue to be that the capacitive touch boards did not share a ground connection with the Raspberry Pi, which solved the issue. We are now ready for our demonstration.
