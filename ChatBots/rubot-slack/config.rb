module Config
  extend self
  attr_accessor :recast_key
  attr_accessor :slack_key
  attr_accessor :id, :url, :team, :team_id, :names, :dms, :users

  def configure
    block_given? ? yield(self) : self
  end

  def regex_names
    regex = '('

    @names.each_with_index do |name, index|
      regex << name
      regex << '|' if index != @names.length - 1
    end

    regex << ')'

    regex
  end
end
