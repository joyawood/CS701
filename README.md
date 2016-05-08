#Visualizing Textual Data

A tool allowing interactive exploration of text files. Focuses on showing connections between themes and words, as well as stats on word and part of speech frequency. Allows upload of txt files, then presents an interface displaying a network graph, wordcloud, and barchart of most common words. 

Currently in rough stages of development. 

To use:

* Run python code, passing txt file as parameter.  Outputs json into directory. 
```
python csv_to_graph_json.py sample.txt
``` 
* Use python to host local server in directory
```
python -m SimpleHTTPServer 8000
```
* Open browser, navigate to:
```
http://localhost:8000/force_graph_combo_cloud.html
```

Double click to see immediate node connections, hover for rudamentary tooltip, click on barchart or wordcloud to see corresponding node in network visualization. 

Known issues:

* Don't search/click until previous search/click has finished fading in. Bad things happen. 
