def search(query, ranking=lambda r: -r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)

def reviewed_both(r, s):
    return len([x for x in r.reviewers if x in s.reviewers])

class Restaurant:
    all = []
    def __init__(self, name, stars, reviewers):
        self.name,self.stars = name, stars
        self.reviewers = reviewers
        Restaurant.all.append(self)
    
    def similar(self, k, similarity = reviewed_both):
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key = lambda r:-similarity(self,r))[:k]

    def __repr__(self):
        return '<' + self.name + '>'

import json 

reviewers_for_resturant = {}
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business.id']
    if biz not in reviewers_for_resturant:
        reviewers_for_resturant[biz] = [r['user_id']]
    else:
        reviewers_for_resturant[biz].append(r['user_id'])

for line in open('resturants.json'):
    r = json.loads(line)
    reviewers = reviewers_for_resturant[r['business_id']]
    Restaurant(r['name'],r['stars'],reviewers)

results = search('Thai')
for r in results:
    print(r, 'is similar to', r.similar(3))
