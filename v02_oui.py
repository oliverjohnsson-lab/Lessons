vendors = {
    "a4:c3:f0" : "intel",
    "3c:d9:2b" : "hewlett-packard",
    "00:1a:a1" : "cisco systems",
}

addresses = [
    "a0:ad:9f:52:03:8b",
    "28:95:29:bf:a3:9c",
]

for address in addresses:
    prefix = address [0:8]

    if prefix in vendors:
        name = vendors [prefix]
    else: 
        name = "okand tillverkare"

    print (f"{address}  ->  {name}")
