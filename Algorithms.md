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
#### 三、插入排序
> 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

![排序演示](http://wuchong.me/img/Insertion-sort-example-300px.gif)
```python
def insert_sort(arry):
    n = len(ary)
    for i in range(1,n):
        # 后一个元素和前一个元素比较
        # 如果前一个元素大
        if arry[i] < arry[i-1]:
            #将这个元素取出
            temp = arry[i]
            #保存下标
            index = i
            #从后往前依次比较每一个元素
            for j in range(i - 1, -i, -1):
                # 和比取出的元素大的元素交换
                if arry[j] > temp:
                    arry[j + 1] = arry[j]
                    index = j
                else:
                    break
            #插入元素
            arry[index] = temp
    return arry
```
####
####
####
####
####
####
