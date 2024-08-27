
## Introduction

This small python project is designed to send newsletter emails to  subscribers.

## Prerequisites


Python 3.x: Ensure you have Python 3.x installed.

MySQL: You need a MySQL server running locally with the appropriate database and table structure.

PyMySQL: A Python library for MySQL, install it using:

pip install pymysql


## Setup Instructions

This has to be done first before running the python file!

Set Up the Database:

Execute the following SQL commands to set up the database and table:

    CREATE DATABASE newsletter;

    USE newsletter;

    CREATE TABLE details(
        c_names VARCHAR(20),
        c_emails VARCHAR(30),
        limits INT,
        uniqueness VARCHAR(50)
    );

    INSERT INTO details (c_names, c_emails, limits, uniqueness) VALUES 
    ('lilly', 'lilly@gmail.com', 0, ''),
    
    ('tom', 'tom@gmail.com', 0, ''),
    
    ('john', 'john@gmail.com', 0, '');
## Assumptions 
For the sake of project I have used 3 subscribers. 

We are assuming all 3 emails are correct and valid.



## How to run the file:

Download and open the python file emailService.py 

In the first few lines you can see an object would have been instantiated for Connection class.

Change the host,user and password to your configurations in there.

And to simulate sending an email simply run the file.






## What happens with the code:

The first input from us is a letter that is unique for this particular email that we are about to send to the subscribers.

Enter a single alphabet for this runtime input.

Next we have to manually enter the response from the server indicating whether that particular mail is sent or not

Enter "y" to simulate successfull response.

or any other key for unsuccessful response.




## Features Included:

Retry logic with exponential backoff:
    
If you press any key other than "y", the program tries to send the mail again after 2 seconds and if you fail it again, it will try after 4 seconds. And if you fail it for the third time, it will try again in 8 seconds.

Fallback mechanism to switch providers:

And if an email fails to go through even after 3 attempts it will automatically switch provider and try for 3 more times.

Idempotency to prevent duplicate sends:

While assigning an alphabet to an email, it gets stored in the database and you cannot send an another email with the same alphabet.

But if one subscriber's mail did not go through and all others went through, in this case, if you try resending the email, with the same alphabet, this time the program will be sending the email only to that particular subscriber instead of everyone.

Rate Limiting and Status Tracking:

The program cannot send more than 5 emails for each subscriber. And the status of how many emails are sent and what emails(the alphabet) are sent can be seen by refreshing the table in MySQL. The status will also be printed on the console everytime you try to send an email.


    
        

## How to Reset to default conditions:

Once the 5 email limit is reached, the program cannot send anymore emails. 

To reset back, do the following.

From the python file remove this last line 

    e = SendEmail()

And add:

    c = Clear()

Now run the file

This will reset the conditions back to initial assumptions.

Now again, to send emails:

Remove:

    c = Clear()

And add back, creating an instance of the SendEmail class

    e = SendEmail()

Now back to running the file again for sending emails.
