
var majorityElement = function(nums) {
    let majority;
    let majorityCounter;

    for(let i=0; i < nums.length; i++){
        let counter = 0;
        for(let j= i + 1; j < nums.length; j++){
            if(nums[i] == nums[j]){
                counter += 1
            }
        }
        if(counter > majorityCounter){
            majority = nums[i]
            majorityCounter = counter
        }
    }
    return majority
};