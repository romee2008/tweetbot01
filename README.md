# Tweet Quote Bot
A simple bot that tweets inspiratonal quotes on twitter. It uses cron job on github action instead of Heroku or other hosts.

## Local Development Setup
N.B: You will need to have a twitter developers account. So make sure you already have one or go to [Twitter Developers](https://developer.twitter.com/en/apply-for-access.html)
to create a developer account.

Steps to Follow for your local machine
1. Clone the repository.
2. Create Virtual environment for python / VS Code is recommended
3. 2. Set Environment Variable on Windows/Linux. Consumer_key, Consumer_Secret, Access_Token Acces_Token_secret
4. Run the bot for sometime on local machine 

Github Workflow Setup

1. Push the repository
2. Set Repository Secrets . Consumer_key, Consumer_Secret, Access_Token Acces_Token_secret
2. Create a yml file in github workflow and paste the tweetworkflow.yml file code in your yml file.
4. Done !!!!
