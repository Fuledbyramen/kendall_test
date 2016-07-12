class SinekoController < ApplicationController
  def test
    require 'sqlite3'
    # give the path to the database file instead of file.db
    db = SQLite3::Database.new 'daily_follower.db'

    # Create a table command
    # result = db.execute ("CREATE TABLE IF NOT EXISTS Follower_Reporter(username TEXT, followers REAL, datestamp TEXT, unix REAL)")

    # Insert some data into it
    # db.execute("INSERT INTO `Follower_Reporter` (username, followers, datestamp, unix) VALUES ('ventura_vixens', 35, '#{Date.today-1}', 123)")   


    @followers = db.execute 'SELECT followers, datestamp FROM Follower_Reporter where username="ventura_vixens"'
    @result = {}
    @followers.each { |row| @result[row[1]] = row[0] }
  end
  def index
   
  end

end
