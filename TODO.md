TO DO:
1) Make clear how i used the models:

- run random foresr for classificaiotn of data scientists
- run NB trained with just CLsssif profile to asses background
- use k-means to suggest closest data scientists


tie together the feature part

2) Say some actionalble items for recruiters:
  - > they may want to see your background becsue they have lost a person 
  and they want one with the similar strength or background.
  -> they knwo they need mor of an engineer / CS profile that need


Also what are the top X features for a data scientist.

Say something about the curve of distribution of PhD.


0) Run again some cross validation testing in my k-means and NMF


1) Have the applicaiton running on Ec2
   -> Have a new folder which is webapp_cloud with the tar from racksapce
   -> Try to optimize..

2) 

Tomorrow:
read again the text of the website and check spellings error


Graph:
0) Normalize between 0 and 100 the thinkness


Presentation:


1) Dont' be defensive

2) Explain why naive bayse and so on

3) Graph colors

4) More the 30 seconds pitch

5) Add a Linkedin Page and check all the information I colelcted.
-> Scraped form the web educaitons and skills.

6) Anchor slide


Add why i was nterested in this in the first place



1) Notes on the presentation:
-> why did you make choices for a certain models
-> 

2) End on the next steps (put some job ads and candidate matching)
    -> Generalization (much more of an)
    -> 

3) Zero Context:
   1) very intentional first sentence: what is that your product did

4) Try to have a name for your project
    - design make it better
     _ What I was predicting and there were the most impotant features 
     used -> features engineering I did

5) These where the important features and what came out
   was an output target variables:
  -> classification of 

  Model using this input predicting this output
  
====================

Add twitter handle
Add the links and the 
Presentation:
1) have  better pic for the Phd (maybe add the masters and have the perentage.
Have some animation about the tag cloud.

2) Have a pic and numbers for clusters and how many data Scientists

Something to be done:

1) Try to get better legend and tuff out of the plots
-> Maybe saving the json and tweak it by hand,

2) Think about how to visualize skills relations other than bag of words.
Tomorrow.

3) Build or figure out


Nice to have
0) Spinning weel while waiting for results..

Toorrow:
-> Build a Naive Bayse (which i did) just with the other sample.
-> Classify then the DS and see form all of them the average distribution of "components"

0) Work to build a networks of skills

1) Go through a story of the presentaion 


TO DO fine tuning web app
===========
1) Dont' recsale the y scale but have it fixed to 100
3) Have a better list of skills with associated resources
(Built offline frm a DB -> that I can update)
4) See other skills dropdown

4) CHeck the lenght of fields returned and 
if they are zero whow a different message


TO DO again about model testing
==========

1) Test and build the model with the top 100 variables
for the 

-> see what happens if I calssify with random forest
with all the variables.
See if I have the smae reuslts.
Compare the results -> See if they make sense wrt the components.






VERIFY:
order of the classes returned..



By wed: get even a simple web-up locally to work (with the bars as interactive 
some dynamic usggesitons of content)

Optional : Visualization of networks of skills focusing on the top 50 for each group
(Or the top 100 overall from my RF).
Maybe over the week end.

Key points for the presentation:
show that the data I have skills and educaiton can tell apart
and at the same time find similarities:
not interested in acccuracy here.

Question: shall I use a RF to classify rather than the NB?


Presentation:

Problems / questions to answer:
  -> small dataset
  
  -> lot's of features comapred ot the data
    -> Also overfitting
    -> have the users declare their labels and then rebalance the model
  
  -> Naive Baseyes but skills aren't independent most of the time
      -> stillif you look at there is clarly spltit across BA vs Machine Learning vs 
 
  -> Fails on categories I haven't seen at all (realtor)
      -> The scope is to 

1 SLide: why , what? (focus on can I be a DS... expand to the potentiial in the last slide)
2 Slide how (number of datapoints, pipeline, )

3 Some results -> tag cloud, skills network (educaiton network)
  -> here say that the data pints were enough
  SHow that the proportions and the content are similar to larger data
  (infographics venture beat about Phds and other data, Peter Schok, Analyzing the Analizers)
  -> this will serve to answer the objection about a small dataset

4) The analysis -> I can cluster and classify using skills and education
    -> BUild a prototype web app:
    Screeshot webapp (few explanation)

5) Future works / improvement
   - > enlrage the dataset do it interactiveley with users coming to vivit
(links , ack , What should be improved : more data, finer parsers,
Next steps: )
===============

0) Get the ball rollin gwith the workflow for the app:
1) write code form the linkeidn public URL to 
-> I've got the features...


CalculatedL 
-> closest profiles
-> missing skills -> resources

-> Histogram of the 5 components (they aybe be 4 ...)
-> How to access for one value i predict the tree 


I want to return


Tonight:
- plot the notworks of skills (where the link came from , 0,1,2,3,4)
- If I want start playing with clustering visualization in D3
- Play with dinamic barplot

EC2 :
Mongodump -> to have the same DB to EC2.
Also install the gem




================
FINAL IDEA:
1) Klout for data scientists.
How do you score in:

Computer Science  (Software Engineering)
Business Analyst
Statistician
Mathematician

Data Scientist
-> Have as an example: the bars
http://columbiadatascience.com/2012/09/08/data-scientist-profiles/

Or the star:
http://columbiadatascience.com/2012/12/08/the-stars-of-data-science/


2) With a decision three also whos 

3) Closests Linkedin profiles:

Things to show:
- Top skills as lists / D3
- Top education
- COmparing top skills form K-menans, NMF , Decision tree
- Show that labels returned from Linkedin or self asserted
arent' really meaningful: (as out assumption)



For later :
==========

1) Try the bernoully NB
2) Try to improve with some additional data


2) Approach is the exploratory cluster analysis 
and have the user experiment with it

3) The ohter approach can be more of a classification 
You are a 75% of a statistician.

Use random forest for a new user.
You have a strong math background
st
Mathematician

And then run random forest.

For random forest don't drop anything.
The cool thing would I come to an app
and I would say : based on your skills you are most a "Engineer"
And you have these skills in commons ->
The finish app is something like...
What is a value and what they can't get:

4) A recommender approach:
DO you know these top things?
-> like a list of the top skills
I'm going to recommend resources to a person on how to 

Based on the diagnostics you can have an app to collect
you own metrics. WHich links they clicked on 
based on their classificaiton?



Quetions for jon:

-> epliminating all the zeros values in my case folks I didn't
have skills or education or persons for which after features reduciotn
i het all zeros (just top skills)


-> K-means = 2 for now and tell whcih cluster I belong

-> Build a random forest


2) Gather all the data I need 
   -> format the dat nicely

	lunch

3) Run a kmeans with k = 2 with
   education and skills to see if I can tell people
   apart 

   -> training set / tests sets testing 





Tonight:
- If I have time try to compute some more features to get stats
- look at perers video again and figure out some searches that will give me
some good results

For later:
==============
- Do some more NMF and SVD analysis on clustering

- Add the multiindex search on the skills
http://docs.mongodb.org/manual/tutorial/model-data-for-keyword-search/
How to do that:
db.ext_profiles_education_ds.ensureIndex( { skills: 1 } )


- Get linkedin premium and try to get more data
- Change the location of the DB under the project (this can wait)
- Try to explore all the connections for the people I have (once I've got t)
- Think about the best way to maintain Old information with the enhanced one in a persistent way
	-> separate mongo xollections
	-> pandas dataframe
	-> For now just separate mongoDB collections
- refactor and strealine all the pipeline (and generalize)


IMPORTANT:
Once I have the skills I want to create the multikeys 
http://docs.mongodb.org/manual/tutorial/model-data-for-keyword-search/

===============================================

