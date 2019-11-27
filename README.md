# GitSecure


**About GitSecure**

GitSecure is a GitHub action that can be used to alert security teams of any exposed API keys for push and pull requests. When files are added or modified on a GitHub repo, this action will be initiated and will start looking for exposed credentials in the system. After finding a token, it will alert the team via Slack Webhooks.

**Setup**

Setup of DataSecure is easy and requires not much of a hassle. 

1) Create a Slack Webhook

You can create a Slack Webhook by going to https://api.slack.com and making an app. When creating the app, select it to be an incoming webhook, and install the webhook to the channel where you want to receive the alerts.

After installing the webhook, copy the URL that Slack provides. You only need to copy the content after https://hooks.slack.com/services/. 


2) Setup Secrets

GitHub action use secrets to prevent disclosure of sensitive information. Go to your repository settings and click on Secrets. There create a secret and for the value paste the webhook portion copied above. 

3) Setting up action

To setup action, next to `Pull Requests` click on `Actions`. In the setup click `Setup a Workflow Yourself`. Paste the following yaml description: 

```
on:
  push:
    branches:
      - master

jobs:
  detect_tests:
    runs-on: ubuntu-latest
    name: A workflow to test the work of DataSecure
    steps:
    - name: Checkout
      uses: actions/checkout@v1
    - name: CodeAnalysis
      uses: bugbounty-site/DataSecure@master
      with:
        slack_hook: ${{ secrets.slack_webhook }}
```

Change the `slack_webhook` to the name of the secret you created in your settings.
