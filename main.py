from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card


def main():
    card_number = "7000792289606361"
    masked_card_number = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card_number}")

    account_number = "73654108430135874305"
    masked_account_number = get_mask_account(account_number)
    print(f"Маскированный номер счета: {masked_account_number}")

    cards = [
        "Visa Platinum 7000792289606361",
        "Maestro 7000792289606361",
        "Счет 73654108430135874305"
    ]

    for card in cards:
        masked = mask_account_card(card)
        print(masked)

    date_str = "2024-03-11T02:26:18.671407"
    formatted_date = get_date(date_str)
    print(formatted_date)


if __name__ == "__main__":
    main()

