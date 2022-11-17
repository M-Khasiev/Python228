st = input("Введите строку: ")
let = input("Введите букву,которую вы желаете видеть в верхнем регистре кроме первого и последнего вхождения: ")
st = st.split(let.lower())
let = let.upper()
n = let.join(st)
conclusion = n[:n.find(let)] + let.lower() + n[n.find(let) + 1:n.rfind(let)] + let.lower() + n[n.rfind(let) + 1:]
print(conclusion)

