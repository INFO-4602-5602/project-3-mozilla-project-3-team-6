# Team 6:
- Justin Chin
- Kenneth (Hunter) Wapman
- Christopher Godley

# How to run it:
- start up a server (python or otherwise) and open up the index page at the root of the directory. you can navigate to the visualizations from here!

### For Visualization 1:  
1. Download the and extract zip of the repo, or just download the folder JustinChin from the repo.    
2. Run Anaconda and open up the Jupyter notebook named JChin_Mozilla_Graphs in JustinChin folder.
3. Run all of the cells in the notebook with Python2 as the interpretter

# Visualization 1: Graph Comparison of Country Average Technology Sentiment and Ownership (Justin Chin) :
<h4>Attributions</h4>
- Bokeh boxplot code modified from https://bokeh.pydata.org/en/latest/docs/gallery/boxplot.html
- Widgets snippet from http://bokeh.pydata.org/en/latest/docs/user_guide/interaction/widgets.html#userguide-interaction-widgets

<h4>Attributes Analyzed/Visualized: </h4>
<ol>
  <li> I consider myself: </li>  
  <li>Ownership of Electronics (Check all the internet connected devices you currently own: WiFi, Laptop, Smart Phone, Smart TV etc) </li>
  <li> Country </li>
  <li> Thinking about a future in which so much of your world is connected to the internet leaves you feeling: </li>
</ol>

<h4> Process </h4>
<h5>Preprocessing</h5>
The raw dataset was first filtered by removing countries with less than 1000 surveys submitted to reduce potential for overplotting of all countries.  Then the survey text responses were coverted into ordinal values which could be averaged and plotted on graphs.  Luckily the survey responses had ordinal properties including the question (Thinking about a future in which so much of your world is connected to the internet leaves you feeling) which ranged from negative values (negative sentiment) to positive values representing positive sentiment.  Custom/user input responses were removed from all questions since they may not be consistent with the ordinal range.  The following shows how each response was mapped to an ordinal value.

Converted text responses to ordinal variables.
<ol>
<li> I consider myself:
 <ul>
  <li> Ultra Nerd... = 4 </li>
  <li> Technically Savvy... = 3 </li>
  <li> Average User... = 2 </li>
  <li> Luddite... = 1 </li>
 </ul>
</li>
<li> Ownership of Electronics (Sum of owned electronics from 0-11) </li> 
<li> Thinking about a future in which so much of your world is connected to the internet leaves you feeling:  </li>
 <ul>
  <li>Scared as hell... = -2 </li>
  <li>A little wary... = -1 </li>
  <li>On the fence... = 0 </li>
  <li>Cautiously optimistic... = 1 </li>
  <li>Super excited!... = 2 </li>
  </ul>
</ol>

<h4>Chart Description and the Design Considerations</h4>
The first question I wanted to be able to answer was: Is the average number of owned electronics or the average person's "knowledge of technology" correlated to country's average sentiment for the future of tech by country?  To answer this I created two coordinated scatter plots that plotted the averaged responses versus the average sentiment for each country.  These two plots give insight of whether there is an overall correlation, since all responses were averaged, of these factors on a country by country basis.  In addition to plotting the averaged values, the plot allowed for interactivity by enabling a tooltip to popup when hovering over each point in the plot.  Each point represented a country with tooltip showing the country's name as well as the number of surveys submitted.  Each point was also assigned a distinct color representing each country.  

One of the challenges of this plot was labelling and making each point distinct to discern each country.  I thought the two plots should be separated to allow correlating the two relationships.  Also representation of all of the countries, roughly 20 in the filtered dataset, proved challenging since they all needed to be in the same plot for correlating the data.  Changing the marks of the countries to the shape of the country didnt make sense since it could skew the perception of the location of the point.  Representing the country based on color seemed the best method, although there did not seem to be a clear way of associating 20 colors with each country.  A legend was also left out of the plot since it would have taken a lot of space compared to the plot itself.  So the information about the country is presented through selection and hovering over the points.  This was the best solution we could think of considering the the number of countries plotted.

The second question I wanted to answer was for a country, what was the distribution of individual responses based on their sentiment about the future of technology?  Drilling down the distribution of each sentiment response groups can show any correlations that are likely hidden when calculating overall country survey response averages.  For example, for a country, did survey responders who reported having a negative outlook of the future own more electronics or were more knowledgable about technology than those were were more positive?  
- This question was answered by plotting boxplot of each question answered for a selected country by each binned sentiment response (-2,-1,0,1,2).
- A dropdown menu allowed the user to select which country he/she would like to drilldown and inspect the distribution of responses.

<h4>Bells and Whistles </h4>
<ol>
  <li> Missing Data: Removed Other/Custom responses from the raw dataset and replaced NaN responses with 0s. </li>
  <li> Coordinated Views: The two scatter plots correlating average # owned electronics and knowledge of technology with sentiment for the future are linked graphs.  Clicking a point (Country) in one scatter plot shows the country's position in the other corresponding scatter plot.  </li>
  <li> Dropdown menu for selecting a country allows for drill down of the distribution of responses, using boxplots, for individual responses (# of owned electronics and technological knowledge ) for each sentiment response group</li>
  <li> Semantic Zoom:  Users can look at the overall average sentiment and survey responses for each country, or drill down to individual response from each country, using the dropdown menu at the top of the visualization, binned by their sentitment response.</li>
</ol>

# visualization 2 (Hunter):
- choose two "feelings" questions
- user can select two different values to look at, one from each question
- dots will be elements by language

# visualization 3 (Chris):
