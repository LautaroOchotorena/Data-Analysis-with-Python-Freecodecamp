<h1> Medical Data Visualizer </h1>
<div class="challenge-instructions  "><div><section id="description">
<p>You will be <a href="https://replit.com/github/freeCodeCamp/boilerplate-medical-data-visualizer" target="_blank" rel="noopener noreferrer nofollow">working on this project with our Replit starter code</a>.</p>
<ul>
<li>Start by importing the project on Replit.</li>
<li>Next, you will see a <code>.replit</code> window.</li>
<li>Select <code>Use run command</code> and click the <code>Done</code> button.</li>
</ul>
<p>We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:</p>
<ul>
<li>
<p><a href="https://www.freecodecamp.org/news/python-for-everybody/" target="_blank" rel="noopener noreferrer nofollow">Python for Everybody Video Course</a>(14 hours)</p>
</li>
<li>
<p><a href="https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/" target="_blank" rel="noopener noreferrer nofollow">How to Analyze Data with Python Pandas</a> (10 hours)</p>
</li>
</ul>
</section></div><hr><div><section id="instructions">
<p>In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.</p>
<h2>Data description</h2>
<p>The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.</p>
<p>File name: medical_examination.csv</p>
<table>
<thead>
<tr>
<th align="center">Feature</th>
<th align="center">Variable Type</th>
<th align="center">Variable</th>
<th align="center">Value Type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Age</td>
<td align="center">Objective Feature</td>
<td align="center"><code>age</code></td>
<td align="center">int (days)</td>
</tr>
<tr>
<td align="center">Height</td>
<td align="center">Objective Feature</td>
<td align="center"><code>height</code></td>
<td align="center">int (cm)</td>
</tr>
<tr>
<td align="center">Weight</td>
<td align="center">Objective Feature</td>
<td align="center"><code>weight</code></td>
<td align="center">float (kg)</td>
</tr>
<tr>
<td align="center">Gender</td>
<td align="center">Objective Feature</td>
<td align="center"><code>gender</code></td>
<td align="center">categorical code</td>
</tr>
<tr>
<td align="center">Systolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_hi</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Diastolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_lo</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Cholesterol</td>
<td align="center">Examination Feature</td>
<td align="center"><code>cholesterol</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Glucose</td>
<td align="center">Examination Feature</td>
<td align="center"><code>gluc</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Smoking</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>smoke</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Alcohol intake</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>alco</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Physical activity</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>active</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Presence or absence of cardiovascular disease</td>
<td align="center">Target Variable</td>
<td align="center"><code>cardio</code></td>
<td align="center">binary</td>
</tr>
</tbody>
</table>
<h2>Tasks</h2>
<p>Create a chart similar to <code>examples/Figure_1.png</code>, where we show the counts of good and bad outcomes for the <code>cholesterol</code>, <code>gluc</code>, <code>alco</code>, <code>active</code>, and <code>smoke</code> variables for patients with cardio=1 and cardio=0 in different panels.</p>
<p>Use the data to complete the following tasks in <code>medical_data_visualizer.py</code>:</p>
<ul>
<li>Add an <code>overweight</code> column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is &gt; 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.</li>
<li>Normalize the data by making 0 always good and 1 always bad. If the value of <code>cholesterol</code> or <code>gluc</code> is 1, make the value 0. If the value is more than 1, make the value 1.</li>
<li>Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's <code>catplot()</code>. The dataset should be split by 'Cardio' so there is one chart for each <code>cardio</code> value. The chart should look like <code>examples/Figure_1.png</code>.</li>
<li>Clean the data. Filter out the following patient segments that represent incorrect data:
<ul>
<li>diastolic pressure is higher than systolic (Keep the correct data with <code>(df['ap_lo'] &lt;= df['ap_hi'])</code>)</li>
<li>height is less than the 2.5th percentile (Keep the correct data with <code>(df['height'] &gt;= df['height'].quantile(0.025))</code>)</li>
<li>height is more than the 97.5th percentile</li>
<li>weight is less than the 2.5th percentile</li>
<li>weight is more than the 97.5th percentile</li>
</ul>
</li>
<li>Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's <code>heatmap()</code>. Mask the upper triangle. The chart should look like <code>examples/Figure_2.png</code>.</li>
</ul>
<p>Any time a variable is set to <code>None</code>, make sure to set it to the correct code.</p>
<p>Unit tests are written for you under <code>test_module.py</code>.</p>
<h2>Development</h2>
<p>For development, you can use <code>main.py</code> to test your functions. Click the "run" button and <code>main.py</code> will run.</p>
<h2>Testing</h2>
<p>We imported the tests from <code>test_module.py</code> to <code>main.py</code> for your convenience. The tests will run automatically whenever you hit the "run" button.</p>
<h2>Submitting</h2>
<p>Copy your project's URL and submit it to freeCodeCamp.</p>
</section></div><hr></div>
