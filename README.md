# Team 6:
- Justin Chin
- Kenneth (Hunter) Wapman
- Christopher Godley

# How to run it:
- start up a server (python or otherwise) and open up the index page at the root of the directory. you can navigate to the visualizations from here!

- For Visualization 1:  
1. Download the and extract zip of the repo, or just download the folder JustinChin from the repo.    
2. Run Anaconda and open up the Jupyter notebook named JChin_Mozilla_Graphs in JustinChin folder.
3. Run all of the cells in the notebook with Python2 as the interpretter

# Visualization 1: Graph Comparison of Country Average Technology Sentiment and Ownership:
<h3>Contributor: Justin Chin </h3>

<h4>Attributions</h4>
Bokeh boxplot code modified from https://bokeh.pydata.org/en/latest/docs/gallery/boxplot.html
Widgets snippet from http://bokeh.pydata.org/en/latest/docs/user_guide/interaction/widgets.html#userguide-interaction-widgets

<h4>Attributes Analyzed/Visualized: </h4>
<ol>
  <li> I consider myself: </li>  
  <li>Ownership of Electronics (Check all the internet connected devices you currently own: WiFi, Laptop, Smart Phone, Smart TV etc) </li>
  <li> Country </li>
  <li> Thinking about a future in which so much of your world is connected to the internet leaves you feeling: </li>
</ol>

<h4> Process </h4>
First filtered country surveys by removing countries with less than 1000 surveys submitted.

Converted text responses to ordinal variables.
<ol>
<li> I consider myself:
 <ul>
  <li> Ultra Nerd:  I build my own computers, run my own servers, code my own apps. I'm basically Mr. Robot. = 4 </li>
  <li> Technically Savvy:   I know my way around a computer pretty well. When anyone in my family needs technical help, I'm the one they call. = 3 </li>
  <li> Average User:   I know enough to get by. = 2 </li>
  <li> Luddite:  Technology scares me! I only use it when I have to. = 1 </li>
 </ul>
</li>
<li> Ownership of Electronics (Sum of owned electronics from 0-1) </li> 
<li> Thinking about a future in which so much of your world is connected to the internet leaves you feeling:  </li>
 <ul>
  <li>Scared as hell. The future where everything is connected has me scared senseless. We are all doomed! = -2 </li>
  <li>A little wary. All this being connected to the internet in every part of our lives makes me a little nervous. What is going to happen to our privacy? = -1 </li>
  <li>On the fence.  I'm not sure about all this. I think I'll wait and see. = 0 </li>
  <li>Cautiously optimistic. I am hopeful we are building a better world by becoming more connected in everything we do. = 1 </li>
  <li>Super excited! I can't wait for everything to be connected. My life will be so much better. = 2 </li>
  </ul>
</ol>

<h4>Chart Description</h4>
- Question 1: Is the average number of owned electronics or "knowledge of technology" correlated to each country's average sentiment for the future of tech?  This is answered with two coordinated scatter plots that plots each of these averaged values versus the average sentiment.
- Hovering over each point, which represented a country, popped up with a tooltip showing the country's name as well as the number of surveys submitted.

- Question 2: For a country, what is the distribution of individual responses based on their sentiment for the future of tech?  We can drill down and look at the distribution of each sentiment response groups to see if there are any correlations since this is likely hidden when calculating overall averages.  For example, for a country, like the US, did survey responders who reported having a negative outlook of the future own more electronics or were more knowledgable about technology?  
- This question was answered by plotting boxplot of each question answered for a selected country by each binned sentiment response (-2,-1,0,1,2).
- A dropdown menu allowed the user to select which country he/she would like to drilldown and inspect the distribution of responses.

<h4>Bells and Whistles </h4>
<ol>
  <li> removed Other/Custom responses from the raw dataset. </li>
  <li> replaced NaN responses with 0s. </li>
  <li> The two scatter plots correlating average # owned electronics and knowledge of technology with sentiment for the future are linked graphs.  Clicking a point (Country) in one scatter plot shows the country's position in the other corresponding scatter plot.  </li>
  <li> Dropdown menu for selecting a country allows for drill down of the distribution of responses, using boxplots, for individual responses (# of owned electronics and technological knowledge ) for each sentiment response group</li>
</ol>

# visualization 2 (Hunter):
- geographic data

# visualization 3 (Chris):
