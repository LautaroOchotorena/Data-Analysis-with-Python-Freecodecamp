<h2> Clarification: This project was created using Replit. You can check it on https://replit.com/@LautaroOchotore/Demographic-Data-Analyzer</h2>
<h1>Demographic Data Analyzer</h1>
<div class="challenge-instructions  "><div><section id="description">
<p>You will be <a href="https://replit.com/github/freeCodeCamp/boilerplate-demographic-data-analyzer" target="_blank" rel="noopener noreferrer nofollow">working on this project with our Replit starter code</a>.</p>
<ul>
<li>Start by importing the project on Replit.</li>
<li>Next, you will see a <code>.replit</code> window.</li>
<li>Select <code>Use run command</code> and click the <code>Done</code> button.</li>
</ul>
<p>We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:</p>
<ul>
<li>
<p><a href="https://www.freecodecamp.org/news/python-for-everybody/" target="_blank" rel="noopener noreferrer nofollow">Python for Everybody Video Course</a> (14 hours)</p>
</li>
<li>
<p><a href="https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/" target="_blank" rel="noopener noreferrer nofollow">How to Analyze Data with Python Pandas</a> (10 hours)</p>
</li>
</ul>
</section></div><hr><div><section id="instructions">
<p>In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:</p>
<pre class="language-markdown" tabindex="0" role="region" aria-label=" code example"><code class="language-markdown">|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | &lt;=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | &lt;=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | &lt;=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | &lt;=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | &lt;=50K    |
</code></pre>
<p>You must use Pandas to answer the following questions:</p>
<ul>
<li>How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (<code>race</code> column)</li>
<li>What is the average age of men?</li>
<li>What is the percentage of people who have a Bachelor's degree?</li>
<li>What percentage of people with advanced education (<code>Bachelors</code>, <code>Masters</code>, or <code>Doctorate</code>) make more than 50K?</li>
<li>What percentage of people without advanced education make more than 50K?</li>
<li>What is the minimum number of hours a person works per week?</li>
<li>What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?</li>
<li>What country has the highest percentage of people that earn &gt;50K and what is that percentage?</li>
<li>Identify the most popular occupation for those who earn &gt;50K in India.</li>
</ul>
<p>Use the starter code in the file <code>demographic_data_analyzer</code>. Update the code so all variables set to "None" are set to the appropriate calculation or code. Round all decimals to the nearest tenth.</p>
<p>Unit tests are written for you under <code>test_module.py</code>.</p>
<h2>Development</h2>
<p>For development, you can use <code>main.py</code> to test your functions. Click the "run" button and <code>main.py</code> will run.</p>
<h2>Testing</h2>
<p>We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.</p>
<h2>Submitting</h2>
<p>Copy your project's URL and submit it to freeCodeCamp.</p>
<h2>Dataset Source</h2>
<p>Dua, D. and Graff, C. (2019). <a href="http://archive.ics.uci.edu/ml" target="_blank" rel="noopener noreferrer nofollow">UCI Machine Learning Repository</a>. Irvine, CA: University of California, School of Information and Computer Science.</p>
</section></div><hr></div>
