from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create the FastAPI app
app = FastAPI()

# Sample data for the inventory
inventory = {
    "cheese": 100,  # in kilograms
    "dough": 200,  # in pieces
    "tomato": 150,  # in kilograms
    "pepperoni": 50,  # in kilograms
    "mushroom": 100,  # in kilograms
}

# Model to receive order information from the user
class Order(BaseModel):
    pizza_type: str
    pizza_size: str
    quantity: int

# Agent 1: Inventory Agent (checks availability)
class InventoryAgent:
    def check_ingredients(self, pizza_type: str, pizza_size: str, quantity: int):
        # Simulating some ingredient requirements for each pizza type
        required_ingredients = {
            "margherita": {"cheese": 1, "dough": 1, "tomato": 0.5},
            "pepperoni": {"cheese": 1, "dough": 1, "tomato": 0.5, "pepperoni": 0.2},
            "veggie": {"cheese": 1, "dough": 1, "tomato": 0.5, "mushroom": 0.3}
        }

        if pizza_type not in required_ingredients:
            raise HTTPException(status_code=404, detail="Pizza type not available")

        # Check if there are enough ingredients in the inventory for the requested pizza type and quantity
        ingredients_needed = required_ingredients[pizza_type]
        for ingredient, amount in ingredients_needed.items():
            if inventory[ingredient] < amount * quantity:
                raise HTTPException(status_code=400, detail=f"Not enough {ingredient} in inventory")

        return True

    def update_inventory(self, pizza_type: str, pizza_size: str, quantity: int):
        required_ingredients = {
            "margherita": {"cheese": 1, "dough": 1, "tomato": 0.5},
            "pepperoni": {"cheese": 1, "dough": 1, "tomato": 0.5, "pepperoni": 0.2},
            "veggie": {"cheese": 1, "dough": 1, "tomato": 0.5, "mushroom": 0.3}
        }

        ingredients_needed = required_ingredients[pizza_type]
        for ingredient, amount in ingredients_needed.items():
            inventory[ingredient] -= amount * quantity

# Agent 2: Order Agent (handles orders)
class OrderAgent:
    def __init__(self, inventory_agent: InventoryAgent):
        self.inventory_agent = inventory_agent

    def process_order(self, order: Order):
        # Check if the inventory has enough ingredients
        self.inventory_agent.check_ingredients(order.pizza_type, order.pizza_size, order.quantity)

        # Since pizza is free, we skip payment processing
        # Update inventory after order is placed
        self.inventory_agent.update_inventory(order.pizza_type, order.pizza_size, order.quantity)

        return {"message": f"Order for {order.quantity} {order.pizza_type} pizza(s) of size {order.pizza_size} placed successfully! Pizza is free of cost!"}

# Instantiate the agents
inventory_agent = InventoryAgent()
order_agent = OrderAgent(inventory_agent=inventory_agent)

# FastAPI endpoint for placing an order
@app.post("/order/")
async def place_order(order: Order):
    try:
        return order_agent.process_order(order)
    except HTTPException as e:
        raise e

# FastAPI endpoint to check the inventory
@app.get("/inventory/")
async def get_inventory():
    return inventory

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
