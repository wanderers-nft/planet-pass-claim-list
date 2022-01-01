import json

def main():
    wandies = json.load(open("output.json"))
    wallets = set()

    for id, addr in wandies.items():
        wallets.add(addr)
    
    for w in wallets:
        print(f"{w},0.16")

if __name__ == "__main__":
    main()