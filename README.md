# surfs_up
Weather Analysis using SQLite

## Challenge
# Goals 
  - Look at the tempurature statistical data for June and Decmeber and compare the outcomes.
  
# Process
  - I used two different routes to get the info.
      1. I pulled all the data from the session and made all the station's tempurature data a DataFrame.  Using the loc function, I found         all the tempuratures from the month of June and December by making a new column with the month number.
      2. I used SQLAlchemy by importing 'extract' from SQLAlchemy.  I was able to make a conditional argument looking for the temps in             June and December.  I turned these two pulls into DataFrames adn used the describe() function.
      
# Results
  - June
      count   1700
      mean    74.94
      std     3.26
      min     64
      25%     73
      50%     75
      75%     77
      max     85
      
  - December
      count   1517
      mean    71.04
      std     3.75
      min     56
      25%     69
      50%     71
      75%     74
      max     83
      
The tempurature in June is typically 4 degrees higher than December. Even though the means are very close in tempurature, the min temps are very far off.  The lowest temp in December is 8 degrees lower than the June minimum. 

# Recommended Further Analysis
  - I would also look at the rainfall to get a more accurate weather analysis.
  - I would take out the outliars to make sure the data is accurate.  
  - It would be benficial to look into how many temps there are per year.  If a certain year only has a few pieces of info, then we might want to take it out.
