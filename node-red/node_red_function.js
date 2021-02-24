/*
This script is part of the RoboCop project.
It serves as backend for the robotic hand.
Incoming, http request, node-red messages
get turned into power signals for the raspberry pi.

There are three steps involved
1: Define minimum and maximum extension values
    MAKE SURE TO CHANGE VALUES SLOWLY!
    CAREFUL TO NOT OVERLOAD THE SERVOES!
    const minMaxFFingerIndex = [ minValue, maxValue ];

2: Convert query value to fingers value in min max range.
*/

const minMaxF1 = [ 8, 17 ];
const minMaxF2 = [ 6, 17 ];
const minMaxF3 = [ 9, 20 ];
const minMaxF4 = [ 9, 20 ];
const minMaxF5 = [ 8.5, 20 ];

return [
    msg,
    { payload : minMaxF1[1] - (minMaxF1[1]-minMaxF1[0]) * msg.req.query.f1 / 100  },
    { payload : minMaxF2[1] - (minMaxF2[1]-minMaxF2[0]) * msg.req.query.f2 / 100  },
    { payload : minMaxF3[1] - (minMaxF3[1]-minMaxF3[0]) * msg.req.query.f3 / 100  },
    { payload : minMaxF4[1] - (minMaxF4[1]-minMaxF4[0]) * msg.req.query.f4 / 100  },
    { payload : minMaxF5[1] - (minMaxF5[1]-minMaxF5[0]) * msg.req.query.f5 / 100  },
];
