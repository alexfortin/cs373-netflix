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
        self.assertEqual(w.getvalue(),"10036:\n3.8\n3.7\n3.5\nRMSE: 0.61\n")

    def test_netflix_solve_2 (self) :
        r = StringIO("9989:\n1800566\n999:\n2192206\n1459773\n9981:\n1506089\n71712\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(),"9989:\n3.4\n999:\n2.9\n3.0\n9981:\n4.3\n4.1\nRMSE: 0.93\n")

    # def test_netflix_solve_3 (self) :
        # r = StringIO("1000:
        # w = StringIO()
        # collatz_solve(r, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")   


    # -----
    # write
    # -----

    def test_write (self) :
        w = StringIO()
        netflix_write(10, w)
        self.assertEqual(w.getvalue(), "10.0\n")
    
    # def test_write_2 (self) :
    #     w = StringIO()
    #     netflix_write(1, 10, w)
    #    self.assertEqual(w.getvalue(), "1 10 20\n")
        
    # def test_write_3 (self) :
    #     w = StringIO()
    #     netflix_write(1, 10, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n")


    # --------------
    # predictRatings
    # --------------
    def test_predictRatings (self) :
        rating = predictRatings('10036:\n', '2161')
        self.assertEqual(rating, 3.8479622641509432)


    # ------------
    # actualRating
    # ------------
    def test_actualRating (self) :
        rating = actualRating('10036:\n', '2161\n')
        self.assertEqual(rating, 3)


# ----
# main
# ----

if __name__ == "__main__" :
    main()
    
    