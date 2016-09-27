## Algorithms
>> 所有默认 min -> max

![算法指标对比](http://ww1.sinaimg.cn/large/81b78497jw1emncvtdf1qj20u10afn0r.jpg)
#### 一、冒泡排序

```python
def dubble_sort(arry):
    n = len(arry)
    for i in range(n):
        for i in range(1,n-i):
            if arry[j-1] > arry[j]:
                arry[j-1],arry[j] = arry[j], arry[j-1]
    return arry
```
> 优化版：通过记录最后发生交换的位置确定下一次循环的范围

```python
def dubble_sort_review(arry):
    n = len(arry)
    k = n
    for i in range(n):
        flag = 1
        for j in range(1,n-i):
            if arry[j-1] > arry[j]:
                arry[j-1],arry[j] = arry[j], arry[j-1]
                k = j
                flag = 0
        if flag:
            braeak
    return arry
```

#### 二、选择排序

```python
def select_sort(arry):
    n = len(arry)
    for i in range(0, n):
        min = 1
        for j in range(i + 1, n):
            if arry[j] < arry[min]:
                min = j
        arry[min],arry[i] = arry[i],arry[min]
    return arry
```
####
####
####
####
####
####
####
