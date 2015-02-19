#!/usr/bin/env python3

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import rmse, netflix_solve, netflix_write, predictRatings, actualRating

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    
    # ----
    # rmse
    # ----

    def test_rmse (self) :
        a    = [2, 3, 4]
        p    = [2, 3, 4]
        result = rmse(a, p)
        self.assertEqual(result, 0)

    def test_rmse_2 (self) :
        a    = [2, 3, 4]
        p    = [3, 2, 5]
        result = rmse(a, p)
        self.assertEqual(result, 1)

    def test_rmse_3 (self) :
        a    = [2, 3, 4]
        p    = [4, 1, 6]
        result = rmse(a, p)
        self.assertEqual(result, 2)
        
    def test_rmse_4 (self) :
        a    = [2, 3, 4]
        p    = [4, 3, 2]
        result = rmse(a, p)
        self.assertEqual(result, 1.632993161855452)
        
    # -----
    # solve
    # -----

    def test_netflix_solve (self) :
        r = StringIO("10036:\n2161\n234405\n2494920\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(),"10036:\n4.1\n3.7\n3.3\nRMSE: 0.75\n")

    def test_netflix_solve_2 (self) :
        r = StringIO("9989:\n1800566\n999:\n2192206\n1459773\n9981:\n1506089\n71712\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(),"9989:\n3.2\n999:\n2.2\n2.5\n9981:\n5.1\n4.5\nRMSE: 0.82\n")

    def test_netflix_solve_3 (self) :
        r = StringIO("10001:\n262828\n2609496\n1474804\n831991\n267142\n2305771\n220050\n1959883\n27822\n2570808\n90355\n2417258\n264764\n143866\n766895\n714089\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10001:\n3.5\n4.3\n4.2\n3.1\n4.6\n3.5\n3.5\n3.7\n3.9\n4.2\n4.2\n4.2\n2.5\n4.4\n3.5\n3.5\nRMSE: 0.85\n")   


    # -----
    # write
    # -----

    def test_write (self) :
        w = StringIO()
        netflix_write(10, w)
        self.assertEqual(w.getvalue(), "10.0\n")
    
    def test_write_2 (self) :
        w = StringIO()
        netflix_write(1127, w)
        self.assertEqual(w.getvalue(), "1127.0\n")
        
    def test_write_3 (self) :
        w = StringIO()
        netflix_write(56511, w)
        self.assertEqual(w.getvalue(), "56511.0\n")


    # --------------
    # predictRatings
    # --------------
    def test_predictRatings (self) :
        rating = predictRatings('10036:\n', '2161')
        self.assertEqual(rating, 4.084924528301887)

    def test_predictRatings_2 (self) :
        rating = predictRatings('10:\n', '1531863')
        self.assertEqual(rating, 2.758035714285714)

    def test_predictRatings_3 (self) :
        rating = predictRatings('10004:\n', '1903515')
        self.assertEqual(rating, 4.593)      

    def test_predictRatings_4 (self) :
        rating = predictRatings('4794:\n', '1437271')
        self.assertEqual(rating, 3.0320000000000005)

    # ------------
    # actualRating
    # ------------
    def test_actualRating (self) :
        rating = actualRating('10036:\n', '2161\n')
        self.assertEqual(rating, 3)

    def test_actualRating_2 (self) :
        rating = actualRating('10:\n', '1531863\n')
        self.assertEqual(rating, 3)

    def test_actualRating_3 (self) :
        rating = actualRating('10004:\n', '1903515\n')
        self.assertEqual(rating, 5)


# ----
# main
# ----

if __name__ == "__main__" :
    main()
    
    