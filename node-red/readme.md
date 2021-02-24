### Node-RED
Here you can find our backup for all the files required on the raspberry pi. Its local Node-RED server is running two flows. One for processing api request. It can be found in `api_flow.json`. The other is our arms debuggng interface. It is found in `debug_flow.json`. To import a flow from json in Node-RED, look [here](https://nodered.org/docs/user-guide/editor/workspace/import-export). `node_red_function.js` is a backup for the JavaScript function running inside the function node of the API flow.

### Requirements
 - Node-RED versionNumber

### Notes
Only ever deploy one flow in Node-REd. The other should be set to inactive. Otherwise you risk conflicting inputs for the servoes.