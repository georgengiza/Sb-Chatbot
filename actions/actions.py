# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import actions.database_connection as connection

#******************************************************** ActionCheckBalance *********************************************
def get_balance_from_db(account_number):
    query = "SELECT [Amount]  FROM [BIGDATA].[dbo].[STG_DEPOSIT_LISTING_TEMP]  WHERE [Account Number] = "+ str(account_number)
    cursor = connection.database_connection()
    amount = cursor.execute(query).fetchone()[0]
    cursor.close()
    return str(amount)

class ActionCheckBalance(Action):
    def name(self):
        return "action_check_balance"

    def run(self, dispatcher, tracker, domain):
        # Fetch the account number from the slot
        account_number = tracker.get_slot("account_number")

        if account_number is None:
            # Ask the user for their account number if it's not provided
            dispatcher.utter_message(text="Please provide your account number.>>>>ba1")
        else:
            # Simulate balance fetching from a backend (replace this with actual logic)
            balance = get_balance_from_db(account_number)

            # Respond to the user with the account balance
            dispatcher.utter_message(text=f"Your balance for account {account_number} is ${balance}.")


        return []



#******************************************************** ActionTransactionHistory *********************************************
def get_recent_transactions(account_number):
    return "getting latest transactions"


class ActionTransactionHistory(Action):
    def name(self):
        return "action_transaction_history"

    def run(self, dispatcher, tracker, domain):
        account_number = tracker.get_slot("account_number")
        # Fetch last 5 transactions (mock data here)
        transactions = get_recent_transactions(account_number)  # Placeholder
        message = "Here are your last 5 transactions:\n"
        for transaction in transactions:
            message += f"- {transaction['date']}: {transaction['type']} of ${transaction['amount']}\n"
        dispatcher.utter_message(text=message)
        return []


#******************************************************** ActionPayBill *********************************************

def process_bill_payment(account_number, bill_type, amount):
    print("Processing Bill payment")
    return True
    #pass


class ActionPayBill(Action):
    def name(self):
        return "action_pay_bill"

    def run(self, dispatcher, tracker, domain):
        bill_type = tracker.get_slot("bill_type")  # Example: electricity, water
        amount = tracker.get_slot("amount")
        account_number = tracker.get_slot("account_number")
        # Simulate the payment process
        success = process_bill_payment(account_number, bill_type, amount)  # Placeholder
        if success:
            dispatcher.utter_message(text=f"Your {bill_type} bill of ${amount} has been successfully paid.")
        else:
            dispatcher.utter_message(text=f"Failed to pay your {bill_type} bill. Please try again.")
        return []


#******************************************************** ActionTransferFunds *********************************************

def transfer_funds(from_account, to_account, amount):
    print("Processing funds transfer")
    return True


class ActionTransferFunds(Action):
    def name(self):
        return "action_transfer_funds"

    def run(self, dispatcher, tracker, domain):
        print("In ActionTransferFunds.run function")
        from_account = tracker.get_slot("from_account")
        to_account = tracker.get_slot("to_account")
        amount = tracker.get_slot("amount")
        # Simulate fund transfer process
        success = transfer_funds(from_account, to_account, amount)  # Placeholder
        if success:
            print("ActionTransferFunds successful")
            dispatcher.utter_message(text=f"${amount} has been transferred to {to_account}.")
        else:
            print("ActionTransferFunds failed")
            dispatcher.utter_message(text=f"Failed to transfer ${amount}. Please try again.")
        return []


#******************************************************** ActionPayBill *********************************************
def get_loan_status(loan_number):
    print("Checking Loan status")
    return "Balance: 3790, next payment 20241101"

class ActionLoanStatus(Action):
    def name(self):
        return "action_loan_status"

    def run(self, dispatcher, tracker, domain):
        loan_number = tracker.get_slot("loan_number")
        # Simulate fetching loan details
        loan_details = get_loan_status(loan_number)  # Placeholder
        message = f"Your loan status:\nBalance: ${loan_details['balance']}\n" \
                  f"Next Payment Due: {loan_details['due_date']}\nInterest Rate: {loan_details['interest_rate']}%"
        dispatcher.utter_message(text=message)
        return []

#******************************************************** ActionOpenAccount *********************************************

def open_bank_account(account_type):
    print("Creating new Account")
    pass


class ActionOpenAccount(Action):
    def name(self):
        return "action_open_account"

    def run(self, dispatcher, tracker, domain):
        account_type = tracker.get_slot("account_type")
        # Simulate account opening process
        success = open_bank_account(account_type)  # Placeholder
        if success:
            dispatcher.utter_message(text=f"Your {account_type} account has been successfully opened.")
        else:
            dispatcher.utter_message(text=f"Failed to open {account_type} account. Please try again.")
        return []


#******************************************************** ActionPayBill *********************************************