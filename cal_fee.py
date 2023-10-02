from datetime import date
import datetime
import calendar



def main():
    amount = float(input("Input amount: "))
    begindate = input("Input Begindate (วัน/เดือน/ปี ค.ศ.) ตัวอย่าง 17/1/2023: ") #input begindate
    enddate = input("Input Enddate  (วัน/เดือน/ปี ค.ศ.) ตัวอย่าง 30/3/2023: ") #input enddate
    print()
    print()
    print(cal_fee(amount,begindate,enddate))



def cal_fee(amount,begindate,enddate):
    fee = 0 #ส้ร้างตัวแปร fee สำหรับเก็บ่ค่า fee
    count_loop =0  #สร้างตัวแปรเก็บค่า loop
    begindate = begindate.split("/")
    enddate = enddate.split("/")
    begin_date = date(int(begindate[2]),int(begindate[1]),int(begindate[0]))
    end_date = date(int(enddate[2]),int(enddate[1]),int(enddate[0]))
    day = (end_date-begin_date)+datetime.timedelta(days=1) #คำนวณหาจำนวนวัน
    time = datetime.timedelta
    #คำนวณค่าธรรมเนียมของเดือนแรก
    if (day - time(calendar.monthrange(int(begindate[2]), int(begindate[1]))[1])).days  <= 0:
        fee += day.days*(0.02/calendar.monthrange(int(begindate[2]), int(begindate[1]))[1])*amount
        day -= day
        #print(f"ค่าธรรมเนียมเมื่อสิ้นสุดเดือนที่ 1 เท่ากับ {fee:,.2f} บาท")
    else:
        fee += (time(calendar.monthrange(int(begindate[2]), int(begindate[1]))[1]) - time(begin_date.day)+time(days=1)).days *(0.02/calendar.monthrange(int(begindate[2]), int(begindate[1]))[1])*amount
        day -= (time(calendar.monthrange(int(begindate[2]), int(begindate[1]))[1]) -time(begin_date.day)+time(days=1))
        count_loop +=1
        #print()
        #print(f"ค่าธรรมเนียมเมื่อสิ้นสุดเดือนที่ 1 เท่ากับ {fee:,.2f} บาท")

        while day.days>0:  #คำนวณค่าธรรมเนียมของเดือนถัดๆไป
            if day - time(calendar.monthrange(int(begindate[2]), int(begindate[1])+count_loop)[1]) < time(days=0):
                fee += day.days*0.02*amount/calendar.monthrange(int(begindate[2]), int(begindate[1])+count_loop)[1]
                day -= day
                count_loop += 1
            else:
                fee += 0.02*amount
                day -= time(calendar.monthrange(int(begindate[2]), int(begindate[1])+count_loop)[1])
                count_loop +=1
                #print(f"ค่าธรรมเนียมเมื่อสิ้นสุดเดือนที่ {count_loop} เท่ากับ {fee:,.2f} บาท")
                #print(f"ค่าธรรมเนียมเมื่อสิ้นสุดเดือนที่ {count_loop} เท่ากับ {fee:,.2f} บาท")


    return (f"{begin_date.day} {calendar.month_name[begin_date.month]}  {begin_date.year} to {end_date.day} {calendar.month_name[end_date.month]} {end_date.year} amount {fee:,.2f} baht")



if __name__ == "__main__":
    main()
