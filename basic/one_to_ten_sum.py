class OneToTenSum (object):

    def one_to_ten_sum(self):
        #example 1
        sum2 = 0
        # for i in []:
        for i in range(1,10+1):
            sum2 += i

        # example 2
        '''sum = sum(i for i in range(1, 11))
        print(sum(i for i in range(1,20)))
        print(sum(i for i in range(1,19)))'''

        # example 3
        sum1 = sum(range(1, 11))
        print(sum1)

    def one_to_ten_sum_2(self):
        print(sum(range(1,11)))

