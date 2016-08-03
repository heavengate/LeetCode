class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        if numerator == 0:
            return "0"
        result = ""
        if denominator < 0:
            denominator *= -1
            numerator *= -1
        if numerator < 0:
            numerator *= -1
            result += '-'
        
        result += str(numerator/denominator)
        remain = numerator % denominator
        if remain == 0:
            return result
        
        result += '.'
        mods = []
        cycle = []
        while remain != 0 and remain not in mods:
            mods.append(remain)
            cycle.append((remain * 10) / denominator)
            remain = (remain * 10) % denominator
        if remain == 0:
            index = len(cycle)
        else:
            index = mods.index(remain)
        for i in range(index):
            result += str(cycle[i])
        if remain != 0:
            result += '('
            for i in range(index,len(cycle)):
                result += str(cycle[i])
            result += ')'
        
        return result
