distances = { 
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for craft, distance in distances.items():
        print(f"The Craft Name is: {craft} and the distance {distance} AU is {convert(distance)} meters")

def convert(AU):
    return AU * 14564688241

main()
