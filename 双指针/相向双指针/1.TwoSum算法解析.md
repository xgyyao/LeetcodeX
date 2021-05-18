### [两数之和](https://leetcode-cn.com/problems/two-sum/)
|难度|简单|
|---|---|

题目描述:

   给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

   你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

   你可以按任意顺序返回答案。
    
示例1:

    输入：nums = [2,7,11,15], target = 9
    输出：[0,1]
    解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
    
示例2:

    输入：nums = [3,2,4], target = 6
    输出：[1,2]
    
示例3：

    输入：nums = [3,3], target = 6
    输出：[0,1]
    
提示：
* `2 <= nums.length <= 103`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
* 只会存在一个有效答案

算法解析：
使用双指针的思想，建立两个指针`p1`和`p2`，初始状态分别指向数组的第0
个索引以及第一个索引。若`p1`和`p2`所指的数字相加与`target`相同，那么
则返回`p1`和`p2`,若不相同，则从`p2`开始向右移动，并计算`p1`与`p2`之和，
当`p2`到达数组末尾时，`p1`向右移动，此时`p2`返回至`p1`索引+1的位置，
继续上述步骤，直至`p1`和`p2`所指数字相加与`target`相等。

代码：
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
```




