from src.model import compute_total
from src.repository import get_data
from src.view import display_result


def main():
    data = get_data()
    total = compute_total(data)
    display_result(total)


if __name__ == '__main__':
    main()
