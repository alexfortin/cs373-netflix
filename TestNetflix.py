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
        assert result == 0

    def test_rmse_2 (self) :
        a    = [2, 3, 4]
        p    = [3, 2, 5]
        result = rmse(a, p)
        assert result == 1

    def test_rmse_3 (self) :
        a    = [2, 3, 4]
        p    = [4, 1, 6]
        result = rmse(a, p)
        assert result == 2
        
    def test_rmse_4 (self) :
        a    = [2, 3, 4]
        p    = [4, 3, 2]
        result = rmse(a, p)
        assert result == 1.632993161855452
        
    # -----
    # solve
    # -----

    def test_netflix_solve (self) :
        r = StringIO("1:
        30878
        2647871
        1283744
        2488120
        317050
        1904905
        1989766
        14756
        1027056
        1149588
        1394012
        1406595
        2529547
        1682104
        2625019
        2603381
        1774623
        470861
        712610
        1772839
        1059319
        2380848
        548064")
        w = StringIO()
        collatz_solve(r, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_netflix_solve_2 (self) :
        r = StringIO("10:
        1952305
        1531863")
        w = StringIO()
        collatz_solve(r, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_netflix_solve_3 (self) :
        r = StringIO("1000:
        2326571
        977808
        1010534
        1861759
        79755
        98259
        1960212
        97460
        2623506
        2409123
        1959111
        809597
        2251189
        537705
        929584
        506737
        708895
        1900790
        2553920
        1196779
        2411446
        1002296
        1580442
        100291
        433455
        2368043
        906984
        10000:
        200206
        523108")
        w = StringIO()
        collatz_solve(r, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")   


    # -----
    # write
    # -----

    def test_write (self) :
        w = StringIO()
        netflix_write(1, 10, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n")
    
    def test_write_2 (self) :
        w = StringIO()
        netflix_write(1, 10, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n")
        
    def test_write_3 (self) :
        w = StringIO()
        netflix_write(1, 10, w)
#        self.assertEqual(w.getvalue(), "1 10 20\n")


    # -------
    # predict
    # -------
    
    