head = {
    "val":11,
    "next":{
        "val":3,
        "next":{
            "val":23,
            "next":{
                "val":7,
                "next": None
            }
        }
    }
}

print(head['next']['next']['val'])