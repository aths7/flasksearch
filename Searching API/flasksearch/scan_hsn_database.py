from HSNCodes2 import data
from pprint import pprint


def search_text(check):
    output = list()
    if check.isdigit():
        for item in data:
            if isinstance(item["Chapter/ Heading / Sub-heading / Tariff item"], str):
                if check in item["Chapter/ Heading / Sub-heading / Tariff item"]:
                    output.append(item)
            elif isinstance(item["Chapter/ Heading / Sub-heading / Tariff item"], int):
                if int(check) == item["Chapter/ Heading / Sub-heading / Tariff item"]:
                    output.append(item)
    else:
        for item in data:
            if check in item['Description of Goods']:
                output.append(item)

    return output


if __name__ == '__main__':
    main()
