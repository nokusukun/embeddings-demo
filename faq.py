import main
from shove import Shove

embedding_store = Shove('file://.cache')
faq_data = [
    {
      "question": "What are the bank's operating hours?",
      "answer": "Our bank operates from Monday to Friday, 9:00 AM to 5:00 PM, and on Saturday from 9:00 AM to 1:00 PM. We are closed on Sundays and public holidays."
    },
    {
      "question": "How can I open a new account?",
      "answer": "To open a new account, you can visit any of our branches with a valid ID and proof of address. Alternatively, you can open an account online through our website."
    },
    {
      "question": "What types of accounts does the bank offer?",
      "answer": "We offer various types of accounts including savings accounts, checking accounts, fixed deposit accounts, and business accounts."
    },
    {
      "question": "What documents are required to open an account?",
      "answer": "To open an account, you need to provide a valid government-issued ID (such as a passport or driver's license) and proof of address (such as a utility bill or lease agreement)."
    },
    {
      "question": "How can I check my account balance?",
      "answer": "You can check your account balance through our online banking portal, mobile app, ATMs, or by visiting any of our branches."
    },
    {
      "question": "What should I do if I forget my online banking password?",
      "answer": "If you forget your online banking password, you can reset it by clicking on the 'Forgot Password' link on the login page and following the instructions. You may also contact our customer support for assistance."
    },
    {
      "question": "How can I report a lost or stolen card?",
      "answer": "If your card is lost or stolen, please report it immediately by calling our 24/7 customer support hotline or through our mobile app. We will block your card and issue a replacement."
    },
    {
      "question": "Does the bank offer loans and mortgages?",
      "answer": "Yes, we offer a variety of loans and mortgages, including personal loans, home loans, auto loans, and business loans. Please visit our website or branch for more details and to apply."
    },
    {
      "question": "What are the bank's fees and charges?",
      "answer": "Our bank's fees and charges vary depending on the type of account and service. For a detailed list of fees, please refer to our fee schedule available on our website or at any branch."
    },
    {
      "question": "How can I contact customer support?",
      "answer": "You can contact our customer support through our 24/7 hotline, email, live chat on our website, or by visiting any of our branches."
    },
    {
      "question": "Does the bank offer online and mobile banking?",
      "answer": "Yes, we offer both online and mobile banking services, allowing you to manage your accounts, transfer funds, pay bills, and more from the convenience of your computer or mobile device."
    },
    {
      "question": "What is the minimum balance requirement for a savings account?",
      "answer": "The minimum balance requirement for a savings account is $100. If the balance falls below this amount, a monthly fee may apply."
    },
    {
      "question": "How can I apply for a credit card?",
      "answer": "You can apply for a credit card online through our website or by visiting any of our branches. You will need to provide personal information and financial details as part of the application process."
    },
    {
      "question": "What should I do if I detect unauthorized transactions on my account?",
      "answer": "If you detect unauthorized transactions on your account, please report them immediately to our fraud department by calling our customer support hotline."
    },
    {
      "question": "How can I set up direct deposit for my paycheck?",
      "answer": "To set up direct deposit for your paycheck, provide your employer with your account number and our bank's routing number. You may need to complete a direct deposit authorization form."
    },
    {
      "question": "Does the bank offer investment services?",
      "answer": "Yes, we offer a range of investment services including mutual funds, stocks, bonds, and retirement accounts. Please schedule an appointment with one of our financial advisors for more information."
    },
    {
      "question": "How do I transfer money between accounts?",
      "answer": "You can transfer money between accounts through our online banking portal, mobile app, by calling our customer support, or by visiting any of our branches."
    },
    {
      "question": "Are my deposits insured?",
      "answer": "Yes, all deposits are insured by the Federal Deposit Insurance Corporation (FDIC) up to the maximum allowed by law, which is currently $250,000 per depositor."
    },
    {
      "question": "Can I schedule automatic bill payments?",
      "answer": "Yes, you can schedule automatic bill payments through our online banking portal or mobile app. Simply set up the payment details and the frequency of the payments."
    },
    {
      "question": "What should I do if I need to update my personal information?",
      "answer": "If you need to update your personal information, such as your address or phone number, you can do so through our online banking portal, mobile app, or by visiting any of our branches."
    }
  ]