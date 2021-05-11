from stack import Stack

if __name__ == '__main__':
    st = Stack()
    st.pop()
    for i in range(int(input())):
        value = int(input())
        st.push(value)
    print('Pop: ', st.pop())
    print('Get: ', st.get())
    print('Stack:', st)
