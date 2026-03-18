def gallona_litroiksi(gallonat):
    return gallonat * 3.785

def main():
    while True:
        maara = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
        if maara < 0:
            print("Lopetetaan...")
            break
        litrat = gallona_litroiksi(maara)
        print(f"{maara} gallonaa on {litrat:.2f} litraa.")

if __name__ == "__main__":
    main()