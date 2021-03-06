# Berlin-Uhr (aka the Mengenlehreuhr)
## The Berlin Clock

This project is a simulation of the so called ["Berlin-Uhr"](https://de.wikipedia.org/wiki/Berlin-Uhr) that can be displayed on the the [Card10 Badge](https://card10.badge.events.ccc.de/).

The clock, which was included in the Guinness Book of Records and has a total height of seven metres - including the mast - was erected on 17 June 1975, initially on the central strip of the Kurfürstendamm at the corner of Uhlandstrasse as the **"first clock in the world to display time with luminous coloured fields"**.
As a tribute to its inventor [Dieter Binninger](https://de.wikipedia.org/wiki/Dieter_Binninger), it is brought to life on the [Card10 Badge](https://card10.badge.events.ccc.de/).
Releases can be found on [hatchery](https://badge.team/projects/berlin_Uhr). 

## Demo:

![demo](berlin-uhr-demo.gif)

## Functions
* fully working Berlin-Uhr simulation
* displays seconds on the outer border of the display (can be turned on/off by lower left button)
* press upper right button to display the current date in a berlin-uhr-ish style
* press lower right button to show a overlay of clock/date in arabic numbers (good for beginners to learn how to read this clock)
* Power-Management / Power-Safing
    * Automatically adjust brightness of display and the seconds LED to safe battery
    * UI renders with 1FPS

## How to read the clock

### short:

| Time Unit | explanation |
| ------------- | ------------- |
| **hours**   | Multiply the number of luminous segments from row 1 by 5 and add the result with the number of luminous segments from row 2. |
| **minutes** | Multiply the number of luminous segments from row 3 by 5 and add the result with the number of luminous segments from row 4. |
| **seconds** | The second indicator is the blinking led on top of the clock. |

### extensive:

The time is displayed in a [Positional notation](https://en.wikipedia.org/wiki/Positional_notation) to the base of 5. 
The hours and minutes are represented by illuminated segments in four horizontally arranged stripes. 
In the first, second and fourth lines there are four luminaires and in the third eleven luminaires. 
The first two lines indicate the hour with red lights, with a luminous segment in the upper strip for five hours and in the lower one for one hour. 
The current hour results from the addition of the values. Accordingly, the minutes with yellow segments in steps of five and one are displayed in the two lower lines. The lamps for 15, 30 and 45 minutes are red for better readability. 
Above the lines there is a round flashing light which is switched on or off every second.


### visit it 🙂
The original clock can be visited at [Budapester Straße 5, Berlin](https://goo.gl/maps/dWd77VB7rNrN2gyT9) (next to the entrance of the Europa Center).

<p align="center">
  <img width="400" height="800" src="picture.jpg"/>
</p>


## The Original Clock:

<img width="260px" height="380px" align="left" src="https://upload.wikimedia.org/wikipedia/commons/7/7b/Berlin_Kurf%C3%BCrstendamm_113714a.jpg"/>

<img width="260px" height="380px" align="left" src="https://upload.wikimedia.org/wikipedia/commons/1/13/Gedenktafel_Budapester_Str_45_%28Charl%29_Berlin_Uhr.jpg"/>
  
<img width="260px" height="380px" align="left" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Mengenlehreuhr.jpg/800px-Mengenlehreuhr.jpg"/>
