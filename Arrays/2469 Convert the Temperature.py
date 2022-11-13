class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [273.15+celsius,(celsius*(9/5)+32)]
