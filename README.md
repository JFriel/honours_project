James Friel
Honours Project 2016/17
"Event Ordering In News Articles"
Supervisor: Shay Cohen

How to Run:
Due to the large size of data retrieved from Wikipedia, it is unable to be stored on GitHub.
To Gather Data yourself
* getArticles.py will print to sdout a large set of event titles, their associated year and the article itself.
* getDoubleSets.py will generate features of the  form [[feature vector],[event1,event2], correct classification]

If you already have double set data
* Run one of the available graph generating scripts (MLP.py is reccomended) this will generate an accuracy and will print
  a dictionary where the value of each key are events that have edges pointing to them from the key.

* Save the dictionary
* Run pathFinder.py to generate optimal pathing and Tau measurment (Warning, this is fragile) 