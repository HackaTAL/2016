# encoding: utf-8

$LOAD_PATH.unshift(File.dirname(__FILE__))

require 'yaml'
require 'recastai'
require 'slack-ruby-client'
require 'httparty'
require 'awesome_print'

require 'config'
require 'utils'

# Load the parameters
p = YAML.load_file(File.join(File.dirname(__FILE__), '/config.yml'))

# Check mandatory tokens
raise(ArgumentError, 'RecastAI token is mandatory') if p['recast_key'].nil?
raise(ArgumentError, 'Slack token is mandatory')    if p['slack_key'].nil?

Config.configure do |config|
  config.slack_key = p['slack_key']
  config.recast_key = p['recast_key']
end

module Rubot
  extend self

  def run!
    # Init the bot with it's hooks and api clients
    self.init!

    # Get the auth infos for the bot
    auth = @slack_client.web_client.auth_test

    # Set the config from the response
    Config.url = auth['url']
    Config.id = auth['user_id']
    Config.team = auth['team']
    Config.team_id = auth['team_id']
    Config.names = [auth['user'], "#{auth['user']}:", "<@#{auth['user_id']}>", "<@#{auth['user_id']}>:"]
    Config.dms = @slack_client.web_client.im_list['ims']

    # Start the client
    @slack_client.start!
  end

  def init!
    @slack_client = Slack::RealTime::Client.new(token: Config.slack_key)
    @recast_client = RecastAI::Client.new(Config.recast_key)

    # On connexion, do something
    @slack_client.on(:hello) do |_|
    end

    # On message, check if its for us, then do the logic!
    @slack_client.on(:message) do |slack|
      explicit = !slack['text'].nil? && !slack['text'].match(/^<@#{Config.id}>:?\s?/).nil?
      implicit = Config.dms.any?{ |im| im['id'] == slack['channel'] }

      if !slack['user'].nil? && slack['user'] != Config.id && (explicit || implicit)
        # Remove Rubot's name from the sentence in order to be processed by Recast.AI
        slack['text'].gsub!(/^<@#{Config.id}>:?\s?/, '')

        recast = @recast_client.text_request(slack['text'])

        if recast.intents.any?
          @slack_client.send_message(slack['channel'], "Hey, I understood '#{recast.intent}'")
        else
          @slack_client.send_message(slack['channel'], "Looks like I some more code...")
        end
      end
    end

    # On error, do something
    @slack_client.on(:error) do |slack|
    end
  end
end

Rubot.run!
