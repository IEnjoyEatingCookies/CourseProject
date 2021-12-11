import math


def rec_query(past_queries,current_query):
    current_query.lower()
    q = current_query.split(" ")

    curr_max_for_q = -1
    to_return = 0
    for index,p_query in enumerate(past_queries):
        p_query.lower()
        if (q == p_query):
            continue
        p_q = p_query.split(" ")
        curr_score = 0
        for word in p_q:
            curr_score+=q.count(word)

        if (curr_score > curr_max_for_q ):
            curr_max_for_q = curr_score
            to_return = index


    return past_queries[index]



