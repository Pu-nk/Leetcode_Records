### Leetcode_Records

---
happy leetcoding!!! 
This repo is used for recording the experience of getting over leetcode

---

- 这是我新学期第一天刷题[X的平方根](2023-02-21)， 刷刷开冲！！！！！！！
- 深夜social回来的匆忙每日一题[在排序数组中查找元素的第一个和最后一个位置](2023-02-22)，其实没有想到分别写两个函数来找上下界，肤浅了！
- 似曾相识的一道题[搜索旋转排序数组 II](2023-02-23)，当初面旷视好像做过当时就挂住了，但是现在还是不会哈哈
- 今天比较悠闲，多刷了两道题[寻找旋转排序数组中的最小值 II](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/) 和 [旋转数组的最小数字](https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)， 关于二分搜索目前可以总结的：
	- 寻找区间：定义`upbound`和`lowbound`两个函数分别搜索，区别在于当碰到`nums[mid] == target`的时候如果是寻找左区间的话`left`往左走， 寻找右区间的话`right`往右走。
	- 寻找值：如果`nums[mid] == target`直接返回就完事了，如果大于就`right = mid - 1`,如果小于就`left = mid + 1`
	- 旋转数组找目标值：找到连续的递增区间，先看看`nums[mid] == target`直接返回就完事了，不然就分情况讨论，只旋转一次的话要么左边单调要么右边单调，根据大小关系判断即可，找到单调区间先看看目标值在不在里面，在里面的话缩小边界，不在里面的话放弃这个区间，另外当`nums[mid] == nums[left] or nums[mid] == nums[right]`的时候缩小一步区间
	- 旋转数组找最小值：找到旋转点即可，比较mid和right之间的大小关系，如果`nums[mid] > nums[right]`这就说明反转点肯定在这个区间里`left = mid + 1`，但是如果`nums[mid] >< nums[right]`就不好说了，就先在left那边找`right = mid`
	- while的条件是`<`还是`<=`取决于你的左右指针是全闭区间还是左闭右开的，如果左闭右开的话就是`<`，同理此时缩小区间也不需要加一或者减一，因为从一开始你的mid计算结果就隐含了这一条件。
- 又刷了一道题[有序数组中的单一元素](https://leetcode.cn/problems/single-element-in-a-sorted-array/)， 休息了休息了！！！
- 周六也要刷力扣，二分搜索做这道题还是挺难的！！！[寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/)
- 周日健身完匆忙补上，二分搜索完结撒花🎉！开始排序算法第一题 [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
---
- 周一作业已交 [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/)
