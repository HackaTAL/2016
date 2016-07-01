# Rubot

This repo is a simple architecture to start a slackbot project using Recast.AI, in Ruby.

## Requirements

* Create an account on [Recast.AI](https://recast.ai/signup)
* Create an account on [Slack](https://slack.com/)

## Get your Slack Bot Token

* Log in to Slack and Create a team.
* Go to : https://yourteam.slack.com/services/new/bot (change "yourteam" with the actual name of your team)
* Follow the bot creation process, you will then be able to see your token

## Get your Recast Bot Token

* Log in to your recast account
* Then on your profile, choose your Bot
* In the settings tab, is your precious request Token

## Launch your bot

* Clone this Repository

```
git clone https://github.com/HackaTAL/rubot-slack.git
```

* Fill the config.yml with your tokens

```
recast_key: RECAST_KEY
slack_key: SLACK_KEY
```

#### Run

* install the dependencies

```
bundle install
```

* run your bot

```
ruby rubot.rb
```
