# Client interface
class ShippingSystem:
    def calculate_shipping_cost(self, weight):
        pass

# Service class
class ThirdPartyShippingService:
    def calculate_cost_by_weight(self, weight_in_kg):
        return weight_in_kg * 2.5 

# Adapter class
class ShippingAdapter(ShippingSystem):
    def __init__(self, third_party_service):
        self.third_party_service = third_party_service

    def calculate_shipping_cost(self, weight):
        weight_in_kg = weight * 0.453592  # Convert pounds to kilograms
        cost = self.third_party_service.calculate_cost_by_weight(weight_in_kg)
        return f"Shipping cost using third-party service: ${cost:.2f}"

# Client class
class ShoppingCart:
    def __init__(self, weight):
        self.weight = weight

    def calculate_shipping_cost(self, shipping_system):
        return shipping_system.calculate_shipping_cost(self.weight)

# Example usage
if __name__ == "__main__":
    third_party_service = ThirdPartyShippingService()

    shipping_adapter = ShippingAdapter(third_party_service)

    shopping_cart = ShoppingCart(weight=10)  # Weight in pounds
    result = shopping_cart.calculate_shipping_cost(shipping_adapter)

    print(result)
