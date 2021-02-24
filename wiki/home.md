# Welcome to the RoboCop wiki!

This is our RoboCop control handbook. Your guide for controlling your own robotic hand.

### What is this?
The documentation for all aspects of the robotic hand project.

### Aha?
Our goal was to control a robotic hand via custom GUI . The mechanical part of the hand already existed. It was the result of another project. We exchanged the custom controller board with a raspberry pi and created a whole new interface.  

### Cool! Can I have that as well?
Of course. And really easy as well. But let us start at the beginning.

***

#### Giving life to the brain of the arm
Plug in the raspberry pi. It is that simple. It will take some time to fully come alive, so feel free to grab a coffe. The next thing we do is opening the GUI. You can even find it in this repository. Simply run `python ui/window.py` in the gits root directory. If it is your first time, a small configuration window will open. Here you should enter the local ip of the brain. To find out how to get it, please have a look [here](https://techtutorialsx.com/2018/05/20/raspberry-pi-3-getting-the-local-ip-address/). The default port used is 1880. If you have not yet messed with the project, You do not need to change it. Otherwise you probably know which port you set it to. The one that the raspberry pi's local node-red server is running on. Oh you want to change it? [No problem](https://nodered.org/docs/user-guide/runtime/configuration). Once you save the configuration, it will open the main GUI. Pretty cool, right? Now you can start moving fingers and making gestures.
#### But nothing is moving
In this case, you still need to bring life to the actual arm itself. Make sure to connect the servos to the raspberry pi according to information which can be found [here](https://drive.google.com/open?id=1l4bHcu0i-FVxMpR3WdEWjgROLYo4Tq5s), or in the git directory. If this info does not help you, please ask someone familiar with electronics. Because making errors here can result in damaging the hardware. Once this is done, we are good to go. Move fingers as you please and save current finger extensions as gestures.

***

## So. Many. Questions...
[Am I even connected to same local area network?](#am-i-even-connected-to-the-same-local-area-network)  
[What is my raspberry pis ip?](#what-is-my-raspberry-pis-id)  
[Why is the UI not starting?](#why-is-the-ui-not-starting)   
[How is all this working?](#how-is-all-of-this-working)  
[Can I change things?](#can-i-change-things)  

### Am I even connected to the same local area network?
I can not really help you with that one. But have a look [here](https://superuser.com/questions/866720/how-do-i-know-if-two-machines-are-on-same-lan).

### What is my raspberry pis ip?  
This is something you need to find out yourself. Luckily other smart people have already created a lot of guides for exactly this topic. Have a look at [this one](https://techtutorialsx.com/2018/05/20/raspberry-pi-3-getting-the-local-ip-address/) for example.

### Why is the UI not starting?
The UI is created in [python3](https://www.python.org) using the [kivy package](https://kivy.org/#home). Make sure you have those installed first.

### How is all this working?
To make this project happen, there are several parts involved. to understand them, let us track what happens when you interact with the GUI. When moving a slider in the GUI, it reads its values and passes them to our python API package. This converts the signal into a HTTP request and sends it to the ip and port specified by its config.json. the raspberry pi is running a locally hosted node-red server. It listens for incoming HTTP request. Once received, it processes it to PWN signals for the raspberry pi. These send a current to the servos in the arm and make them move. This is all a bit vague, so lets look at the components a bit closer. Starting with the

#### GUI
The GUI is written in python using the kivy package. The layout of the window is defined in the `layout.kv` file. The python script actually making things happen is called `window.py`. Both those files can be found in the `ui` subdirectory. Saving and loading gestures is managed by this script as well. Gestures are saved in the `gestures.json` file. When a gesture is selected or a slider is moved, it makes use of the 

#### API package
The APIpackage is created as a wrapper for the possible HTTP requests. It takes finger extension amounts and its configuration to turn them into requests using the requests module. It comes with a small tkinter based UI for changing ip and port in the configuration. This window can be launched at any time by running the `config.py` file. It is also run when opening the GUI for the first time, or pressing its config button. If your goal is to create a new application which determines how much fingers should be moved, but do not want to touch the raspberry pi and how it works, you can also make use of this package. Sent HTTP requests will be received by

#### Node-RED
Node-RED runs as a locally hosted server on the raspberry pi. It launches itself on startup. By default it listens to port 1880. This can be changed as needed. Refer to the NODE-RED documentation for this. There are two flows defined in Node-RED. They is a backup for both of them in the node-red subdirectory. The API flow listens for incoming http requests and, if the parameters match, converts them to pwn signals. this is achieved with a function node. A backup for the function run inside this node can be found in the `node_red_function.js`.
The Debug flow renders a webpage with sliders for the fingers as well. This can be used to quickly test the hands inner workings. For example if you want to change servos. It is also good for finding maximum and minimum values for the pwn signal to not stress the motors too much. In the node-red function, these values can be set individually for each finger. It is advised to only ever have one flow active to not have conflicting signals.

#### Can I change things?
Of course. Everything we use to make this work can be found in this git. and therefore you can change anything you like. Have fun :)