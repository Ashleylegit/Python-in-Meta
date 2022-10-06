list5 = [10,20,30,40,50,60,70,80,90]
list10 = [15,25,35,45,55,65,75,85,95]

count = 0
#outer loop
for x in list5:
    count +=1

    #inner loop
    for y in list10:
        count +=1

        print(count)

        import time
        start_time = time.time()
        #outer loop
        for i in range(100):

            #inner loop
            for k in range(100):
               print(0, end = "")
            print()
        print(round((time.time()- start_time), 2))
