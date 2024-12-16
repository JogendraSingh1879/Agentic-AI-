# Agentic AI
# Building and Deploying a Free Pizza Ordering System with FastAPI and Multi-Agent Architecture

Here's a complete use case for a multi-agent system (MAS) incorporating two agents in the context of an online pizza store. The two agents in this system will be:

**Order Agent:** Handles the order placement, takes the pizza order from the customer, and processes the payment.
Inventory Agent: Manages the inventory of pizza ingredients and updates the stock after each order.
The system will be exposed as a REST API using FastAPI.

# Use Case: Online Pizza Store

# Actors:
**Customer:** Places pizza orders through the system.
**Order Agent:** Responsible for taking orders and initiating payments.
**Inventory Agent:** Manages the inventory of ingredients and updates stock.
**Goal:** Allow a customer to place an order for a pizza, check if the inventory has sufficient ingredients, and then confirm the order after payment.

# Agents and Responsibilities:

**1. Order Agent:**

Receives the order details (pizza size, type, quantity).
Validates if the pizza type and size are available.
Sends the request to the Inventory Agent to check the ingredient availability.
Handles the payment processing.

**2. Inventory Agent:**

Manages the inventory of pizza ingredients (e.g., cheese, dough, toppings).
Checks if sufficient ingredients are available to fulfill the order.
Updates the stock after the order is placed.

# Multi-Agent System Architecture:

Order Agent communicates with the Inventory Agent via API calls (synchronous or asynchronous).
The Inventory Agent checks the availability of ingredients in the system.
Order Agent responds to the customer based on inventory availability and processes the payment.
The Order Agent and Inventory Agent are exposed as separate endpoints using FastAPI.

Python Code Implementation

FastAPI Setup

Order Agent and Inventory Agent as separate endpoints

Communication between Order and Inventory Agents
