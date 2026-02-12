from services.crypto_service import get_bitcoin_price


def main():
    price = get_bitcoin_price()

    if price:
        print(f"Bitcoin price: ${price}")
        print("Request successful!")
    else:
        print("Failed to retrieve Bitcoin price.")


if __name__ == "__main__":
    main()
