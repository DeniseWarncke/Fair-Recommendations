from lenskit import batch, topn, util
from lenskit import crossfold as xf

from lenskit.algorithms import Recommender, als, item_knn as knn
from lenskit import topn
#from lenskit.algorithms import als, item_knn as knn
#from lenskit.metrics import topn as tnmetrics 
import numpy as np

import pandas as pd

class LegMedLensKit():

    def loadData():  
        ratings = pd.read_csv('/Users/denisehansen/Desktop/movielens-dataset/ratings.dat', sep='::',
                      names=['user', 'item', 'rating', 'timestamp'])
        print (ratings.head())
        return(ratings)

    
    #print ("test")
    ratings = loadData()
    data_matrix = np.array(ratings.pivot(index = 'item', columns = 'user', values = 'rating'))
    print(data_matrix)
    data_matrix_rev = np.nan_to_num(data_matrix)
    print(data_matrix_rev) 

    algo_ii = knn.ItemItem(20)
    algo_als = als.BiasedMF(50)

    def eval(aname, algo, train, test):
        print("test")
        fittable = util.clone(algo)
        fittable = Recommender.adapt(fittable)
        fittable.fit(train)
        users = test.user.unique()
        # now we run the recommender
        recs = batch.recommend(fittable, users, 100)
        # add the algorithm name for analyzability
        recs['Algorithm'] = aname
        return recs
    
    all_recs = []
    test_data = []
    
    for train, test in xf.partition_users(ratings[['user', 'item', 'rating']], 1, xf.SampleFrac(0.2)):
        test_data.append(test)
        #print(test.head(10))
        all_recs.append(eval('ItemItem', algo_ii, train, test))
        all_recs.append(eval('ALS', algo_als, train, test))

    print("test2")
    all_recs = pd.concat(all_recs, ignore_index=True)
    print(all_recs.head())
    test_data = pd.concat(test_data, ignore_index=True) 
    #print(test_data.head)

    
    rla = topn.RecListAnalysis()
    rla.add_metric(topn.ndcg)
    results = rla.compute(all_recs, test_data)
    results.head()

    results.groupby('Algorithm').ndcg.mean()
    results.groupby('Algorithm').ndcg.mean().plot.bar()

    
    # print("test4")
    # user_dcg = all_recs.groupby(['Algorithm', 'user']).rating.apply(tnmetrics.dcg)
    # print("test5")
    # user_dcg = user_dcg.reset_index(name='DCG')
    # user_dcg.head()

    # ideal_dcg = tnmetrics.compute_ideal_dcgs(test)
    # print(ideal_dcg.head())

    # user_ndcg = pd.merge(user_dcg, ideal_dcg)
    # user_ndcg['nDCG'] = user_ndcg.DCG / user_ndcg.ideal_dcg
    # print(user_ndcg.head())

    
    # user_ndcg.groupby('Algorithm').nDCG.mean()
    # user_ndcg.groupby('Algorithm').nDCG.mean().plot.bar()
    
 