vendors = {
    "a0:ad:9f" : "ASUStek-COMPUTER-INC",
    "28:95:29" : "Intel-Corporate",
    "28:c1:a0" : "Apple, Inc",
}

addresses = [
    "a0:ad:9f:52:03:8b",
    "28:95:29:bf:a3:9c",
    "28:c1:a0:4b:85:f8",
]

for address in addresses:
    prefix = address [0:8]

    if prefix in vendors:
        name = vendors [prefix]
    else: 
        name = "okand tillverkare"

    print (f"{address}  ->  {name}")
