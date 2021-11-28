const express = require( "express" );
const app = express();
const port = 8081; // default port to listen

// start the Express server
app.listen( port, () => {
    console.log( `server started at http://localhost:${ port }` );
} );

// define a route handler for the default home page
app.get( "/", ( req, res ) => {
    res.send( "Hello world!" );
});

app.get("/networks/mock/clients", (req, res) => {
    var response = 
        {
            "version": "3.0",
            "secret": "supersecret",
            "type": "WiFi",
            "data": {
                "networkId": "L_000000000000000001",
                "observations": [
                    {
                    "locations": [
                       {
                            "x": "7.976651798199431",
                            "lng": 6.0957744807924485,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -32
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -54
                                },
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.6885258062410806,
                            "y": "10.576847081490314",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:21Z",
                            "lat": 60.05342983801672
                        },
                        {
                            "x": "8.013339145491448",
                            "lng": 6.095772908171716,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -52
                                },
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -32
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.6201842796909718,
                            "y": "10.697906571736747",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:35Z",
                            "lat": 60.05342922730819
                        },
                        {
                            "x": "8.591860719528196",
                            "lng": 6.095759658672512,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -34
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -51
                                },
                                {
                                    "apMac": "aa:aa:aa:44:44:44",
                                    "rssi": -45
                                },
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.5097088029182084,
                            "y": "11.404523745521399",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:46Z",
                            "lat": 60.053427800388225
                        }
                    ],
                    "ipv4": "192.168.0.251",
                    "ssid": ".interwebs",
                    "os": "iOS",
                    "clientMac": "11:22:33:44:55:66",
                    "latestRecord": {
                        "time": Math.round(Date.now() / 1000),
                        "nearestApMac": "aa:aa:aa:44:44:44",
                        "nearestApRssi": "-47"
                    },
                    "ipv6": null,
                    "manufacturer": "Apple"
                    },


                    {
                    "locations": [
                       {
                            "x": "7.976651798199431",
                            "lng": 6.0957744807924485,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -32
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -54
                                },
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.6885258062410806,
                            "y": "10.576847081490314",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:21Z",
                            "lat": 60.05342983801672
                        },
                        {
                            "x": "8.013339145491448",
                            "lng": 6.095772908171716,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -52
                                },
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -32
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.6201842796909718,
                            "y": "10.697906571736747",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:35Z",
                            "lat": 60.05342922730819
                        },
                        {
                            "x": "8.591860719528196",
                            "lng": 6.095759658672512,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -34
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -51
                                },
                                {
                                    "apMac": "aa:aa:aa:44:44:44",
                                    "rssi": -45
                                },
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.5097088029182084,
                            "y": "11.404523745521399",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:46Z",
                            "lat": 60.053427800388225
                        }
                    ],
                    "ipv4": "192.168.0.251",
                    "ssid": ".interwebs",
                    "os": "iOS",
                    "clientMac": "22:33:44:55:66:77",
                    "latestRecord": {
                        "time": Math.round(Date.now() / 1000),
                        "nearestApMac": "aa:aa:aa:44:44:44",
                        "nearestApRssi": "-47"
                    },
                    "ipv6": null,
                    "manufacturer": "Apple"
                    },

                    {
                    "locations": [
                       {
                            "x": "7.976651798199431",
                            "lng": 6.0957744807924485,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -32
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -54
                                },
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.6885258062410806,
                            "y": "10.576847081490314",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:21Z",
                            "lat": 60.05342983801672
                        },
                        {
                            "x": "8.013339145491448",
                            "lng": 6.095772908171716,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -52
                                },
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -32
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.6201842796909718,
                            "y": "10.697906571736747",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:35Z",
                            "lat": 60.05342922730819
                        },
                        {
                            "x": "8.591860719528196",
                            "lng": 6.095759658672512,
                            "floorPlanName": "3rd Floor",
                            "rssiRecords": [
                                {
                                    "apMac": "aa:aa:aa:11:11:11",
                                    "rssi": -34
                                },
                                {
                                    "apMac": "aa:aa:aa:22:22:22",
                                    "rssi": -51
                                },
                                {
                                    "apMac": "aa:aa:aa:44:44:44",
                                    "rssi": -45
                                },
                                {
                                    "apMac": "aa:aa:aa:33:33:33",
                                    "rssi": -51
                                }
                            ],
                            "variance": 1.5097088029182084,
                            "y": "11.404523745521399",
                            "nearestApTags": ["", "API-TEST", "Office", ""],
                            "floorPlanId": "g_643451796760560979",
                            "time": "2019-11-28T14:27:46Z",
                            "lat": 60.053427800388225
                        }
                    ],
                    "ipv4": "192.168.0.251",
                    "ssid": ".interwebs",
                    "os": "iOS",
                    "clientMac": "33:44:55:66:77:88",
                    "latestRecord": {
                        "time": Math.round(Date.now() / 1000),
                        "nearestApMac": "aa:aa:aa:44:44:44",
                        "nearestApRssi": "-47"
                    },
                    "ipv6": null,
                    "manufacturer": "Apple"
                    },
                ]
            }
        }
    
    res.json(response);
});