import os
import sys
from openai import OpenAI
import asyncio
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from agents import Agent, Runner
from paypal_agent_toolkit.openai.toolkit import PayPalToolkit
from paypal_agent_toolkit.openai.tool import PayPalTool
from paypal_agent_toolkit.shared.configuration import Configuration, Context

#uncomment after setting the env file
# load_dotenv()
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
OPENAI_API_VERSION = "2024-02-15-preview"

configuration = Configuration(
    actions={
        "orders": {
            "create": True,
            "capture": True,
            "get": True
        },
        "products": {
            "create": True,
            "list": True,
            "show": True
        },
        "subscriptionPlans": {
            "create": True,
            "list": True,
            "show": True
        },
        "subscriptions": {
            "create": True,
            "show": True,
            "cancel": True
        },
        "invoices": {
            "create": True,
            "get": True,
            "list": True,
            "send": True,
            "sendReminder": True,
            "cancel": True,
            "generateQRC": True,
        },
        "shipment": {
            "create": True,
            "get": True,
            "list": True
        },
        "disputes": {
            "create": True,
            "get": True,
            "list": True
        },
        "transactions": {
            "list": True
        },
    },
    context=Context(
        sandbox=True,
    )
)


# Initialize toolkit
toolkit = PayPalToolkit(PAYPAL_CLIENT_ID, PAYPAL_SECRET, configuration)
tools = toolkit.get_tools()


# OpenAI client with SSL verify off
client = OpenAI()

# Initialize OpenAI Agent
agent = Agent(
    name="PayPal Assistant",
    instructions="""
    You assist users in creating and managing payments, disputes, subscriptions, shipments, and more. Based on the HATEOAS links in the response, you provide next steps, actionable recommendations, and suggest appropriate prompts to guide them effectively.
    """,
    model="gpt-4o",
    tools=tools
)

runner = Runner()

async def main():
    print("PayPal Assistant (OpenAI Agents). Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            break

runner = Runner()

async def main():
    print("PayPal Assistant (OpenAI Agents). Type 'exit' to quit.")

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in {"exit", "quit"}:
                break

            try:
                result = await runner.run(agent, user_input)

                # Print final response if no tools were involved
                if hasattr(result, "final_output") and result.final_output:
                    print("🤖 Assistant:", result.final_output)
                else:
                    print("🤖 Assistant: No response generated.")
            except Exception as e:
                print("❌ Error running agent:", e)

        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            break
        except Exception as e:
            print("❌ Unexpected error:", e)

# Run the main loop
asyncio.run(main())
