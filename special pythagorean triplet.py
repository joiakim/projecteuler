import random
import math



while True:
    for i in range(100, 999):

        for v in range(i+1, 999):

            val = i*i + v*v
            c_val = math.isqrt(val)

            sum_0f_val = i + v + c_val
            if i < v < c_val and sum_0f_val == 1000 and c_val*c_val == i*i + v*v:
                print(i, v, c_val, "product of values:", i*v*c_val)
    print("Done")

    break







