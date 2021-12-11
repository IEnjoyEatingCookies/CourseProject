import math
import sys
import time
import metapy
import pytoml


def load_ranker(cfg_file):
    """
    Use this function to return the Ranker object to evaluate, 
    The parameter to this function, cfg_file, is the path to a
    configuration file used to load the index.
    """
    return metapy.index.OkapiBM25(1.5,0.75,3.25)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)

    cfg = sys.argv[1]
    print('Building or loading index...')
    idx = metapy.index.make_inverted_index(cfg)
    ranker = load_ranker(cfg)




    query = metapy.index.Document()


    print('Running queries')
    input_str = "Vector Space Model"
    query.content(input_str.strip())
    results = ranker.score(idx, query, 10)