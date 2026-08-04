class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in "+-*/":
                #print("a", t)
                a = st.pop()
                b = st.pop()
                if t == '+':
                    c = a + b
                elif t == '-':
                    c = b - a
                elif t == '*':
                    c = a * b
                else:
                    c = int(float(b) / float(a))
                st.append(c)
            else:
                st.append(int(t))
            print(st)
        return st[0]