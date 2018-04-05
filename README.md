# Team 6:
- Justin Chin
- Kenneth (Hunter) Wapman
- Christopher Godley

# How to run it:
- start up a server (python or otherwise) and open up the index page at the root of the directory. you can navigate to the visualizations from here!

# Visualization 1: Graph Comparison of Country Average Technology Sentiment and Ownership:
<h3>Contributor: Justin Chin </h3>

<h4>Attributes Analyzed/Visualized: </h4>
<ol>
  <li> I consider myself: </li>  
  <li>Ownership of Electronics (Check all the internet connected devices you currently own: WiFi, Laptop, Smart Phone, Smart TV etc) </li>
  <li> Country </li>
  <li> Thinking about a future in which so much of your world is connected to the internet leaves you feeling: </li>
</ol>

<h4> Process </h4>
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
<h4>Bells and Whistles </h4>
<ol>
  <li> removed Other/Custom responses from the raw dataset. </li>
  <li> replaced NaN responses with 0s. </li>
</ol>

# visualization 2 (Hunter):
- choose two "feelings" questions
- user can select two different values to look at, one from each question
- dots will be elements by language

# visualization 3 (Chris):
