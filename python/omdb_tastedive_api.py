import requests_with_caching as req

def get_movies_from_tastedive(mname):
    baseurl = 'https://tastedive.com/api/similar'
    parameters = {}
    parameters['q'] = mname
    parameters['type'] = 'movies'
    parameters['limit'] = 5
    data = req.get(baseurl, params = parameters)
    return data.json()

def extract_movie_titles(resp_dict):
    return [movie['Name'] for movie in resp_dict['Similar']['Results']]

def get_related_titles(mlist):
    a = {i for l in mlist for i in extract_movie_titles(get_movies_from_tastedive(l))}
    return list(a)

def get_movie_data(mname):
    baseurl = 'http://www.omdbapi.com/'
    parameters = {}
    parameters['t'] = mname
    parameters['r'] = 'json'
    data = req.get(baseurl, params = parameters)
    return data.json()

def get_movie_rating(res_dict):
    for i in res_dict['Ratings']:
        if 'Rotten Tomatoes' in i.values():
            return int(float(i['Value'].strip('%')))
    return 0

def get_sorted_recommendations(mlist):
    usort_mlist = get_related_titles(mlist)
    l = sorted([(i,get_movie_rating(get_movie_data(i))) for i in usort_mlist],key = lambda x: x[1],reverse = True)
    return [i[0] for i in l]
