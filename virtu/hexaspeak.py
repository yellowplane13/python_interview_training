class Solution:
    def toHexspeak(self, num: str) -> str:
        hexa=hex(int(num))
        hexStr=str(hexa)
        hexa=hexStr.replace("0x","")
        print(hexa)
        ans=""
        for i,v in enumerate(hexa):
            if v.isalpha():
                print("I'm in if")
                ans+=v
            elif v=="1":
                print("I'm in elif 1")
                ans+="I"
                print("ans1",ans)
            elif v=="0":
                print("I'm in elif 2")
                ans+="O"
            else:
                print("I'm in else")
                return "ERROR"

        print(ans)

        return ans




op=Solution()
#op.toHexspeak("257")
#op.toHexspeak("257")
print(op.toHexspeak("3"))