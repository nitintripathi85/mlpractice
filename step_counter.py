import numpy as np
import matplotlib.pyplot as plt

step = 0
np.random.seed()
rollNumber = 0
stepList =[0]
rollList = [0]

while step < 50:
    dice = np.random.randint(1, 7)
    if dice <= 2:
        if step != 0:
            step -= 1
    elif 3 <= dice <= 5:
        step += 1
    else:
        step += np.random.randint(1, 7)
    rollNumber += 1
    stepList.append(step)
    rollList.append(dice)
    print ("Try# " + str(rollNumber) + " Rolled : " + str(dice) + "-- Now at step " + str(step))

plt.plot(stepList)
plt.show()
plt.clf()

plt.hist(rollList)
plt.show()
plt.clf()