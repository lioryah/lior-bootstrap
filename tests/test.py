import fire

class Solution(object):
    def twoSum(self, nums, target):
        
        for i in nums:
            print(i)
            for j in nums:
                print(j)
                if ((i+j == target) and (nums.index(i) != nums.index(j))):
                    print(i+j)
                    return nums.index(i),nums.index(j)

def main_():
#    import fire
#    fire.Fire(flip_cli)

    fire.Fire()
    Solution.twoSum([3,3],6)


if __name__ == '__main__':
    main_()