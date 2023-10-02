from cal_fee import cal_fee

def test_value():
    assert cal_fee(120000,"1/6/2023","26/6/2023") == "1 June  2023 to 26 June 2023 amount 2,080.00 baht"
    assert cal_fee(120000,"17/1/2023","31/1/2023") == "17 January  2023 to 31 January 2023 amount 1,161.29 baht"
    assert cal_fee(120000,"1/2/2023","31/5/2023") == "1 February  2023 to 31 May 2023 amount 9,600.00 baht"
    assert cal_fee(47101.60,"27/6/2023","30/6/2023") == "27 June  2023 to 30 June 2023 amount 125.60 baht"
    assert cal_fee(47101.60,"1/7/2023","30/8/2023") == "1 July  2023 to 30 August 2023 amount 1,853.68 baht"
    assert cal_fee(6779.02,"31/8/2023","31/8/2023") == "31 August  2023 to 31 August 2023 amount 4.37 baht"
    assert cal_fee(493548.29,"2/9/2023","13/9/2023") == "2 September  2023 to 13 September 2023 amount 3,948.39 baht"
