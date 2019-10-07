## HW1
### Command
```
$python3 main.py [testcaseNum] [vi/pi]
```
### Policy Iteration
1. initialize our policy to be a random policy and load our initial value.
2. evaluate policy and derive our value function
3. improve our policy by choosing greedily.
4. if the new value function and the old one is the same down to the third decimal places, terminate. Otherwise, keep on repeating 2. and 3.

### Value Iteration
1. load our initial value
2. update value function using the vlue iteration equation in the lecture.
3. If the new value funciton and the old one is the same down to the third deciaml places, terminates. Otherwise repeat step 3.
4. Update policy once by choosing greedily.


### Testing

I used the unittest library in python to test the correctness of each function. This way, we can avoid printing out value or policy function and checking them manuelly for correctness. Code below is one of the function test.

![](https://i.imgur.com/mCu3BYl.png)


### Test Result

#### case1
* takes 5 steps of policy iteration to converge
* takes 3 steps of value iteration to converge
![](https://i.imgur.com/vpqABhv.png)


#### case2

* takes 8 steps of policy iteration to converge
* takes 6 steps of value iteration to converge
![](https://i.imgur.com/RAMMxHW.png)

#### case3

* takes 8 steps of policy iteration to converge
* takes 6 steps of value iteration to converge
![](https://i.imgur.com/P7pANu0.png)

#### case4

* takes 6 steps of policy iteration to converge
* takes 4 steps of value iteration to converge

![](https://i.imgur.com/PPK3oCY.png)

### Problem and Discussion
* Value iteration seems to be faster than policy iteration.

* I forgot to update value synchronously, which leads to weird result. To solve this, I create a new value array and store the newly updated value in the array. Then copy the new array to replace the value array when we have iterated through all the state in the array.

* At first i check float value with "assertEqual" and it always result in error whenever I ran the test. I later figure out that, for float number, we use "assertAlmostEqual" to test them. This will test the number equality only down to the seventh deciam point.
