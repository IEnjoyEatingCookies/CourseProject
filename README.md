# Coursera Transcript Search

We created an interface with Flask for a client to search the transcripts of lectures on Coursera. The server ranks a collection of lectures based on the query and serves the updated webpage with the search results. There is also a content-based recommender system.

## Get Started

### Installation
The dependency `metapy` only works on certain versions of Python 3, such as 3.5.10. It is recommended to set up a virtual environment with a version that works with `metapy`.
1. Clone the repository
```
git clone https://github.com/IEnjoyEatingCookies/CourseProject.git
```
2. Install dependencies
```py
pip install metapy pytoml flask coursera-dl
```


### Scrape Dataset
If the project already has the dataset included, then this step can be skipped.

1. Enter your credentials in `GetTranscript.py`. To get your CAUTH, you must use chrome. Go to `Chrome Settings > Cookies` and in the dropdown, click https://www.coursera.org/. Then find and click `Copy value CAUTH`.
2. Download the raw dataset.
```py
python GetTranscripts.py
```
3. Build the dataset. Keep `BuildDataset.py` outside of the folder that contains the scraped data. Running the script creates `allData.txt`,  which contains all of the video transcript and text files from Coursera.
```py
python BuildDataset.py
```
4. Format the dataset.
```py
python GetLessonTitle.py
```

##  Usage

Run the flask server.
```py
flask run
```

