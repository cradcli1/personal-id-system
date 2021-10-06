const express = require( "express" );
const app = express();
const port = 8080; // default port to listen

// start the Express server
app.listen( port, () => {
    console.log( `server started at http://localhost:${ port }` );
} );

// define a route handler for the default home page
app.get( "/", ( req, res ) => {
    res.send( "Hello world!" );
});

app.get("/networks/mock/clients", (req, res) => {
    var response = [
        {
            "usage": { "sent": 138, "recv": 61 },
            "id": "k74272e",
            "description": "Christopher's phone",
            "mac": "11:22:33:44:55:66",
            "ip": "1.2.3.4",
            "user": "cradcli1",
            "vlan": 255,
            "switchport": null,
            "ip6": "",
            "firstSeen": Math.round(Date.now() / 1000) - 100,
            "lastSeen": Math.round(Date.now() / 1000),
            "manufacturer": "Apple",
            "os": "iOS",
            "recentDeviceSerial": "Q234-ABCD-5678",
            "recentDeviceName": "My AP",
            "recentDeviceMac": "00:11:22:33:44:55",
            "ssid": "My SSID",
            "status": "Online",
            "notes": "My client note",
            "ip6Local": "fe80:0:0:0:1430:aac1:6826:75ab",
            "smInstalled": true,
            "groupPolicy8021x": "Student_Access"
        },
        {
            "usage": { "sent": 138, "recv": 61 },
            "id": "e53624x",
            "description": "Miles's phone",
            "mac": "22:33:44:55:66:77",
            "ip": "1.2.3.4",
            "user": "milesmeraki",
            "vlan": 255,
            "switchport": null,
            "ip6": "",
            "firstSeen": Math.round(Date.now() / 1000) - 3000,
            "lastSeen": Math.round(Date.now() / 1000),
            "manufacturer": "Apple",
            "os": "iOS",
            "recentDeviceSerial": "Q234-ABCD-5678",
            "recentDeviceName": "My AP",
            "recentDeviceMac": "00:11:22:33:44:55",
            "ssid": "My SSID",
            "status": "Online",
            "notes": "My client note",
            "ip6Local": "fe80:0:0:0:1430:aac1:6826:75ab",
            "smInstalled": true,
            "groupPolicy8021x": "Student_Access"
        },
        {
            "usage": { "sent": 138, "recv": 61 },
            "id": "g5d2734",
            "description": "John's phone",
            "mac": "33:44:55:66:77:88",
            "ip": "1.2.3.4",
            "user": "jsnow",
            "vlan": 255,
            "switchport": null,
            "ip6": "",
            "firstSeen": Math.round(Date.now() / 1000) - 3600,
            "lastSeen": Math.round(Date.now() / 1000),
            "manufacturer": "Apple",
            "os": "iOS",
            "recentDeviceSerial": "Q234-ABCD-5678",
            "recentDeviceName": "My AP",
            "recentDeviceMac": "00:11:22:33:44:55",
            "ssid": "My SSID",
            "status": "Online",
            "notes": "My client note",
            "ip6Local": "fe80:0:0:0:1430:aac1:6826:75ab",
            "smInstalled": true,
            "groupPolicy8021x": "Student_Access"
        }
    ]
    res.json(response);
});