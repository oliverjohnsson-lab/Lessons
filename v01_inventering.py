device_1 = "sw-nordvik-1"
model_1 = "ws-c3560g-48ts"
role_1 = "switch, access"

device_2 = "r-nordviks-1"
model_2 = "cisco2951"
role_2 = "router, lager 3"

device_3 = "gg-nordviks-1"
model_3 = "bredband-2"
role_3 = "router, lager 4"

print ("utrustningslista")
print ("-" * 52)

print (f"{device_1:<16} {model_1:<20}{role_1}")
print (f"{device_2:<16} {model_2:<20}{role_2}")
print (f"{device_3:<16} {model_3:<20}{role_3}")

print ("-" * 52)
print ("antal enheter: 3")
