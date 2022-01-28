from structural.composite.logic import Order, Product, Packet


def main() -> None:
    butter = Product("Butter", 33.5)
    bread = Product("Bread", 18)
    grocery_packet = Packet("Grocery")
    grocery_packet.extend([bread, butter])

    varenyky = Product("Varenyky", 42)
    ice_cream = Product("Ice Cream", 80)
    frozen_products_packet = Packet("Frozen")
    frozen_products_packet.extend([varenyky, ice_cream])

    food_packet = Packet("Food")
    food_packet.extend([grocery_packet, frozen_products_packet])

    shampoo = Product("Shampoo", 55)
    hygienic_packet = Packet("Hygienic")
    hygienic_packet.append(shampoo)

    order = Order("ABC123")
    order.extend([hygienic_packet, food_packet])

    print(f"Order ID '{order.order_id}' cost ${order.sum}")


if __name__ == "__main__":
    main()