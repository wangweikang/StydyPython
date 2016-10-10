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

#### 四、希尔排序
> 将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。

```python
def shell_sort(arry):
    n = len(arry)
    #初始步长
    gap = round(n/2)
    while gap > 0:
        for i in range(gap, n):
            # 插入排序
            temp = arry[i]
            j = i
            while(j >= gap and arry[j - gap] > temp):
                arry[j] = arry[j - gap]
                j = j - gap
            arry[j] = temp
        # 得到新的步长
        gap = round(gap/2)
    return arry
```
> 想来想去，其实希尔排序就是插入排序的优化版  mdzz(

#### 五、归并排序
> 比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

![排序演示](http://wuchong.me/img/Merge-sort-example-300px.gif)

代码用迭代法实现:
```python
def merge_sort(arry):
    if len(arry) <= 1:  #长度不大于1的数组是有序的
        return arry
    num = int(len(arry)/2)    #二分分解
    left = merge_sort(arry[:num])
    right = merge_sort(arry[num:])
    return merge(left, right)  # 合并数组


def merge(left, right):
    #将两个有序数组left[]和right[]合并成一个大的有序数组
    l,r = 0,0
    result = []
    while l<len(left) and r < len(right):
        if eft[l] < right(left[l]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
```

#### 六、快速排序
> 1.挑出一个元素作为基准数。2.将比基准数大的放到右边，小于或等于它的数都放到左边。3.左右区间递归执行第二步，直至各区间只有一个数。

![排序演示](http://wuchong.me/img/Quicksort-example.gif)

```python
def quick_sort(arry):
    less = []
    pivotList = []
    more = []
    #递归
    if len(arry) <= 1:
        return arry
    else:
        #将第一个数作为基准
        pivot = arry[0]
        for i in arry:
            #将比基准小的数放到less数组
            if i < pivot;
                less.append(i)
            #将比基准大的数放到more数组
            elif i > piovt:
                more.append(i)
            #将和基准相同的数保存在基准数列
            else:
                pivotList.append(i)
        #对less和more数组继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more
```

#### 七、堆排序


#### 八、系统自带排序 (逃
```python
arry.sort()
```
