#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - the function will run as many times as n

b) O(n^2) - The function has two loops, the first runs n times, the nested second has to run n-2 times, so maybe it could also be O(nlogn)

c) O(n) - the recursive function only runs as many times as there are bunnies

## Exercise II

I would go to the half way point of the n floors and drop the egg
If it breaks then I know every higher floor doesn't matter, eliminating half of the total floors.
If the egg doesn't break, I would know the lower floors are safe and don't matter, eliminating half of the total floors.

    I would then continue the process of finding the halfway of remaining floors and drop the egg then apply the logic above to eventually find the highest floor where the egg is still safe to drop.

This is a binary search, and it's runtime complexity would close to O(log(n))
